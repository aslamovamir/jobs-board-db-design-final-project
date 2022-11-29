from helpers.MenuHelper import MenuHelper
from authentication.AuthenticationHelpers.AuthenticationHelper import AuthenticationHelper
from database.ApplicantUserDBActions import ApplicantUserDBActions
from database.CompanyUserDBActions import CompanyUserDBActions
from model.Applicant.ApplicantUser import ApplicantUser
from model.Applicant.ApplicantModelHelper import ApplicantModelHelper
from model.Company.CompanyUser import CompanyUser
from model.Company.CompanyModelHelper import CompanyModelHelper
from actions.DisplayAccountInfo import DisplayAccountInfo
from actions.UpdateAccount import UpdateAccount
from actions.UpdateProfile import UpdateProfile


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
                    Signin.LoginCompanyUser()
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
                    loggedApplicantUser: ApplicantUser = ApplicantUserDBActions.ReturnApplicantUser(
                        id=ApplicantModelHelper.CreateApplicantUserId(username=username, password=password)
                    )
                    
                    Signin.ShowMenuLoggedApplicantUser(loggedUser=loggedApplicantUser)

                else:
                    MenuHelper.InformFailureOperation()
                    return
            except Exception as e:
                MenuHelper.DisplayErrorException(exception=e, errorSource="Signin::LoginApplicantUser::CheckExistsApplicantUser")
                return      

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="Signin::LoginApplicantUser")
            return False

    
    # method to signin CompanyUser
    def LoginCompanyUser():
        MenuHelper.DefineSectionBreak()
        terminateOperation: bool = False

        try:
            # username
            while True:
                try:
                    print("\nPlease enter company username")
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
                    print("\nPlease enter company password")
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
                if CompanyUserDBActions.CheckExistsGivenUsernamePassword(username=username, password=password):
                    loggedCompanyUser: CompanyUser = CompanyUserDBActions.ReturnCompanyUser(
                        id=CompanyModelHelper.CreateCompanyUserId(username=username, password=password)
                    )
                    
                    Signin.ShowMenuLoggedCompanyUser(loggedUser=loggedCompanyUser)
                
                else:
                    MenuHelper.InformFailureOperation()
                    return
            except Exception as e:
                MenuHelper.DisplayErrorException(exception=e, errorSource="Signin::LoginCompanyUser::CheckExistsCompanyUser")
                return

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="Signin::LoginCompanyUser")
            return False

    
    # show menu options for the applicant user
    def ShowMenuLoggedApplicantUser(loggedUser: ApplicantUser):
        MenuHelper.DefineSectionBreak()
        logoutSession: bool = False

        # welcome logged user
        MenuHelper.WelcomeApplicantUser(loggedUser=loggedUser)

        # menu options
        options: list[str] = ["Show your account information", "Update your account", 
            "Show your profile information", "Update your profile information", "Log out"]

        while True:
            try:
                MenuHelper.RequestInput()
                MenuHelper.DisplayMenuOptions(options=options)

                # take in the menu option entered
                decision: int = MenuHelper.InputOption()

                # check the menu option selected and redirect the user correspondignly
                if decision == 1:
                    MenuHelper.DisplaySelectedOption(selectedOption=options[decision-1])
                    DisplayAccountInfo.DisplayApplicantInfo(loggedUser=loggedUser)
                    pass
            
                elif decision == 2:
                    MenuHelper.DisplaySelectedOption(selectedOption=options[decision-1])
                    updateResult = UpdateAccount.UpdateApplicantAccount(loggedUser=loggedUser) 
                    if updateResult != None:
                        loggedUser = updateResult

                elif decision == 3:
                    MenuHelper.DisplaySelectedOption(selectedOption=options[decision-1])
                    # TO DO: IMPLEMENT SHOW PROFILE INFORMATION ACTION METHOD
                    pass
                
                elif decision == 4:
                    MenuHelper.DisplaySelectedOption(selectedOption=options[decision-1])
                    UpdateProfile.UpdateApplicantProfile(loggedUser=loggedUser)
                
                # TO_DO: IMPLEMENT LOGOUT
                elif decision == -1:
                    MenuHelper.InformMenuQuit()
                    break

                else:
                    MenuHelper.WarnInvalidInput()

            except Exception as e:
                MenuHelper.WarnInvalidInput()

    
    # show menu options for the company user
    def ShowMenuLoggedCompanyUser(loggedUser: CompanyUser):
        MenuHelper.DefineSectionBreak()
        logoutSession: bool = False

        # welcome logged user
        MenuHelper.WelcomeCompanyUser(loggedUser=loggedUser)

        # menu options
        options: list[str] = ["Show company account information", "Update company account", "Log out"]

        while True:
            try:
                MenuHelper.RequestInput()
                MenuHelper.DisplayMenuOptions(options=options)

                # take in the menu option entered
                decision: int = MenuHelper.InputOption()

                # check the menu option selected and redirect the user correspondignly
                if decision == 1:
                    MenuHelper.DisplaySelectedOption(selectedOption=options[decision-1])
                    DisplayAccountInfo.DisplayCompanyInfo(loggedUser=loggedUser)
                    pass
            
                elif decision == 2:
                    MenuHelper.DisplaySelectedOption(selectedOption=options[decision-1])
                    updateResult = UpdateAccount.UpdateCompanyUser(loggedUser=loggedUser)
                    if updateResult != None:
                        loggedUser = updateResult
                
                # TO_DO: IMPLEMENT LOGOUT
                elif decision == -1:
                    MenuHelper.InformMenuQuit()
                    break

                else:
                    MenuHelper.WarnInvalidInput()

            except Exception as e:
                MenuHelper.WarnInvalidInput()