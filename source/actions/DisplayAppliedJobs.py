from model.Applicant.ApplicantUser import ApplicantUser
from model.JobPosting.JobPosting import JobPosting
from model.JobPosting.AppliedJobPosting import AppliedJob
from model.Company.CompanyProfile import CompanyProfile
from database.AppliedJobDBActions import AppliedJobDBActions
from database.CompanyUserDBActions import CompanyUserDBActions
from database.JobPostingDBActions import JobPostingDBActions
from helpers.MenuHelper import MenuHelper
from actions.DisplayProfileInfo import DisplayProfileInfo
from actions.DisplayCreatedJobPostings import DisplayCreatedJobPostings


# class to display all applied jobs
class DisplayAppliedJobs:

    # method to display all applied jobs of an applicant user
    def DisplayAppliedJobsApplicantUser(loggedUser: ApplicantUser):
        # let's retrieve all the applied jobs of the user from the database
        try:
            appliedJobs: list[AppliedJob] = AppliedJobDBActions.ReturnAppliedJobsApplicantUser(applicantUsername=loggedUser.Username)
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="DisplayAppliedJobs::DisplayAppliedJobsApplicantUser")

        if len(appliedJobs) == 0:
            print("\nError! You have not applied for any job yet.")
            return

        # now display all applied jobs with details
        MenuHelper.DefineSectionBreak()
        index: int = 1
        for i in range(len(appliedJobs)):
            print(f"\n\n{index}.")
            print("Position Name: ", AppliedJobDBActions.ReturnPositionNameAppliedJob(jobPostingID=appliedJobs[i].JobPostingID))
            print("Company Name: ", AppliedJobDBActions.ReturnCompanyNameAppliedJob(companyID=appliedJobs[i].CompanyID))
            print("Status: ", appliedJobs[i].Status)
            print("Start Date: ", appliedJobs[i].StartDate)
            print("Good Fit Explanation: ", appliedJobs[i].GoodFitExplanation)
            print("Date Applied: ", appliedJobs[i].DateApplied)
            index += 1
        MenuHelper.DefineSectionBreak()
        while True:
            try:
                print("\nWould you like more information about the poster company or job posting? (Y/N) ")
                input = MenuHelper.InputStream()
                if input == "-1":
                    MenuHelper.InformMenuQuit()
                    return
                elif input == "Y":
                    while True:
                        try:
                            print("\nPlease indicate the index of the applied job")
                            input: str = MenuHelper.InputStream()
                            if input == "-1":
                                break

                            index: int = int(input)
                            if index in range(1, len(appliedJobs) + 1):
                                companyProfile: CompanyProfile = CompanyUserDBActions.RetrieveProfileWithID(appliedJobs[index-1].CompanyID)
                                jobPosting: JobPosting = JobPostingDBActions.ReturnJobPostingWithID(ID=appliedJobs[index-1].JobPostingID)

                                # now print the profile and job details
                                DisplayProfileInfo.DisplayCompanyProfileProvided(profile=companyProfile)
                                DisplayCreatedJobPostings.HelpDisplayDetailJobPosting(job=jobPosting)
                            else:
                                MenuHelper.WarnInvalidInput()
                        except:
                            MenuHelper.WarnInvalidInput()
                elif input == "N":
                    break
                else:
                    MenuHelper.WarnInvalidInput()
            except:
                MenuHelper.WarnInvalidInput()