from helpers.MenuHelper import MenuHelper
from authentication.AuthenticationHelpers.AuthenticationHelper import AuthenticationHelper
from model.Applicant.ApplicantUser import ApplicantUser
# from model.Company import CompanyUser


class Signup:

    # signup method
    def SignUp():
        MenuHelper.DefineSectionBreak()

        # let the user know they need to select the type of user they want to sign up for
        print("\nPlease indicate the type of user you want to sign up as.\n")

        # define menu options for the user
        options: list[str] = ['Applicant User', 'Company User']

        while True:
            try:
                MenuHelper.RequestInput()
                MenuHelper.DisplayMenuOptions(options=options)

                # take in the menu option entered
                decision: int = MenuHelper.InputOption()

                # check the menu option selected and redirect the user correspondignly
                if decision == 1:
                    MenuHelper.DisplaySelectedOption(selectedOption=options[decision-1])
                    if Signup.RegisterNewApplicantUser():
                        pass
            
                elif decision == 2:
                    MenuHelper.DisplaySelectedOption(selectedOption=options[decision-1])
                    pass
                
                elif decision == -1:
                    MenuHelper.InformMenuQuit()
                    break

                else:
                    MenuHelper.WarnInvalidInput()

            except Exception as e:
                MenuHelper.WarnInvalidInput()



    # method to add a new ApplicantUser
    def RegisterNewApplicantUser() -> bool:

        MenuHelper.DefineSectionBreak()
        terminateOperation: bool = False
        try:
            # username
            while True:
                try:
                    print("\nPlease enter a username")
                    username: str = MenuHelper.InputStream()
                    if username == "-1":
                        terminateOperation = True
                        break
                    if MenuHelper.ValidateEmptyInput(input=username):
                        MenuHelper.WarnInvalidInput()
                        continue
                    break
                except:
                    MenuHelper.WarnInvalidInput()
            
            if terminateOperation:
                return True

            # password
            while True:
                try: 
                    print("\nNOTE: Password must be of size between 8 and 12, have at least one uppercase letter,",
                    "one digit and one special character.")
                    print("Please enter a password")
                    password: str = MenuHelper.InputStream()
                    if password == "-1":
                        terminateOperation = True
                        break
                    if not AuthenticationHelper.ValidatePassword(password=password):
                        MenuHelper.WarnInvalidInput()
                        continue
                    break
                except:
                    MenuHelper.WarnInvalidInput()
            
            if terminateOperation:
                return True

            # email address
            while True:
                try:
                    print("\nPlease enter your email address")
                    email: str = MenuHelper.InputStream()
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
                return True

            # first name
            while True:
                try:
                    print("\nPlease enter your first name")
                    firstName: str = MenuHelper.InputStream()
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

            # last name
            while True:
                try:
                    print("\nPlease enter your last name")
                    lastName: str = MenuHelper.InputStream()
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

            # create a new ApplicantUser object with the input parameters
            newUser: ApplicantUser = ApplicantUser(
                Username=username, 
                Password=password,
                Email=email,
                FirstName=firstName,
                LastName=lastName)

            

            return True

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="Signup::RegisterNewUser")
            return False
                