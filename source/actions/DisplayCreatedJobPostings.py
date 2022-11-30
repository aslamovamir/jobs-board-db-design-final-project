from model.Company.CompanyUser import CompanyUser
from model.JobPosting.JobPosting import JobPosting
from database.JobPostingDBActions import JobPostingDBActions
from helpers.MenuHelper import MenuHelper


# class for diplay of created job postings
class DisplayCreatedJobPostings:

    def DisplayAllJobsCompanyUser(loggedUser: CompanyUser):
        
        # let's get retrieve all the job postings of the user from the database
        try:
            jobPostingsQuery: list[JobPosting] = JobPostingDBActions.ReturnJobPostingsCompanyUser(companyUsername=loggedUser.Username)
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="DisplayCreatedJobPostings::DisplayAllJobsCompanyUser")
        
        # now list by position name
        print("PRINING ALL POSTINGS!")
        for job in jobPostingsQuery:
            print(job.PositionName)