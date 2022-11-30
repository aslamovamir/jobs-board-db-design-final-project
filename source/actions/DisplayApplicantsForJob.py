from helpers.MenuHelper import MenuHelper
from model.JobPosting.AppliedJobPosting import AppliedJob
from database.AppliedJobDBActions import AppliedJobDBActions

# class for the action to display all appicants for a particular job
class DisplayApplicantsForJob:

    # method to show all applicants for a job
    def DisplayAllApplicantsForJob(loggedUsername: str, jobPostingID: str):
        # first let's get all applied jobs objects from the database using the job posting ID
        try:
            allAppliedJobsInstances: list[AppliedJob] = AppliedJobDBActions.ReturnAppliedJobsByJobPostingID(jobPostingID=jobPostingID)
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="DisplayApplicantsForJob::DisplayAllApplicantsForJob")

        # if there are no applied job instances, inform the user and return
        if len(allAppliedJobsInstances) == 0:
            print("\nError! No applicant has applied for this job posting yet.")
            return

        # TODO: now get all the usernames and full names of the applicants
        