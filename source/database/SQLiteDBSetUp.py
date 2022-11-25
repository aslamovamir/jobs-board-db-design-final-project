import sqlite3
from dataclasses import dataclass


# NOTE: 
# Methods of this class must be run only once: they are run when running the app for
# the first time internally by developers to set up the database and the neceassary tables 

# class for the database set-up
@dataclass
class DatabaseSetUp:

    # method to create an SQL table for the ApplicantUser entity
    def CreateApplicantUserTable() -> bool:
        
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = sqlite3.Cursor()

            # query to create a new table for the Applicant User
            DatabaseCursor.execute("""
                CREATE TABLE ApplicantUser (
                    pk INTEGER PRIMARY KEY,
                    ID TEXT,
                    Username VARCHAR(50),
                    Email VARCHAR(50),
                    FirstName VARCHAR(50),
                    LastName VARCHAR(50),
                    DateRegistered TIMESTAMP,
                    DateLastLogin TIMESTAMP
                );
            """
            )

            # commit the query operation to the database
            DatabaseConnection.commit()

            # for safety, close the database connection
            DatabaseConnection.close()

            # return True as success confirmation
            return True

        except Exception as e:
            print("\nFailure! Creation of the Applicant Table in the database failed for some reason.",
                f"\nPlease address the following exception: {e}\n")
            return False



    # method to create an SQL table for the ApplicantProfile entity
    def CreateApplicantProfileTable() -> bool:
        pass

    # method to create an SQL table for the CompanyUser entity
    def CreateCompanyUserTable() -> bool:
        pass

    # method to create an SQL table for the CompanyProfile entity
    def CreateCompanyProfileTable() -> bool:
        pass




DatabaseSetUp.CreateApplicantUserTable()

