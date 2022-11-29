from model.Company.CompanyUser import CompanyUser
from model.JobPosting.JobPosting import JobPosting
from helpers.MenuHelper import MenuHelper
from database.CompanyUserDBActions import CompanyUserDBActions
from database.JobPostingDBActions import JobPostingDBActions



# function to create a job posting
def CreateJobPosting(loggedUser: CompanyUser) -> bool:
    MenuHelper.DefineSectionBreak()
    terminateOperation: bool = False

    try:
        # position name
        while True:
            try:
                print("\nPlease enter postion name")
                input: str = MenuHelper.InputStream()
                if input == "-1":
                    terminateOperation = True
                    break
                if MenuHelper.ValidateEmptyInput(input=input):
                    MenuHelper.WarnInvalidInput()
                    continue
                positionName: str = input
                break
            except:
                MenuHelper.WarnInvalidInput()
        if terminateOperation:
            return True
        
        # pay
        while True:
            try:
                print("\nPlease enter pay")
                input: str = MenuHelper.InputStream()
                if input == "-1":
                    terminateOperation = True
                    break
                if MenuHelper.ValidateEmptyInput(input=input):
                    MenuHelper.WarnInvalidInput()
                    continue
                pay: str = input
                break
            except:
                MenuHelper.WarnInvalidInput()
        if terminateOperation:
            return True
        
        # location
        while True:
            try:
                print("\nPlease enter location")
                input: str = MenuHelper.InputStream()
                if input == "-1":
                    terminateOperation = True
                    break
                if MenuHelper.ValidateEmptyInput(input=input):
                    MenuHelper.WarnInvalidInput()
                    continue
                location: str = input
                break
            except:
                MenuHelper.WarnInvalidInput()
        if terminateOperation:
            return True

        # description
        while True:
            try:
                print("\nPlease enter description")
                input: str = MenuHelper.InputStream()
                if input == "-1":
                    terminateOperation = True
                    break
                if MenuHelper.ValidateEmptyInput(input=input):
                    MenuHelper.WarnInvalidInput()
                    continue
                description: str = input
                break
            except:
                MenuHelper.WarnInvalidInput()
        if terminateOperation:
            return True

        # department
        while True:
            try:
                print("\nPlease enter department")
                input: str = MenuHelper.InputStream()
                if input == "-1":
                    terminateOperation = True
                    break
                if MenuHelper.ValidateEmptyInput(input=input):
                    MenuHelper.WarnInvalidInput()
                    continue
                department: str = input
                break
            except:
                MenuHelper.WarnInvalidInput()
        if terminateOperation:
            return True

        # create a new JobPosting object with the input parameters
        newJobPosting: JobPosting = JobPosting(
            CompanyID=CompanyUserDBActions.ReturnIDUser(username=loggedUser.Username),
            PositionName=positionName,
            Pay=pay,
            Location=location,
            Description=description,
            Department=department
        )
        
        while True:
            try:
                print("\nThis is a new job posting:")
                print("Position Name: ", newJobPosting.PositionName)
                print("Pay: ", newJobPosting.Pay)
                print("Location: ", newJobPosting.Location)
                print("Description: ", newJobPosting.Description)
                print("Department: ", department)

                # ask for creation confirmation
                if MenuHelper.ConfirmChanges():
                    # now try to insert the new job posting object into the database
                    try:
                        if JobPostingDBActions.InsertNewJobPosting(newJobPosting=newJobPosting):
                            MenuHelper.InformSuccessOperation()
                            return True
                        else:
                            MenuHelper.InformFailureOperation()
                            return False
                    except Exception as e:
                        MenuHelper.DisplayErrorException(exception=e, errorSource="CreateJobPosting::InsertNewJobPosting")
                else:
                    MenuHelper.InformMenuQuit()
                    return True
            except:
                MenuHelper.WarnInvalidInput()

    except Exception as e:
        MenuHelper.DisplayErrorException(exception=e, errorSource="CreateJobPosting")