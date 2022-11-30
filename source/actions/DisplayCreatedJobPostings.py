from model.Company.CompanyUser import CompanyUser
from model.JobPosting.JobPosting import JobPosting
from database.JobPostingDBActions import JobPostingDBActions
from helpers.MenuHelper import MenuHelper


# class for diplay of created job postings
class DisplayCreatedJobPostings:

    # helper method to return the poition names of job postings as menu options
    def HelpReturnPositionNamesOptions(jobs: list[JobPosting]) -> list[str]:
        try:
            options: list[str] = []
            for i in range(len(jobs)):
                options.append(jobs[i].PositionName)
            return options
        except Exception as e:
            MenuHelper.DisplayErrorException("DisplayCreatedJobPostings::HelpReturnPositionNamesOptions")


    # helper method to display all the information about a job posting
    def HelpDisplayDetailJobPosting(job: JobPosting):
        try:
            MenuHelper.DefineSectionBreak()
            print("Here is the information about the selected job:\n")
            print("Position Name: ", job.PositionName)
            print("Pay: ", job.Pay)
            print("Location: ", job.Location)
            print("Description: ", job.Description)
            print("Department: ", job.Department)
            MenuHelper.DefineSectionBreak()
        except Exception as e:
            MenuHelper.DisplayErrorException("DisplayCreatedJobPostings::HelpDisplayDetailJobPosting")


    # method to display all job postings created by the company user
    def DisplayAllJobsCompanyUser(loggedUser: CompanyUser):
        
        # let's retrieve all the job postings of the user from the database
        try:
            jobPostings: list[JobPosting] = JobPostingDBActions.ReturnJobPostingsCompanyUser(companyUsername=loggedUser.Username)
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="DisplayCreatedJobPostings::DisplayAllJobsCompanyUser")
        
        # now list all jobs by position name as menu options
        options: list[str] = DisplayCreatedJobPostings.HelpReturnPositionNamesOptions(jobs=jobPostings)
        while True:
            try:
                MenuHelper.RequestInput()
                MenuHelper.DisplayMenuOptions(options=options)

                # take in the menu option entered
                decision: int = MenuHelper.InputStream()
                if decision == "-1":
                    MenuHelper.InformMenuQuit()
                    break
                
                decision = int(decision)
                if decision in range(1, len(jobPostings)+1):
                    MenuHelper.DisplaySelectedOption(selectedOption=options[decision-1])
                    # now display all the information about this job
                    DisplayCreatedJobPostings.HelpDisplayDetailJobPosting(job=jobPostings[decision-1])
                else:
                    MenuHelper.WarnInvalidInput()
            except:
                MenuHelper.WarnInvalidInput()