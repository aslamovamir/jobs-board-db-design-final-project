from database.InterviewDBActions import InterviewDBActions
from model.Interview.Interview import Interview
from helpers.MenuHelper import MenuHelper


# class for the display of all scheduled interview of an applicant user
class DisplayInterviews:

    # method to display all interviews
    def DisplayAllInterviews(loggedUsername: str):
        # let's retrieve all the applied jobs of the user from the database
        try:
            appliedJobs: list[Interview] = InterviewDBActions.ReturnInterviewsApplicantUser(applicantUsername=loggedUsername)
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="DisplayAppliedJobs::DisplayAppliedJobsApplicantUser")

        if len(appliedJobs) == 0:
            print("\nError! You don't have any scheduled interview yet.")
            return

        # now display all scheduled jobs with details
        index: int = 1
        for i in range(len(appliedJobs)):
            print(f"\n\n{index}.")
            print("Position Name: ", AppliedJobDBActions.ReturnPositionNameAppliedJob(jobPostingID=appliedJobs[i].JobPostingID))
            print("Company Name: ", AppliedJobDBActions.ReturnCompanyNameAppliedJob(jobPostingID=appliedJobs[i].CompanyID))
            print("Status: ", appliedJobs[i].Status)
            print("Start Date: ", appliedJobs[i].StartDate)
            print("Good Fit Explanation: ", appliedJobs[i].GoodFitExplanation)
            print("Date Applied: ", appliedJobs[i].DateApplied)
            index += 1