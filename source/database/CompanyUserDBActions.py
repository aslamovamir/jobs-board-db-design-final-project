import sqlite3
from model.Company.CompanyUser import CompanyUser
from model.Company.CompanyModelHelper import CompanyModelHelper
from helpers.MenuHelper import MenuHelper
from database.QueryHelpers.QueryHelper import QueryHelper


# class for the CompanyUserDBActions
class CompanyUserDBActions:

    # method to execute an SQL query to insert a new Company User row into the CompanyUser table
    def InsertNewCompanyUser(companyUser: CompanyUser) -> bool:
        try:

            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()
            # query
            # insert a new user row into the table
            # the value for the column "DateLogin" is skipped so its default value becomes Null
            DatabaseCursor.execute("""
                INSERT INTO CompanyUser (ID, Username, CompanyName, Email, DateRegistered)
                    VALUES (:id, :username, :company_name, :email, CURRENT_TIMESTAMP);
                """, 
                {
                    'id': companyUser.ID, 
                    'username': companyUser.Username, 
                    'company_name': companyUser.CompanyName,
                    'email': companyUser.Email
                }
            )
            
            # commit the query operation to the database
            DatabaseConnection.commit()

            # for safety, close the database connection
            DatabaseConnection.close()

            return True


        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="CompanyUserDBActions::InsertNewCompanyUser")
            return False

    
    # method to query all Company User rows from the CompanyUser table
    def QueryAllCompanyUserRows() -> list[dict()]:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()
            # query
            DatabaseCursor.execute("SELECT * FROM CompanyUser;")
            
            # keys for the columns of the CompanyUser table
            keys: list() = ['pk', 'ID', 'Username', 'CompanyName', 'Email', 'DateRegistered', 'DateLastLogin']
            output: list() = []
            try:
                output = QueryHelper.ConvertTupleToDict(query=DatabaseCursor.fetchall(), dictKeys=keys)
            except Exception as e:
                MenuHelper.DisplayErrorException(exception=e, 
                    errorSource="CompanyUserDBActions::QueryAllCompanyUserRows::QueryHelper.ConvertTupleToDict")


            # commit the query operation to the database
            DatabaseConnection.commit()

            # for safety, close the database connection
            DatabaseConnection.close()

            # return True as success confirmation
            return output

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="CompanyUserDBActions::QueryAllCompanyUserRows")
            return False
    

    # method to check if an ApplicantUser exists with the given username and password
    def CheckExistsGivenUsernamePassword(username: str, password: str) -> bool:
        id: str = CompanyModelHelper.CreateCompanyUserId(username=username, password=password)

        # database connection object to the JobsBoard database
        DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
        # database cursor object to manipulate SQL queries
        DatabaseCursor = DatabaseConnection.cursor()
        # query
        DatabaseCursor.execute("""SELECT * FROM CompanyUser WHERE ID = ?""", (id,))

        if len(DatabaseCursor.fetchall()) == 0:
            # for safety, close the database connection
            DatabaseConnection.close()

            print('\nUser with this username and password does not exist.')
            return False
        else:
            # if the user exists, we update the DateLastLogin to capture the time the user's account has been accessed
            DatabaseCursor.execute("""UPDATE CompanyUser SET DateLastLogin=CURRENT_TIMESTAMP WHERE ID = ?""", (id,))
            # commit the query to the database
            DatabaseConnection.commit()
            # for safety, close the database connection
            DatabaseConnection.close()
            return True
    

    # method to check if an ApplicantUser exists with the given username
    def CheckExistsGivenUsername(username: str) -> bool:
        # database connection object to the JobsBoard database
        DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
        # database cursor object to manipulate SQL queries
        DatabaseCursor = DatabaseConnection.cursor()
        # query
        DatabaseCursor.execute("""SELECT * FROM CompanyUser WHERE Username = ?""", (username,))


        if len(DatabaseCursor.fetchall()) == 0:
            # for safety, close the database connection
            DatabaseConnection.close()
            return False
        else:
            # for safety, close the database connection
            DatabaseConnection.close()
            return True

    
    # method to return the CompanyUser with the given id
    def ReturnCompanyUser(id: str) -> CompanyUser:
        # database connection object to the JobsBoard database
        DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
        # database cursor object to manipulate SQL queries
        DatabaseCursor = DatabaseConnection.cursor()

        # query
        DatabaseCursor.execute("""SELECT * FROM CompanyUser WHERE ID = ?""", (id,))
        # query results
        records = DatabaseCursor.fetchall()

        # for safety, close the database connection
        DatabaseConnection.close()

        if len(records) == 1:
            # TO_DO: CREATE A DB METHOD TO UPDATE THE DATELASTLOGIN COLUMN FOR THE USER

            # keys for the columns of the ApplicantUser table
            keys: list() = ['pk', 'ID', 'Username', 'CompanyName', 'Email', 'DateRegistered', 'DateLastLogin']
            dictResult: dict() = QueryHelper.ConvertTupleToDict(query=records, dictKeys=keys)[0]

            return CompanyUser(
                Username=dictResult['Username'],
                Password="",
                Email=dictResult['Email'],
                CompanyName=dictResult['CompanyName'],
                DateRegistered=dictResult['DateRegistered'],
                DateLastLogin=dictResult['DateLastLogin']
            )
        else:
            raise Exception("\nError! There are applicant users with duplicate ID's.")

    
    # method to update account information of a company user
    def UpdateAccountInfo(loggedUser: CompanyUser) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            DatabaseCursor.execute("""UPDATE CompanyUser SET Email = ?, CompanyName = ? WHERE Username = ?;""", 
                (loggedUser.Email, loggedUser.CompanyName, loggedUser.Username,)
            )

            # commit the query operation to the database
            DatabaseConnection.commit()

            # for safety, close the database connection
            DatabaseConnection.close()

            # return True as success confirmation
            return True

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::UpdateAccountInfo")
            return False