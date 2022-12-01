import sqlite3
from helpers.MenuHelper import MenuHelper


# NOTE: 
# Methods of this class must be run only once: they are run when running the app for
# the first time internally by developers to set up the database and the neceassary tables 

# class for the database set-up
class DatabaseSetUp:

    # method to create an SQL table for the ApplicantUser entity
    def CreateApplicantUserTable() -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

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
            MenuHelper.DisplayErrorException(exception=e, errorSource="SQLiteDBSetUp::DatabaseSetUp::CreateApplicantUserTable")
            return False


    # method to create an SQL table for the ApplicantProfile entity
    def CreateApplicantProfileTable() -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            # query to create a new table for the ApplicantProfile
            DatabaseCursor.execute("""
                CREATE TABLE ApplicantProfile (
                    pk INTEGER PRIMARY KEY,
                    ApplicantID TEXT,
                    Title TEXT,
                    About TEXT,
                    Gender VARCHAR(50),
                    Ethnicity VARCHAR(50),
                    DisabilityStatus TEXT,
                    Location TEXT,
                    PhoneNumber VARCHAR(50),
                    FOREIGN KEY(ApplicantID) REFERENCES ApplicantUser(ID)
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
            MenuHelper.DisplayErrorException(exception=e, errorSource="SQLiteDBSetUp::DatabaseSetUp::CreateApplicantProfileTable")
            return False


    # method to create an SQL table for the CompanyUser entity
    def CreateCompanyUserTable() -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            # query to create a new table for the Applicant User
            DatabaseCursor.execute("""
                CREATE TABLE CompanyUser (
                    pk INTEGER PRIMARY KEY,
                    ID TEXT,
                    Username VARCHAR(50),
                    CompanyName VARCHAR(50),
                    Email VARCHAR(50),
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
            MenuHelper.DisplayErrorException(exception=e, errorSource="SQLiteDBSetUp::DatabaseSetUp::CreateCompanyUserTable")
            return False


    # method to create an SQL table for the CompanyProfile entity
    def CreateCompanyProfileTable() -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            # query to create a new table for the Company Profile
            DatabaseCursor.execute("""
                CREATE TABLE CompanyProfile (
                    pk INTEGER PRIMARY KEY,
                    CompanyID TEXT,
                    About TEXT,
                    Location TEXT,
                    Industry TEXT,
                    ServiceType VARCHAR(50),
                    CompanyType VARCHAR(50),
                    AnnualRevenue TEXT,
                    EmployeeSize TEXT,
                    FoundationDate TEXT,
                    InternationalHires VARCHAR(50),
                    FOREIGN KEY(CompanyID) REFERENCES CompanyUser(ID)
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
            MenuHelper.DisplayErrorException(exception=e, errorSource="SQLiteDBSetUp::DatabaseSetUp::CreateCompanyProfileTable")
            return False

    
    # method to create an SQL table for the JobPosting entity
    def CreateJobPostingTable() -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            # query to create a new table for the Company Profile
            DatabaseCursor.execute("""
                CREATE TABLE JobPosting (
                    pk INTEGER PRIMARY KEY,
                    ID TEXT,
                    CompanyID TEXT,
                    PositionName VARCHAR(50),
                    Pay VARCHAR(50),
                    Location TEXT,
                    Description TEXT,
                    Department VARCHAR(50),
                    FOREIGN KEY(CompanyID) REFERENCES CompanyUser(ID)
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
            MenuHelper.DisplayErrorException(exception=e, errorSource="SQLiteDBSetUp::DatabaseSetUp::CreateJobPostingTable")
            return False

    
    # method to create an SQL table for the AppliedJob entity
    def CreateAppliedJobTable() -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            # query to create a new table for the Company Profile
            DatabaseCursor.execute("""
                CREATE TABLE AppliedJob (
                    pk INTEGER PRIMARY KEY,
                    ID TEXT,
                    JobPostingID TEXT,
                    CompanyID TEXT,
                    ApplicantID TEXT,
                    Status VARCHAR(50),
                    DateApplied TIMESTAMP,
                    StartDate VARCHAR(50),
                    GoodFitExplanation TEXT,
                    SponsorshipRequirement TEXT,
                    FOREIGN KEY(JobPostingID) REFERENCES JobPosting(ID),
                    FOREIGN KEY(CompanyID) REFERENCES CompanyUser(ID),
                    FOREIGN KEY(ApplicantID) REFERENCES ApplicantUser(ID)
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
            MenuHelper.DisplayErrorException(exception=e, errorSource="SQLiteDBSetUp::DatabaseSetUp::CreateJobPostingTable")
            return False


    # method to create an SQL table for the Interview entity
    def CreateInterviewTable() -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            DatabaseCursor.execute("""DROP TABLE Interview;""")
            DatabaseConnection.commit()

            # query to create a new table for the Company Profile
            DatabaseCursor.execute("""
                CREATE TABLE Interview (
                    pk INTEGER PRIMARY KEY,
                    ID TEXT,
                    CompanyID TEXT,
                    ApplicantID TEXT,
                    JobPostingID TEXT,
                    Location TEXT,
                    MeetingTime TEXT,
                    FOREIGN KEY(CompanyID) REFERENCES CompanyUser(ID),
                    FOREIGN KEY(ApplicantID) REFERENCES ApplicantUser(ID)
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
            MenuHelper.DisplayErrorException(exception=e, errorSource="SQLiteDBSetUp::DatabaseSetUp::CreateJobPostingTable")
            return False