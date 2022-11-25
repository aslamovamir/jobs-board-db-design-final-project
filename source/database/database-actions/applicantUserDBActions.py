import sqlite3


# function to execute an SQL query to insert a new Applicant User row into the ApplicantUser table
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
                VALUES ('wdawd231daw1!r23r13r', 'amiraslamov', 'amiraslamov@usf.edu', 'Amir', 'Aslamov', CURRENT_TIMESTAMP);
            """
            )

    except Exception as e:
        print("\nFailure! Insertion of a new Applicant User row in the database failed for some reason.",
                f"\nPlease address the following exception: {e}\n")
        return False


# InsertNewApplicantUser({})
# c = sqlite3.connect('JobsBoardDB.db')
# cursor = c.cursor()

# cursor.execute("SELECT * FROM ApplicantUser;")
# print(type(cursor.fetchall()))
