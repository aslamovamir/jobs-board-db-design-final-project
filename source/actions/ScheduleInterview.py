from helpers.MenuHelper import MenuHelper
from database.InterviewDBActions import InterviewDBActions
from database.CompanyUserDBActions import CompanyUserDBActions
from database.ApplicantUserDBActions import ApplicantUserDBActions
from model.Interview.Interview import Interview


# function to schedule an interview between a company user and an applicant user
def ScheduleInterview(companyUsername: str, applicantUsername: str) -> bool:
    
    # first check if the company user has already scheduled an interview with this applicant user
    try:
        if InterviewDBActions.InterviewAlreadyCreated(companyUsername=companyUsername, applicantUsername=applicantUsername):
            print("\nError! An interview has already been scheduled with this applicant.")
            return False
    except Exception as e:
        MenuHelper.DisplayErrorException(exception=e, errorSource="ScheduleInterview::")

    MenuHelper.DefineSectionBreak()
    terminateOperation: bool = False
    try:
        # location
        while True:
            try:
                print("\nPlease enter location")
                input: str = MenuHelper.InputStream()
                if input == "-1":
                    terminateOperation = True
                    break
                if MenuHelper.ValidateEmptyInput(input=input):
                    MenuHelper.WarnInvalidInput()
                    continue
                location: str = input
                break
            except:
                MenuHelper.WarnInvalidInput()
        if terminateOperation:
            return True

        # meeting time
        while True:
            try:
                print("\nPlease enter meeting time")
                input: str = MenuHelper.InputStream()
                if input == "-1":
                    terminateOperation = True
                    break
                if MenuHelper.ValidateEmptyInput(input=input):
                    MenuHelper.WarnInvalidInput()
                    continue
                meetingTime: str = input
                break
            except:
                MenuHelper.WarnInvalidInput()
        if terminateOperation:
            return True

        # create an interview object with the given parameters
        newInterview: Interview = Interview(
            CompanyID=CompanyUserDBActions.ReturnIDUser(username=companyUsername),
            ApplicantID=ApplicantUserDBActions.ReturnIDUser(username=applicantUsername),
            Location=location,
            MeetingTime=meetingTime
        )

        while True:
            try:
                print("\nThis is a new interview to be scheduled:")
                print("Company Username: ", companyUsername)
                print("Applicant Username: ", applicantUsername)
                print("Location: ", location)
                print("Meeting Time: ", meetingTime)

                # ask for creation confirmation
                if MenuHelper.ConfirmChanges():
                    # now try to insert the new job posting object into the database
                    try:
                        if InterviewDBActions.InsertNewInterview(newInterview=newInterview):
                            MenuHelper.InformSuccessOperation()
                            return True
                        else:
                            MenuHelper.InformFailureOperation()
                            return False
                    except Exception as e:
                        MenuHelper.DisplayErrorException(exception=e, errorSource="ScheduleInterview::InsertNewInterview")
                else:
                    MenuHelper.InformMenuQuit()
                    return True
            except:
                MenuHelper.WarnInvalidInput()
    
    except Exception as e:
        MenuHelper.DisplayErrorException(exception=e, errorSource="ScheduleInterview")