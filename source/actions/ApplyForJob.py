from model.Applicant.ApplicantUser import ApplicantUser
from model.JobPosting.JobPosting import JobPosting
from model.JobPosting.AppliedJobPosting import AppliedJob
from helpers.MenuHelper import MenuHelper
from database.ApplicantUserDBActions import ApplicantUserDBActions
from database.CompanyUserDBActions import CompanyUserDBActions


# class for ApplyForJob
class ApplyForJob:

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
                    print("\nPlease explain if you woul require any work visa sponsorship")
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
                CompanyID=jobPosting.ID,
                ApplicantID=ApplicantUserDBActions.ReturnIDUser(username=loggedUser.Username),
                Status="Unreviewed",
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
                        # TODO: FINISH PUSH OF THE APPLIED JOB INSTANCE TO THE DATABASE
                        pass
                    else:
                        MenuHelper.WarnInvalidInput()
                except:
                    MenuHelper.WarnInvalidInput()
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="ApplyForJob::ApplyForJob")

