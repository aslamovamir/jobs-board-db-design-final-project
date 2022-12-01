from database.InterviewDBActions import InterviewDBActions
from model.Interview.Interview import Interview
from helpers.MenuHelper import MenuHelper
from database.AppliedJobDBActions import AppliedJobDBActions


# class for the display of all scheduled interview of an applicant user
class DisplayInterviews:

    # method to display all interviews
    def DisplayAllInterviews(loggedUsername: str):
        # let's retrieve all the applied jobs of the user from the database
        try:
            scheduledInterviews: list[Interview] = InterviewDBActions.ReturnInterviewsApplicantUser(applicantUsername=loggedUsername)
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="DisplayAppliedJobs::DisplayAppliedJobsApplicantUser")

        if len(scheduledInterviews) == 0:
            print("\nError! You don't have any scheduled interview yet.")
            return

        # now display all scheduled jobs with details
        index: int = 1
        for i in range(len(scheduledInterviews)):
            print(f"\n\n{index}.")
            print("Position Name: ", AppliedJobDBActions.ReturnPositionNameAppliedJob(jobPostingID=scheduledInterviews[i].JobPostingID))
            print("Company Name: ", AppliedJobDBActions.ReturnCompanyNameAppliedJob(jobPostingID=scheduledInterviews[i].JobPostingID))
            print("Location: ", scheduledInterviews[i].Location)
            print("Meeting Time: ", scheduledInterviews[i].MeetingTime)
            index += 1