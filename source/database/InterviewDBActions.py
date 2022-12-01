import sqlite3
from database.ApplicantUserDBActions import ApplicantUserDBActions
from database.CompanyUserDBActions import CompanyUserDBActions
from helpers.MenuHelper import MenuHelper
from database.SQLiteDBSetUp import DatabaseSetUp
from model.Interview.Interview import Interview
from database.QueryHelpers.QueryHelper import QueryHelper


# class for DB actions on the Interview table
class InterviewDBActions:

    # method to check if the company user has already scheduled an interview with the given applicant user
    def InterviewAlreadyCreated(companyUsername: str, applicantUsername: str) -> bool:
        try:
            DatabaseSetUp.CreateInterviewTable()


            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            # first try to get the ID of the applicant user
            try:
                applicantId: str = ApplicantUserDBActions.ReturnIDUser(username=applicantUsername)
            except:
                raise Exception("\nFailure! Retrieve of applicant ID from applicant username failed.\n")

            # now try to get the ID of the company user
            try:
                companyId: str = CompanyUserDBActions.ReturnIDUser(username=applicantUsername)
            except:
                raise Exception("\nFailure! Retrieve of company ID from company username failed.\n")

            # query
            DatabaseCursor.execute("""SELECT * FROM Interview WHERE ApplicantID = ? AND CompanyID = ?;""", (applicantId, companyId,))

            if len(DatabaseCursor.fetchall()) == 0:
                # for safety, close the database connection
                DatabaseConnection.close()
                return False
            else:
                # for safety, close the database connection
                DatabaseConnection.close()
                return True

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="InterviewDBActions::InterviewAlreadyCreated")


    # method to insert a new row into the Interview table
    def InsertNewInterview(newInterview: Interview) -> bool:
        try:
            # database connection object to the JobsBoard database
            DatabaseConnection = sqlite3.connect('JobsBoardDB.db')
            # database cursor object to manipulate SQL queries
            DatabaseCursor = DatabaseConnection.cursor()

            # query
            # insert a new job posting row into the table
            # the value for the column "DateLogin" is skipped so its default value becomes Null
            DatabaseCursor.execute("""INSERT INTO Interview (
                ID,
                CompanyID,
                ApplicantID,
                Location,
                MeetingTime
                ) VALUES (?, ?, ?, ?, ?);""", (
                    newInterview.ID,
                    newInterview.CompanyID,
                    newInterview.ApplicantID,
                    newInterview.Location,
                    newInterview.MeetingTime
                )
            )
            
            # commit the query operation to the database
            DatabaseConnection.commit()

            # for safety, close the database connection
            DatabaseConnection.close()

            # return True as success confirmation
            return True

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="InterviewDBActions::InsertInterview")

    
    # method to return all the interviews of an applicant user
    def ReturnInterviewsApplicantUser(applicantUsername: str) -> list[Interview   ]:
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
            DatabaseCursor.execute("""SELECT * FROM Interview WHERE ApplicantID = ?;""", (applicantId,))
            # query results
            records = DatabaseCursor.fetchall()

            # for safety, close the database connection
            DatabaseConnection.close()

            if len(records) != 0:
                # keys for the columns of the Intrview table
                keys: list() = ['pk', 'ID', 'CompanyID', 'ApplicantID', 'Location', 'MeetingTime']
                convertResult: list[dict()] = QueryHelper.ConvertTupleToDict(query=records, dictKeys=keys)
                
                output: list[Interview] = []
                for dictItem in convertResult:
                    output.append(
                        Interview(
                            CompanyID=dictItem['CompanyID'],
                            ApplicantID=dictItem['ApplicantID'],
                            Location=dictItem['Location'],
                            MeetingTime=dictItem['MeetingTime']
                        )
                    )
                
                return output
            else:
                return []
        
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="InterviewDBActions::ReturnInterviewsApplicantUser")
            return False