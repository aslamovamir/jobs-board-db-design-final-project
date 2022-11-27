from helpers.MenuHelper import MenuHelper
from authentication.AuthenticationHelpers.AuthenticationHelper import AuthenticationHelper
from database.ApplicantUserDBActions import ApplicantUserDBActions


# class for Signin
class Signin:

    # signin method
    def Signin():
        # let the user know they need to select the type of user they want to sign up for
        print("\nPlease indicate the type of user you want to sign in as.\n")

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
                    Signin.LoginApplicantUser()
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

    
    # method to signin ApplicantUser
    def LoginApplicantUser():
        MenuHelper.DefineSectionBreak()
        terminateOperation: bool = False

        try:
            # username
            while True:
                try:
                    print("\nPlease enter your username")
                    username: str = MenuHelper.InputStream()
                    if username == "-1":
                        terminateOperation = True
                        break
                    # check if empty input
                    if MenuHelper.ValidateEmptyInput(input=username):
                        MenuHelper.WarnInvalidInput()
                        continue
                    # check if user already exists with the given username
                    if ApplicantUserDBActions.CheckExistsGivenUsername(username=username):
                        print("User already exists with the given username. Please try a new username.")
                        MenuHelper.InformFailureOperation()
                        continue
                    break
                except:
                    MenuHelper.WarnInvalidInput()
            
            if terminateOperation:
                return True

            # password
            while True:
                try: 
                    print("\nPlease enter your password")
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


            # check the database if this user with the username and password exists
            try:
                if ApplicantUserDBActions.CheckExistsGivenUsernamePassword(username=username, password=password):
                    #TO-DO: create another method to return the user as an object from the database
                    print("USER EXISTS")
                    pass
                else:
                    MenuHelper.InformFailureOperation()
                    return
            except Exception as e:
                MenuHelper.DisplayErrorException(exception=e, errorSource="Signin::LoginApplicantUser::CheckExistsApplicantUser")
                return
            


        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="Signin::LoginApplicantUser")
            return False