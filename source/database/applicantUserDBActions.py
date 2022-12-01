import sqlite3
from database.QueryHelpers.QueryHelper import QueryHelper
from helpers.MenuHelper import MenuHelper
from model.Applicant.ApplicantUser import ApplicantUser
from model.Applicant.ApplicantModelHelper import ApplicantModelHelper
from model.Applicant.ApplicantProfile import ApplicantProfile


# class for the ApplicantUserDBActions
class ApplicantUserDBActions:

    # method to execute an SQL query to insert a new Applicant User row into the ApplicantUser table
    def InsertNewApplicantUser(applicantUser: ApplicantUser) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()
            # query
            # insert a new user row into the table
            # the value for the column "DateLogin" is skipped so its default value becomes Null
            DatabaseCursor.execute("""
                INSERT INTO ApplicantUser (ID, Username, Email, FirstName, LastName, DateRegistered)
                    VALUES (:id, :username, :email, :first_name, :last_name, CURRENT_TIMESTAMP);
                """, 
                {
                    'id': applicantUser.ID, 
                    'username': applicantUser.Username, 
                    'email': applicantUser.Email,
                    'first_name': applicantUser.FirstName, 
                    'last_name': applicantUser.LastName,
                }
            )
            
            # commit the query operation to the database
            DatabaseConnection.commit()

            # for safety, close the database connection
            DatabaseConnection.close()

            # return True as success confirmation
            return True


        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::InsertNewApplicantUser")
            return False


    # method to query all Applicant User rows from the ApplicantUser table
    def QueryAllApplicantUserRows() -> list[dict()]:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()
            # query
            DatabaseCursor.execute("SELECT * FROM ApplicantUser;")
            
            # keys for the columns of the ApplicantUser table
            keys: list() = ['pk', 'ID', 'Username', 'Email', 'FirstName', 'LastName', 'DateRegistered', 'DateLastLogin']
            output: list() = []
            try:
                output = QueryHelper.ConvertTupleToDict(query=DatabaseCursor.fetchall(), dictKeys=keys)
            except Exception as e:
                MenuHelper.DisplayErrorException(exception=e, 
                    errorSource="ApplicantUserDBActions::QueryAllApplicantUserRows::QueryHelper.ConvertTupleToDict")


            # commit the query operation to the database
            DatabaseConnection.commit()

            # for safety, close the database connection
            DatabaseConnection.close()

            return output

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::QueryAllApplicantUserRows")
            return False

    
    # method to check if an ApplicantUser exists with the given username and password
    def CheckExistsGivenUsernamePassword(username: str, password: str) -> bool:
        try:
            id: str = ApplicantModelHelper.CreateApplicantUserId(username=username, password=password)

            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()
            # query
            DatabaseCursor.execute("""SELECT * FROM ApplicantUser WHERE ID = ?;""", (id,))

            if len(DatabaseCursor.fetchall()) == 0:
                # for safety, close the database connection
                DatabaseConnection.close()

                print('\nUser with this username and password does not exist.')
                return False
            else:
                # if the user exists, we update the DateLastLogin to capture the time the user's account has been accessed
                DatabaseCursor.execute("""UPDATE ApplicantUser SET DateLastLogin=CURRENT_TIMESTAMP WHERE ID = ?;""", (id,))
                # commit the query to the database
                DatabaseConnection.commit()
                # for safety, close the database connection
                DatabaseConnection.close()
                return True

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::CheckExistsGivenUsernamePassword")
            return False


    # method to check if an ApplicantUser exists with the given username
    def CheckExistsGivenUsername(username: str) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()
            # query
            DatabaseCursor.execute("""SELECT * FROM ApplicantUser WHERE Username = ?;""", (username,))

            if len(DatabaseCursor.fetchall()) == 0:
                # for safety, close the database connection
                DatabaseConnection.close()
                return False
            else:
                # for safety, close the database connection
                DatabaseConnection.close()
                return True
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::CheckExistsGivenUsername")
            return False

    
    # method to return the ApplicantUser with the given id
    def ReturnApplicantUser(id: str) -> ApplicantUser:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            # query
            DatabaseCursor.execute("""SELECT * FROM ApplicantUser WHERE ID = ?;""", (id,))
            # query results
            records = DatabaseCursor.fetchall()

            # for safety, close the database connection
            DatabaseConnection.close()

            if len(records) == 1:
                # keys for the columns of the ApplicantUser table
                keys: list() = ['pk', 'ID', 'Username', 'Email', 'FirstName', 'LastName', 'DateRegistered', 'DateLastLogin']
                dictResult: dict() = QueryHelper.ConvertTupleToDict(query=records, dictKeys=keys)[0]

                return ApplicantUser(
                    Username=dictResult['Username'],
                    Password="",
                    Email=dictResult['Email'],
                    FirstName=dictResult['FirstName'],
                    LastName=dictResult['LastName'],
                    DateRegistered=dictResult['DateRegistered'],
                    DateLastLogin=dictResult['DateLastLogin']
                )
            else:
                raise Exception("\nError! There are applicant users with duplicate ID's.")
        
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::ReturnApplicantUser")
            return False


    # method to update account information of an applicant user
    def UpdateAccountInfo(loggedUser: ApplicantUser) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            DatabaseCursor.execute("""UPDATE ApplicantUser SET Email = ?, FirstName = ?, LastName = ? WHERE Username = ?;""", 
                (loggedUser.Email, loggedUser.FirstName, loggedUser.LastName, loggedUser.Username,)
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

    
    # method to check if the applicant user has a profile added to the database
    def CheckUserHasProfile(loggedUser: ApplicantUser) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()
            # query
            # first get the ID
            DatabaseCursor.execute("""SELECT ID FROM ApplicantUser WHERE Username = ?;""", (loggedUser.Username,))
            queryResult = DatabaseCursor.fetchall()

            if len(queryResult) == 0:
                return False
            else:
                # now check if there is a row with the given ID in the ApplicantProfile table
                DatabaseCursor.execute("""SELECT * FROM ApplicantProfile WHERE ApplicantID = ?""", (queryResult[0][0],))
                queryResult = DatabaseCursor.fetchall()

                # for safety, close the database connection
                DatabaseConnection.close()

                if len(queryResult) == 0:
                    return False
                elif len(queryResult) == 1:
                    return True
                else:
                    raise Exception("\nFailure! The user has duplicate profiles in the Applicant Profiles table.\n")

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::CheckExistsGivenUsername")
            return False

    
    # method to return the ID of an applicant user
    def ReturnIDUser(username: str) -> str:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()
            # query
            DatabaseCursor.execute("""SELECT ID FROM ApplicantUser WHERE Username = ?""", (username,))
            queryResult = DatabaseCursor.fetchall()

            # for safety, close the database connection
            DatabaseConnection.close()

            if len(queryResult) == 1:
                return queryResult[0][0]
            else:
                return None

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::ReturnIDUser")

    
    # method to insert a new row into the ApplicantProfile table
    def InsertNewProfile(newProfile: ApplicantProfile) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()
            # query
            DatabaseCursor.execute("""INSERT INTO ApplicantProfile (
                ApplicantID, 
                Title, 
                About, 
                Gender, 
                Ethnicity, 
                DisabilityStatus,
                Location,
                PhoneNumber) VALUES (?, ?, ?, ?, ?, ?, ?, ?);""", (
                    newProfile.ApplicantID,
                    newProfile.Title,
                    newProfile.About,
                    newProfile.Gender,
                    newProfile.Ethnicity,
                    newProfile.DisabilityStatus,
                    newProfile.Location,
                    newProfile.PhoneNumber,
                ))
            
            # commit the query operation to the database
            DatabaseConnection.commit()

            # for safety, close the database connection
            DatabaseConnection.close()

            # return True as success confirmation
            return True

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::InsertNewProfile")

    
    # method to retrieve the row as ApplicantProfile object for a user
    def RetrieveProfile(loggedUser: ApplicantUser) -> ApplicantProfile:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            # first fetch the ID of the logged user
            try:
                ID: str = ApplicantUserDBActions.ReturnIDUser(loggedUser.Username)
            except Exception as e:
                MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::RetrieveProfile::ReturnIDUser")
            
            # now fetch the row
            # query
            DatabaseCursor.execute("""SELECT * FROM ApplicantProfile WHERE ApplicantID = ?;""", (ID,))
            # query results
            records = DatabaseCursor.fetchall()

            # for safety, close the database connection
            DatabaseConnection.close()

            if len(records) == 1:
                # keys for the columns of the ApplicantUser table
                keys: list() = ['pk', 'ApplicantID', 'Title', 'About', 'Gender', 'Ethnicity', 
                    'DisabilityStatus', 'Location', 'PhoneNumber']
                dictResult: dict() = QueryHelper.ConvertTupleToDict(query=records, dictKeys=keys)[0]

                return ApplicantProfile(
                    ApplicantID=dictResult['ApplicantID'],
                    Title=dictResult['Title'],
                    About=dictResult['About'],
                    Gender=dictResult['Gender'],
                    Ethnicity=dictResult['Ethnicity'],
                    DisabilityStatus=dictResult['DisabilityStatus'],
                    Location=dictResult['Location'],
                    PhoneNumber=dictResult['PhoneNumber']
                )
            elif len(records) == 0:
                print("\nError! You have not yet created a profile. Please select to update your profile to create one.\n")
                return None
            else:
                raise Exception("\nError! There are applicant profiles with duplicate ApplicantID's.")


        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::RetrieveProfile")

    
    # method to update profile of an applicant user
    def UpdateProfile(newProfile: ApplicantProfile) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            DatabaseCursor.execute("""UPDATE ApplicantProfile SET Title = ?, About = ?, Gender = ?, 
                Ethnicity = ?, DisabilityStatus = ?, Location = ?, PhoneNumber = ? WHERE ApplicantID = ?;""", 
                (newProfile.Title, newProfile.About, newProfile.Gender, newProfile.Ethnicity, newProfile.DisabilityStatus,
                    newProfile.Location, newProfile.PhoneNumber, newProfile.ApplicantID,)
            )

            # commit the query operation to the database
            DatabaseConnection.commit()

            # for safety, close the database connection
            DatabaseConnection.close()

            # return True as success confirmation
            return True
            
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::UpdateProfile")