import sqlite3
from database.ApplicantUserDBActions import ApplicantUserDBActions
from database.SQLiteDBSetUp import DatabaseSetUp
from helpers.MenuHelper import MenuHelper
from model.JobPosting.AppliedJobPosting import AppliedJob
from database.QueryHelpers.QueryHelper import QueryHelper


# class for Applied Job DB actions
class AppliedJobDBActions:

    # method to check if the applicant user already applied for the job posting
    def AppliedJobAlreadyCreated(applicantUsername: str, jobPostingID: str) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            try:
                applicantId: str = ApplicantUserDBActions.ReturnIDUser(username=applicantUsername)
            except:
                raise Exception("\nFailure! Retrieve of company ID from company username failed.\n")

            # query
            DatabaseCursor.execute("""SELECT * FROM AppliedJob WHERE ApplicantID = ? AND JobPostingID = ?;""", (applicantId, jobPostingID,))

            if len(DatabaseCursor.fetchall()) == 0:
                # for safety, close the database connection
                DatabaseConnection.close()
                return False
            else:
                # for safety, close the database connection
                DatabaseConnection.close()
                return True

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="AppliedJobDBActions::AppliedJobAlreadyCreated")


    # method to insert a new row into the AppliedJob table
    def InsertNewAppliedJob(newAppliedJob: AppliedJob) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            # query
            # insert a new job posting row into the table
            # the value for the column "DateLogin" is skipped so its default value becomes Null
            DatabaseCursor.execute("""INSERT INTO AppliedJob (
                ID,
                JobPostingID,
                CompanyID,
                ApplicantID,
                Status,
                StartDate,
                GoodFitExplanation,
                SponsorshipRequirement,
                DateApplied
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP);""", (
                    newAppliedJob.ID,
                    newAppliedJob.JobPostingID,
                    newAppliedJob.CompanyID,
                    newAppliedJob.ApplicantID,
                    newAppliedJob.Status,
                    newAppliedJob.StartDate,
                    newAppliedJob.GoodFitExplanation,
                    newAppliedJob.SponsorshipRequirement
                )
            )
            
            # commit the query operation to the database
            DatabaseConnection.commit()

            # for safety, close the database connection
            DatabaseConnection.close()

            # return True as success confirmation
            return True

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="AppliedJobDBActions::InsertNewAppliedJob")


    # method to return all the applied jobs of an applicant user
    def ReturnAppliedJobsApplicantUser(applicantUsername: str) -> list[AppliedJob]:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            try:
                applicantId: str = ApplicantUserDBActions.ReturnIDUser(username=applicantUsername)
            except:
                raise Exception("\nFailure! Retrieve of company ID from company username failed.\n")

            # query
            DatabaseCursor.execute("""SELECT * FROM AppliedJob WHERE ApplicantID = ?;""", (applicantId,))
            # query results
            records = DatabaseCursor.fetchall()

            # for safety, close the database connection
            DatabaseConnection.close()

            if len(records) != 0:
                # keys for the columns of the JobPosting table
                keys: list() = ['pk', 'ID', 'JobPostingID', 'CompanyID', 'ApplicantID', 'Status', 'DateApplied', 'StartDate', 
                    'GoodFitExplanation', 'SponsorshipRequirement']
                convertResult: list[dict()] = QueryHelper.ConvertTupleToDict(query=records, dictKeys=keys)
                
                output: list[AppliedJob] = []
                for dictItem in convertResult:
                    output.append(
                        AppliedJob(
                            JobPostingID=dictItem['JobPostingID'],
                            CompanyID=dictItem['CompanyID'],
                            ApplicantID=dictItem['ApplicantID'],
                            Status=dictItem['Status'],
                            StartDate=dictItem['StartDate'],
                            GoodFitExplanation=dictItem['GoodFitExplanation'],
                            SponsorshipRequirement=dictItem['SponsorshipRequirement'],
                            DateApplied=dictItem['DateApplied']
                        )
                    )
                return output
            else:
                return []
        
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="AppliedJobDBActions::ReturnAppliedJobsApplicantUser")
            return False

    
    # method to retrieve the position name of an applied job
    def ReturnPositionNameAppliedJob(jobPostingID: str) -> str:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()
            # query
            DatabaseCursor.execute("""SELECT PositionName FROM JobPosting WHERE ID = ?""", (jobPostingID,))
            queryResult = DatabaseCursor.fetchall()

            # for safety, close the database connection
            DatabaseConnection.close()

            if len(queryResult) == 1:
                return queryResult[0][0]
            else:
                return None
        
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="AppliedJobDBActions::ReturnPositionNameAppliedJob")
            return False
    

    # method to retrieve the company name of an applied job
    def ReturnCompanyNameAppliedJob(jobPostingID: str) -> str:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()
            # query
            DatabaseCursor.execute("""SELECT CompanyName FROM CompanyUser WHERE ID = ?""", (jobPostingID,))
            queryResult = DatabaseCursor.fetchall()

            # for safety, close the database connection
            DatabaseConnection.close()

            if len(queryResult) == 1:
                return queryResult[0][0]
            else:
                return None
        
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="AppliedJobDBActions::ReturnPositionNameAppliedJob")
            return False