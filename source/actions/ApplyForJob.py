from model.Applicant.ApplicantUser import ApplicantUser
from model.JobPosting.JobPosting import JobPosting
from model.JobPosting.AppliedJobPosting import AppliedJob
from helpers.MenuHelper import MenuHelper
from database.ApplicantUserDBActions import ApplicantUserDBActions
from database.CompanyUserDBActions import CompanyUserDBActions
from database.JobPostingDBActions import JobPostingDBActions
from actions.DisplayCreatedJobPostings import DisplayCreatedJobPostings
from database.AppliedJobDBActions import AppliedJobDBActions


# class for ApplyForJob
class ApplyForJob:

    def ApplyEntree(loggedUser: ApplicantUser):
        # show all job postings currently in the database
        try:
            allJobs: list[JobPosting] = JobPostingDBActions.ReturnAllJobPostings()
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplyForJob::ApplyEntree")

        # now list all jobs by position name as menu options
        options: list[str] = DisplayCreatedJobPostings.HelpReturnPositionNamesOptions(jobs=allJobs)
        while True:
            try:
                MenuHelper.RequestInput()
                MenuHelper.DisplayMenuOptions(options=options)

                # take in the menu option entered
                decision: int = MenuHelper.InputStream()
                if decision == "-1":
                    MenuHelper.InformMenuQuit()
                    break
                
                jobSelectedIndex: int = int(decision)
                if jobSelectedIndex in range(1, len(allJobs)+1):
                    MenuHelper.DisplaySelectedOption(selectedOption=options[jobSelectedIndex-1])

                    # now check to see if the user has already applied for this job
                    if AppliedJobDBActions.AppliedJobAlreadyCreated(loggedUser.Username, jobPostingID=allJobs[jobSelectedIndex-1].ID):
                        print("\nError! You have already applied for this job posting. Please select a new one.")
                        continue

                    # now display all the information about this job
                    DisplayCreatedJobPostings.HelpDisplayDetailJobPosting(job=allJobs[jobSelectedIndex-1])
                    # now ask if they would like to apply for this job
                    decision: str = input("\nWould you like to apply for this job? Y/N: ")
                    if decision == "Y":
                        # call the method to apply for this job
                        try:
                            if ApplyForJob.ApplyForJob(loggedUser=loggedUser, jobPosting=allJobs[jobSelectedIndex-1]):
                                print("You have successfully applied for this job posting.")
                            else:
                                print("Application for this job failed.")
                        except Exception as e:
                            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplyForJob::ApplyEntree:ApplyForJob")
                else:
                    MenuHelper.WarnInvalidInput()
            except:
                MenuHelper.WarnInvalidInput()


    # method to apply for a job posting by an applicant user
    def ApplyForJob(loggedUser: ApplicantUser, jobPosting: JobPosting) -> bool:
        MenuHelper.DefineSectionBreak()
        terminateOperation: bool = False

        try:
            # start date
            while True:
                try:
                    print("\nPlease enter when can start working")
                    input: str = MenuHelper.InputStream()
                    if input == "-1":
                        terminateOperation = True
                        break
                    if MenuHelper.ValidateEmptyInput(input=input):
                        MenuHelper.WarnInvalidInput()
                        continue
                    startDate: str = input
                    break
                except:
                    MenuHelper.WarnInvalidInput()
            if terminateOperation:
                return True

            # good fit explanation
            while True:
                try:
                    print("\nPlease explain why you would be a good fit for this role")
                    input: str = MenuHelper.InputStream()
                    if input == "-1":
                        terminateOperation = True
                        break
                    if MenuHelper.ValidateEmptyInput(input=input):
                        MenuHelper.WarnInvalidInput()
                        continue
                    goodFitExplanation: str = input
                    break
                except:
                    MenuHelper.WarnInvalidInput()
            if terminateOperation:
                return True

            # sponsorship requirement
            while True:
                try:
                    print("\nPlease explain if you would require any work visa sponsorship")
                    input: str = MenuHelper.InputStream()
                    if input == "-1":
                        terminateOperation = True
                        break
                    if MenuHelper.ValidateEmptyInput(input=input):
                        MenuHelper.WarnInvalidInput()
                        continue
                    SponsorshipRequirement: str = input
                    break
                except:
                    MenuHelper.WarnInvalidInput()
            if terminateOperation:
                return True

            # now create a new applied job object with the input parameters
            newAppliedJob: AppliedJob = AppliedJob(
                JobPostingID=jobPosting.ID,
                CompanyID=jobPosting.CompanyID,
                ApplicantID=ApplicantUserDBActions.ReturnIDUser(username=loggedUser.Username),
                Status="Unreviewed",
                StartDate=startDate,
                GoodFitExplanation=goodFitExplanation,
                SponsorshipRequirement=SponsorshipRequirement,
                DateApplied=None
            )

            while True:
                try:
                    print("\nThis is an overview of your job application:")
                    print("Position Name: ", jobPosting.PositionName)
                    print("Company: ", CompanyUserDBActions.ReturnCompanyUser(id=jobPosting.CompanyID).CompanyName)
                    print("Good Fit Explanation: ", newAppliedJob.GoodFitExplanation)
                    print("Sponorship Requirement: ", newAppliedJob.SponsorshipRequirement)

                    # ask for creation confirmation
                    if MenuHelper.ConfirmChanges():
                        # now we attempt to push the applied job object to the database
                        try:
                            if AppliedJobDBActions.InsertNewAppliedJob(newAppliedJob=newAppliedJob):
                                MenuHelper.InformSuccessOperation()
                                return True
                            else:
                                MenuHelper.InformFailureOperation()
                                return False
                        except Exception as e:
                            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplyForJob::ApplyForJob::InsertNewAppliedJob")
                            return False
                    else:
                        break
                except:
                    MenuHelper.WarnInvalidInput()
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplyForJob::ApplyForJob")

