from model.Applicant.ApplicantUser import ApplicantUser
from model.Company.CompanyUser import CompanyUser
from helpers.MenuHelper import MenuHelper
from authentication.AuthenticationHelpers.AuthenticationHelper import AuthenticationHelper
from database.ApplicantUserDBActions import ApplicantUserDBActions


# class for the UpdateAccount
class UpdateAccount:

    # method to update the account of an applicant user
    def UpdateApplicantAccount(loggedUser: ApplicantUser) -> ApplicantUser:
        MenuHelper.DefineSectionBreak()
        terminateOperation: bool = False

        # entry
        print("\nPlease indicate what you would like to update in your account.")

        # menu options
        options: list[str] = ["Email", "First Name", "Last Name"]

        # initialie the new account parameters with what the user originally had
        email: str = loggedUser.Email
        firstName: str = loggedUser.FirstName
        lastName: str = loggedUser.LastName


        while True:
            try:
                MenuHelper.RequestInput()
                MenuHelper.DisplayMenuOptions(options=options)

                # take in the menu option entered
                decision: int = MenuHelper.InputOption()

                # update email
                if decision == 1:
                    while True:
                        try:
                            print("\nPlease enter a new email address")
                            email = MenuHelper.InputStream()
                            if email == "-1":
                                terminateOperation = True
                                break
                            if not AuthenticationHelper.ValidateEmail(email=email):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your email address changed to: ", email)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()

                    if terminateOperation:
                        break

                # update first name
                elif decision == 2:
                    while True:
                        try:
                            print("\nPlease enter a new first name")
                            firstName = MenuHelper.InputStream()
                            if firstName == "-1":
                                terminateOperation = True
                                break
                            if MenuHelper.ValidateEmptyInput(input=firstName):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your first name changed to: ", firstName)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()

                    if terminateOperation:
                        break

                # update last name
                elif decision == 3:
                    while True:
                        try:
                            print("\nPlease enter a new last name")
                            lastName = MenuHelper.InputStream()
                            if lastName == "-1":
                                terminateOperation = True
                                break
                            if MenuHelper.ValidateEmptyInput(input=lastName):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your email last name changed to: ", lastName)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                    if terminateOperation:
                        break

                # terminate operation
                elif decision == -1:
                    break   

            except Exception as e:
                MenuHelper.DisplayErrorException(exception=e, errorSource="UpdateAccount::UpdateApplicantAccount")

        if terminateOperation:
            return loggedUser
 
        while True:
            try:
                print("\nThis is your new account information: ")
                print("Email: ", email)
                print("First Name: ", firstName)
                print("Last Name: ", lastName)

                # ask for change confirmation
                if MenuHelper.ConfirmChanges():
                    # To-DO: UPDATE THE USER's ACCOUNT PARAMETERS WITH THE DATABASE ACTION

                    # manually change the attributes of the local variable as well
                    loggedUser.Email = email
                    loggedUser.FirstName = firstName
                    loggedUser.LastName = lastName

                    # now attempt to update the column values of the applicant user row in the database
                    if ApplicantUserDBActions.UpdateAccountInfo(loggedUser=loggedUser):
                        MenuHelper.InformSuccessOperation()
                        return loggedUser
                    else:
                        raise Exception("\nFailure! Update of the applicant user account information failed when calling the database action method.\n")
                else:
                    MenuHelper.InformMenuQuit()
                    return loggedUser
            except:
                MenuHelper.WarnInvalidInput()
                

    # method to update the account of a company user
    def UpdateCompanyUser(loggedUser: CompanyUser) -> bool:
        pass


