import sqlite3
from QueryHelpers.QueryHelper import QueryHelper


# class for the ApplicantUserDBActions
class ApplicantUserDBActions:

    # method to execute an SQL query to insert a new Applicant User row into the ApplicantUser table
    def InsertNewApplicantUser(applicantUser: dict()) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            # insert a new user row into the table
            # the value for the column "DateLogin" is skipped so its default value becomes Null
            DatabaseCursor.execute("""
                INSERT INTO ApplicantUser (ID, Username, Email, FirstName, LastName, DateRegistered)
                    VALUES (:id, :username, :email, :first_name, :last_name, CURRENT_TIMESTAMP);
                """, 
                {
                    'id': applicantUser['ID'], 
                    'username': applicantUser['Username'], 
                    'email': applicantUser["Email"],
                    'first_name': applicantUser['FirstName'], 
                    'last_name': applicantUser['LastName'],
                }
            )
            
            # commit the query operation to the database
            DatabaseConnection.commit()

            # for safety, close the database connection
            DatabaseConnection.close()

            # return True as success confirmation
            return True


        except Exception as e:
            print("\nFailure! Insertion of a new Applicant User row in the database failed for some reason.",
                    f"\nPlease address the following exception: {e}\n")
            return False


    # method to query all Applicant User rows from the ApplicantUser table
    def QueryAllApplicantUserRows() -> list[dict()]:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            DatabaseCursor.execute("SELECT * FROM ApplicantUser;")
            
            # keys for the columns of the ApplicantUser table
            keys: list() = ['pk', 'ID', 'Username', 'Email', 'FirstName', 'LastName', 'DateRegistered', 'DateLastLogin']
            output: list() = []
            try:
                output = QueryHelper.ConvertTupleToDict(query=DatabaseCursor.fetchall(), dictKeys=keys)
            except Exception as e:
                print("\nFailure! Call of the ConvertTupleToDict method in QueryAllApplicantUserRows method failed for some reason.\n",
                    f"Please address the following exception: {e}\n")


            # commit the query operation to the database
            DatabaseConnection.commit()

            # for safety, close the database connection
            DatabaseConnection.close()

            # return True as success confirmation
            return output

        except Exception as e:
            print("\nFailure! Querying of all Applicant User rows in the database failed for some reason.",
                    f"\nPlease address the following exception: {e}\n")
            return False

# newUser = {
#     'Id': 'wadd21123!21#3#3443###',
#     'Username': 'testUsername',
#     'Email': 'testEmail',
#     'FirstName': 'TestFirstName',
#     'LastName': 'TestLastName',
# }

# ApplicantUserDBActions.InsertNewApplicantUser(applicantUser=newUser)
result = ApplicantUserDBActions.QueryAllApplicantUserRows()
for row in result:
    print(row)
