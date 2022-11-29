import sqlite3
# from model.Company.CompanyUser import CompanyUser
from model.JobPosting.JobPosting import JobPosting
from helpers.MenuHelper import MenuHelper
from database.SQLiteDBSetUp import DatabaseSetUp


# class for JobPostingDBActions
class JobPostingDBActions:

    def InsertNewJobPosting(newJobPosting: JobPosting) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            DatabaseCursor.execute("DROP TABLE JobPosting;")
            DatabaseConnection.commit()
            DatabaseSetUp.CreateJobPostingTable()

            # query
            # insert a new job posting row into the table
            # the value for the column "DateLogin" is skipped so its default value becomes Null
            DatabaseCursor.execute("""INSERT INTO JobPosting (
                ID,
                CompanyID,
                PositionName,
                Pay,
                Location,
                Description,
                Department
                ) VALUES (?, ?, ?, ?, ?, ?);""", (
                    newJobPosting.ID,
                    newJobPosting.CompanyID,
                    newJobPosting.PositionName,
                    newJobPosting.Pay,
                    newJobPosting.Location,
                    newJobPosting.Description,
                    newJobPosting.Department
                )
            )
            
            # commit the query operation to the database
            DatabaseConnection.commit()

            # for safety, close the database connection
            DatabaseConnection.close()

            # return True as success confirmation
            return True

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="JobPostingDBActions::InsertNewJobPosting")
