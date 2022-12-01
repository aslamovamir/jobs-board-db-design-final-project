from helpers.MenuHelper import MenuHelper
from model.JobPosting.AppliedJobPosting import AppliedJob
from model.Applicant.ApplicantUser import ApplicantUser
from database.AppliedJobDBActions import AppliedJobDBActions
from database.ApplicantUserDBActions import ApplicantUserDBActions
from actions.DisplayProfileInfo import DisplayProfileInfo


# class for the action to display all appicants for a particular job
class DisplayApplicantsForJob:

    # helper method to display details of an applied job
    def HelpDisplayAppliedJob(appliedJob: AppliedJob, applicantFullName: str):
        # TODO: first, update the status of the applied job to "Reviewed"
        pass

        MenuHelper.DefineSectionBreak()
        print("\nHere's the full application of the applicant:\n")
        print("Applicant Name: ", applicantFullName)
        print("Position Name: ", AppliedJobDBActions.ReturnPositionNameAppliedJob(jobPostingID=appliedJob.JobPostingID))
        print("Status: ", appliedJob.Status)
        print("Start Date: ", appliedJob.StartDate)
        print("Good Fit Reasoning: ", appliedJob.GoodFitExplanation)
        print("Date Applied: ", appliedJob.DateApplied)
        MenuHelper.DefineSectionBreak()


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

        # now get all the usernames and full names of the applicants
        try:
            allAplicants: list[ApplicantUser] = []

            # first get all applicant users
            for appliedJob in allAppliedJobsInstances:
                allAplicants.append(ApplicantUserDBActions.ReturnApplicantUser(id=appliedJob.ApplicantID))
            
            # save the applicant's as a string for reuse
            applicantsOutput: str = ""
            index: int = 1
            for i in range(len(allAplicants)):
                applicantsOutput += f"\n{index}. "
                applicantsOutput += f"{allAplicants[i].LastName}, {allAplicants[i].FirstName} - {allAplicants[i].Username}"
                index += 1
            
            # now ask to show the details of the applicant's application for the job
            while True:
                terminateOperation: bool = False
                try:
                    if terminateOperation:
                        break
                    # now display their username and full names in a list
                    print(applicantsOutput)
                    print("\nWould you like to review the full application of applicants? (Y/N)")
                    input: str = MenuHelper.InputStream()
                    if input == "-1":
                        MenuHelper.InformMenuQuit()
                        break
                    elif input == "Y":
                        while True:
                            try:
                                print(applicantsOutput)
                                print("\nPlease indicate the index of the applicant")
                                input: str = MenuHelper.InputStream()
                                if input == "-1":
                                    terminateOperation = True
                                    break

                                index: int = int(input)
                                if index in range(1, len(allAplicants) + 1):
                                    if len(allAppliedJobsInstances) == len(allAplicants):
                                        try:
                                            # display details of the applied job
                                            DisplayApplicantsForJob.HelpDisplayAppliedJob(appliedJob=allAppliedJobsInstances[index-1], 
                                                applicantFullName=allAplicants[index-1].FirstName + ", " + allAplicants[index-1].LastName)
                                            # now ask to display the profile of the applicant for the job
                                            while True:
                                                try:
                                                    print("\nWould you like to review the profile of the applicant? (Y/N)")
                                                    input: str = MenuHelper.InputStream()
                                                    if input == "-1":
                                                        MenuHelper.InformMenuQuit()
                                                        break
                                                    elif input == "Y":
                                                        DisplayProfileInfo.DisplayApplicantProfileToCompany(applicantUser=allAplicants[index-1])
                                                        break
                                                    elif input == "N":
                                                        MenuHelper.InformMenuQuit()
                                                        break
                                                    else:
                                                        MenuHelper.WarnInvalidInput()
                                                except:
                                                    MenuHelper.WarnInvalidInput()
                                            
                                        except Exception as e:
                                            MenuHelper.DisplayErrorException(exception=e, errorSource="DisplayAllApplicantsForJob::DisplayAllApplicantsForJob::")
                                    else:
                                        raise Exception("\nFailure! The number of applied jobs is not equal to the number of applicants.\n")
                                else:
                                    MenuHelper.WarnInvalidInput()
                            except:
                                MenuHelper.WarnInvalidInput()
                    elif input == "N":
                        MenuHelper.InformMenuQuit()
                        break
                    else:
                        MenuHelper.WarnInvalidInput()

                except:
                    MenuHelper.WarnInvalidInput()
        
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="DisplayApplicantsForJob::ReturnApplicantUser")