from helpers.MenuHelper import MenuHelper
from authentication.AuthenticationHelpers.AuthenticationHelper import AuthenticationHelper
from model.Applicant.ApplicantUser import ApplicantUser
from database.ApplicantUserDBActions import ApplicantUserDBActions
from database.CompanyUserDBActions import CompanyUserDBActions
from model.Company.CompanyUser import CompanyUser


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
                    Signup.RegisterNewApplicantUser()
            
                elif decision == 2:
                    MenuHelper.DisplaySelectedOption(selectedOption=options[decision-1])
                    Signup.RegisterNewCompanyUser()
                
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
                    # check for empty input
                    if MenuHelper.ValidateEmptyInput(input=username):
                        MenuHelper.WarnInvalidInput()
                        continue
                    # check if user already exists with the given username
                    if ApplicantUserDBActions.CheckExistsGivenUsername(username=username):
                        print("\nError! User already exists with the given username. Please try a new username.")
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
                LastName=lastName
            )

            # now try to insert the new user object into the database
            try:
                if ApplicantUserDBActions.InsertNewApplicantUser(applicantUser=newUser):
                    MenuHelper.InformSuccessOperation()
                    return True
                else:
                    MenuHelper.InformFailureOperation()
                    return False
            except Exception as e:
                MenuHelper.DisplayErrorException(exception=e, errorSource="Signup::RegisterNewApplicantUser::InsertNewApplicantUser")
                return False

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="Signup::RegisterNewApplicantUser")
            return False


    # method to add a new CompanyUser
    def RegisterNewCompanyUser() -> bool:

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
                    # check for empty input
                    if MenuHelper.ValidateEmptyInput(input=username):
                        MenuHelper.WarnInvalidInput()
                        continue
                    # check if user already exists with the given username
                    if CompanyUserDBActions.CheckExistsGivenUsername(username=username):
                        print("\nError! User already exists with the given username. Please try a new username.")
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
                    print("\nPlease enter company email address")
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

            # company name
            while True:
                try:
                    print("\nPlease enter company name")
                    companyName: str = MenuHelper.InputStream()
                    if companyName == "-1":
                        terminateOperation = True
                        break
                    if MenuHelper.ValidateEmptyInput(input=companyName):
                        MenuHelper.WarnInvalidInput()
                        continue
                    break
                except:
                    MenuHelper.WarnInvalidInput()

            if terminateOperation:
                return True   


            # create a new CompanyUser object with the input parameters
            newUser: CompanyUser = CompanyUser(
                Username=username,
                Password=password,
                Email=email,
                CompanyName=companyName
            )

            # now try to insert the new user object into the database
            try:
                if CompanyUserDBActions.InsertNewCompanyUser(companyUser=newUser):
                    MenuHelper.InformSuccessOperation()
                    return True
                else:
                    MenuHelper.InformFailureOperation()
                    return False
            except Exception as e:
                MenuHelper.DisplayErrorException(exception=e, errorSource="Signup::RegisterNewCompanyUser::InsertNewCompanyUser")
                return False

        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="Signup::RegisterNewCompanyUser")
            return False   