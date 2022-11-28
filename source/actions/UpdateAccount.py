from model.Applicant.ApplicantUser import ApplicantUser
from model.Company.CompanyUser import CompanyUser
from helpers.MenuHelper import MenuHelper
from authentication.AuthenticationHelpers.AuthenticationHelper import AuthenticationHelper


# class for the UpdateAccount
class UpdateAccount:

    # method to update the account of an applicant user
    def UpdateApplicantAccount(loggedUser: ApplicantUser) -> bool:
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
                            print("Success! Your first name changed to: ", email)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()

                    if terminateOperation:
                        return True

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
                            print("Success! Your email last name changed to: ", email)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                    if terminateOperation:
                        return True

                # terminate operation
                elif decision == -1:
                    break   

            except Exception as e:
                MenuHelper.DisplayErrorException(exception=e, errorSource="UpdateAccount::UpdateApplicantAccount")

        if terminateOperation:
            return True
 
        while True:
            try:
                print("\nThis is your new account information: ")
                print("Email: ", email)
                print("First Name: ", firstName)
                print("Last Name: ", lastName)

                # ask for change confirmation
                if MenuHelper.ConfirmChanges():
                    # To-DO: UPDATE THE USER's ACCOUNT PARAMETERS WITH THE DATABASE ACTION
                    pass
                else:
                    pass
            except:
                MenuHelper.WarnInvalidInput()
                

    # method to update the account of a company user
    def UpdateCompanyUser(loggedUser: CompanyUser) -> bool:
        pass

