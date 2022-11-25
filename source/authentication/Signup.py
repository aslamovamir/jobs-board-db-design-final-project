from helpers.MenuHelper import MenuHelper
from authentication.AuthenticationHelpers.AuthenticationHelper import AuthenticationHelper
# from model.Applicant import ApplicantUser
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
        # TO-DO: ADD THE INPUT FROM THE MENU HELPER TO ALLOW THE USER QUIT OUT OF INPUT STREAMS
        try:
            # username
            while True:
                try:
                    username: str = input("\nPlease enter a username: ")
                    if MenuHelper.ValidateEmptyInput(input=username):
                        MenuHelper.WarnInvalidInput()
                        continue
                    break
                except:
                    MenuHelper.WarnInvalidInput()

            # password
            while True:
                try: 
                    print("\nNOTE: Password must be of size between 8 and 12, have at least one uppercase letter,",
                    "one digit and one special character.")
                    password: str = input("\nPlease enter a password:")
                    if not AuthenticationHelper.ValidatePassword(password=password):
                        MenuHelper.WarnInvalidInput()
                        continue
                    break
                except:
                    MenuHelper.WarnInvalidInput()

            # email address
            while True:
                try:
                    email: str = input("\nPlease enter your email address: ")
                    if not AuthenticationHelper.ValidateEmail(email=email):
                        MenuHelper.WarnInvalidInput()
                        continue
                    break
                except:
                    MenuHelper.WarnInvalidInput()

            # first name
            while True:
                try:
                    firstName: str = input("\nPlease enter your first name: ")
                    if MenuHelper.ValidateEmptyInput(input=firstName):
                        MenuHelper.WarnInvalidInput()
                        continue
                    break
                except:
                    MenuHelper.WarnInvalidInput()

            # last name
            while True:
                try:
                    lastName: str = input("\nPlease enter your last neme: ")
                    if MenuHelper.ValidateEmptyInput(input=lastName):
                        MenuHelper.WarnInvalidInput()
                        continue
                    break
                except:
                    MenuHelper.WarnInvalidInput()
            

            
            print(username)
            print(password)
            print(email)
            print(firstName)
            print(lastName)


            return True

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="Signup::RegisterNewUser")
            return False
                