import sqlite3
from model.JobPosting.JobPosting import JobPosting
from helpers.MenuHelper import MenuHelper
from database.QueryHelpers.QueryHelper import QueryHelper
from database.CompanyUserDBActions import CompanyUserDBActions


# class for JobPostingDBActions
class JobPostingDBActions:

    # method to check if the company already created a job with the same position name
    def JobAlreadyCreated(companyUsername: str, positionName: str) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            try:
                companyId: str = CompanyUserDBActions.ReturnIDUser(username=companyUsername)
            except:
                raise Exception("\nFailure! Retrieve of company ID from company username failed.\n")

            # query
            DatabaseCursor.execute("""SELECT * FROM JobPosting WHERE CompanyID = ? AND PositionName = ?;""", (companyId, positionName,))

            if len(DatabaseCursor.fetchall()) == 0:
                # for safety, close the database connection
                DatabaseConnection.close()
                return False
            else:
                # for safety, close the database connection
                DatabaseConnection.close()
                return True

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="JobPostingDBActions::JobAlreadyCreated")


    # method to insert a new row into the JobPosting table
    def InsertNewJobPosting(newJobPosting: JobPosting) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

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
                ) VALUES (?, ?, ?, ?, ?, ?, ?);""", (
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

    
    # method to return all the job postings of a company user
    def ReturnJobPostingsCompanyUser(companyUsername: str) -> list[JobPosting]:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            try:
                companyId: str = CompanyUserDBActions.ReturnIDUser(username=companyUsername)
            except:
                raise Exception("\nFailure! Retrieve of company ID from company username failed.\n")

            # query
            DatabaseCursor.execute("""SELECT * FROM JobPosting WHERE CompanyID = ?;""", (companyId,))
            # query results
            records = DatabaseCursor.fetchall()

            # for safety, close the database connection
            DatabaseConnection.close()

            if len(records) != 0:
                # keys for the columns of the JobPosting table
                keys: list() = ['pk', 'ID', 'CompanyID', 'PositionName', 'Pay', 'Location', 'Description', 'Department']
                convertResult: list[dict()] = QueryHelper.ConvertTupleToDict(query=records, dictKeys=keys)
                
                output: list[JobPosting] = []
                for dictItem in convertResult:
                    output.append(
                        JobPosting(
                            CompanyID=dictItem['CompanyID'],
                            PositionName=dictItem['PositionName'],
                            Pay=dictItem['Pay'],
                            Location=dictItem['Location'],
                            Description=dictItem['Description'],
                            Department=dictItem['Department']
                        )
                    )
                
                return output
            else:
                return None
        
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::ReturnApplicantUser")
            return False

    
    # method to return all job postings currently stored in the database
    def ReturnAllJobPostings() -> list[JobPosting]:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            # query
            DatabaseCursor.execute("SELECT * FROM JobPosting;")
            # query results
            records = DatabaseCursor.fetchall()

            # for safety, close the database connection
            DatabaseConnection.close()

            if len(records) != 0:
                # keys for the columns of the JobPosting table
                keys: list() = ['pk', 'ID', 'CompanyID', 'PositionName', 'Pay', 'Location', 'Description', 'Department']
                convertResult: list[dict()] = QueryHelper.ConvertTupleToDict(query=records, dictKeys=keys)
                
                output: list[JobPosting] = []
                for dictItem in convertResult:
                    output.append(
                        JobPosting(
                            CompanyID=dictItem['CompanyID'],
                            PositionName=dictItem['PositionName'],
                            Pay=dictItem['Pay'],
                            Location=dictItem['Location'],
                            Description=dictItem['Description'],
                            Department=dictItem['Department']
                        )
                    )
                
                return output
            else:
                return None
        
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplicantUserDBActions::ReturnApplicantUser")
            return False