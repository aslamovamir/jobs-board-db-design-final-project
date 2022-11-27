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
            print('\nUser with this username and password does not exist.')
            return False
        else:
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
            return False
        else:
            return True