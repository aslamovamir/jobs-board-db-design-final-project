from model.Applicant.ApplicantUser import ApplicantUser
from model.Company.CompanyUser import CompanyUser
from helpers.MenuHelper import MenuHelper
from authentication.AuthenticationHelpers import AuthenticationHelper


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
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                if terminateOperation:
                    return True

                # terminate operation
                elif decision == -1:
                    return True

                break     

            except Exception as e:
                MenuHelper.DisplayErrorException(exception=e, errorSource="UpdateAccount::UpdateApplicantAccount")
            
        # To-DO: UPDATE THE USER's ACCOUNT PARAMETERS WITH THE DATABASE ACTION
        print("NEW: ")
        print(email)
        print(firstName)
        print(lastName)


    # method to update the account of a company user
    def UpdateCompanyUser(loggedUser: CompanyUser) -> bool:
        pass


