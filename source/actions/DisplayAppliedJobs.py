from model.Applicant.ApplicantUser import ApplicantUser
from model.Company.CompanyUser import CompanyUser
from model.JobPosting.AppliedJobPosting import AppliedJob
from database.AppliedJobDBActions import AppliedJobDBActions
from database.CompanyUserDBActions import CompanyUserDBActions
from helpers.MenuHelper import MenuHelper


# class to display all applied jobs
class DisplayAppliedJobs:

    def DisplayAppliedJobsApplicantUser(loggedUser: ApplicantUser):
        # let's retrieve all the applied jobs of the user from the database
        try:
            appliedJobs: list[AppliedJob] = AppliedJobDBActions.ReturnAppliedJobsApplicantUser(applicantUsername=loggedUser.Username)
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="DisplayAppliedJobs::DisplayAppliedJobsApplicantUser")

        # now display all applied jobs with details
        index: int = 1
        for i in range(len(appliedJobs)):
            print(f"\n\n{index}.")
            print("Position Name: ", AppliedJobDBActions.ReturnPositionNameAppliedJob(jobPostingID=appliedJobs[i].JobPostingID))
            print("Company Name: ", AppliedJobDBActions.ReturnCompanyNameAppliedJob(jobPostingID=appliedJobs[i].CompanyID))
            print("Status: ", appliedJobs[i].Status)
            print("Start Date: ", appliedJobs[i].StartDate)
            print("Good Fit Explanation: ", appliedJobs[i].GoodFitExplanation)
            print("Date Applied: ", appliedJobs[i].DateApplied)