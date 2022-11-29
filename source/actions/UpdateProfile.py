from model.Applicant.ApplicantUser import ApplicantUser
from model.Applicant.ApplicantProfile import ApplicantProfile
from model.Company.CompanyUser import CompanyUser
from model.Company.CompanyProfile import CompanyProfile
from helpers.MenuHelper import MenuHelper
from database.ApplicantUserDBActions import ApplicantUserDBActions
from database.CompanyUserDBActions import CompanyUserDBActions


class UpdateProfile:


    # method to update the profile of an applicant user:
    def UpdateApplicantProfile(loggedUser: ApplicantUser) -> bool:

        # if user has profile, initialie the new profile parameters with what the user originally had
        # first check if the user has profile
        userHasProfile: bool = False
        try:
            if ApplicantUserDBActions.CheckUserHasProfile(loggedUser=loggedUser):
                userHasProfile = True
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="UpdateProfile::UpdateApplicantProfile::ApplicantUserDBActions::CheckUserHasProfile")


        if userHasProfile:
            # if the user already has a profile, we fetch the origingal profile
            newProfile: ApplicantProfile = ApplicantUserDBActions.RetrieveProfile(loggedUser=loggedUser)
        else:
            # default initial profile object with parameters initialized to None
            newProfile: ApplicantProfile = ApplicantProfile(
                ApplicantID=ApplicantUserDBActions.ReturnIDUser(username=loggedUser.Username),
                Title=None,
                About=None,
                Gender=None,
                Ethnicity=None,
                DisabilityStatus=None,
                Location=None,
                PhoneNumber=None
            )
        
        MenuHelper.DefineSectionBreak()
         # entry
        print("\nPlease indicate what you would like to update in your account.")

        # menu options
        options: list[str] = ["Title", "About", "Gender", "Ethnicity", "Disability Status",
            "Location", "Phone Number"]

        while True:
            try:
                MenuHelper.RequestInput()
                MenuHelper.DisplayMenuOptions(options=options)

                # take in the menu option entered
                decision: int = MenuHelper.InputOption()

                # update title
                if decision == 1:
                    while True:
                        try:
                            print("\nPlease enter a new title")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.Title = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.Title):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your title changed to: ", newProfile.Title)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()

                # update about
                elif decision == 2:
                    while True:
                        try:
                            print("\nPlease enter a new about section")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.About = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.About):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your about section changed to: ", newProfile.About)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                # update gender
                elif decision == 3:
                    while True:
                        try:
                            print("\nPlease enter a new gender")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.Gender = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.Gender):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your gender changed to: ", newProfile.Gender)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                # update ethnicity
                elif decision == 4:
                    while True:
                        try:
                            print("\nPlease enter a new ethnicity")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.Ethnicity = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.Ethnicity):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your ethnicity changed to: ", newProfile.Ethnicity)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                # update disability status
                elif decision == 5:
                    while True:
                        try:
                            print("\nPlease enter a new disability status")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.DisabilityStatus = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.DisabilityStatus):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your disability status changed to: ", newProfile.DisabilityStatus)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                    
                # update location
                elif decision == 6:
                    while True:
                        try:
                            print("\nPlease enter a new location")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.Location = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.Location):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your location changed to: ", newProfile.Location)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                # update phone number
                elif decision == 7:
                    while True:
                        try:
                            print("\nPlease enter a new phone number")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.PhoneNumber = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.PhoneNumber):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your phone number changed to: ", newProfile.PhoneNumber)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                elif decision == -1:
                    break
            
            except Exception as e:
                MenuHelper.WarnInvalidInput()
        
        while True:
            try:
                print("\nThis is your new profile information: ")
                print("Title: ", newProfile.Title)
                print("About: ", newProfile.About)
                print("Gender: ", newProfile.Gender)
                print("Ethnicity: ", newProfile.Ethnicity)
                print("Disability Status: ", newProfile.DisabilityStatus)
                print("Location: ", newProfile.Location)
                print("Phone Number: ", newProfile.PhoneNumber)

                # ask for change confirmation
                if MenuHelper.ConfirmChanges():
                    # send the local profile object and either add or update the profile row in the database
                    if not userHasProfile:
                        try:
                            if ApplicantUserDBActions.InsertNewProfile(newProfile=newProfile):
                                MenuHelper.InformSuccessOperation()
                                return True
                            else:
                                MenuHelper.InformFailureOperation()
                                return False
                        except Exception as e:
                            MenuHelper.DisplayErrorException(exception=e, errorSource="UpdateProfile::UpdateApplicantProfile::InsertNewProfile")
                    else:
                        try:
                            if ApplicantUserDBActions.UpdateProfile(newProfile=newProfile):
                                MenuHelper.InformSuccessOperation()
                                return True
                            else:
                                MenuHelper.InformFailureOperation()
                                return False
                        except Exception as e:
                            MenuHelper.DisplayErrorException(exception=e, errorSource="UpdateProfile::UpdateApplicantProfile::UpdateProfile")
                else:
                    MenuHelper.InformMenuQuit()
                    return True

            except:
                MenuHelper.WarnInvalidInput()


    # method to update the profile of a company user
    def UpdateCompanyProfile(loggedUser: CompanyUser) -> bool:

        # if user has profile, initialie the new profile parameters with what the user originally had
        # first check if the user has profile
        userHasProfile: bool = False
        try:
            if CompanyUserDBActions.CheckUserHasProfile(loggedUser=loggedUser):
                userHasProfile = True
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="UpdateProfile::UpdateCompanyProfile::CompanytUserDBActions::CheckUserHasProfile")


        if userHasProfile:
            # if the user already has a profile, we fetch the origingal profile
            newProfile: CompanyProfile = CompanyUserDBActions.RetrieveProfile(loggedUser=loggedUser)
        else:
            # default initial profile object with parameters initialized to None
            newProfile: CompanyProfile = CompanyProfile(
                CompanyID=CompanyUserDBActions.ReturnIDUser(username=loggedUser.Username),
                About=None,
                Location=None,
                Industry=None,
                ServiceType=None,
                CompanyType=None,
                AnnualRevenue=None,
                EmployeeSize=None,
                FoundationDate=None,
                InternationalHires=None
            )
        
        MenuHelper.DefineSectionBreak()
         # entry
        print("\nPlease indicate what you would like to update in the company account.")

        # menu options
        options: list[str] = ["About", "Location", "Industry", "Service Type", "Company Type", "Annual Revenue",
            "Employee Size", "Foundation Date", "International Hires"]

        while True:
            try:
                MenuHelper.RequestInput()
                MenuHelper.DisplayMenuOptions(options=options)

                # take in the menu option entered
                decision: int = MenuHelper.InputOption()

                # update about
                if decision == 1:
                    while True:
                        try:
                            print("\nPlease enter a new about section")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.About= input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.About):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! The company about section changed to: ", newProfile.About)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()

                # update location
                elif decision == 2:
                    while True:
                        try:
                            print("\nPlease enter a new location")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.Location = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.Location):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! The company location changed to: ", newProfile.Location)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                # update industry
                elif decision == 3:
                    while True:
                        try:
                            print("\nPlease enter a new industry")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.Industry = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.Industry):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! The company industry changed to: ", newProfile.Industry)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                # update service type
                elif decision == 4:
                    while True:
                        try:
                            print("\nPlease enter a new service type")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.ServiceType = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.ServiceType):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! The company service type changed to: ", newProfile.ServiceType)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                # update company type
                elif decision == 5:
                    while True:
                        try:
                            print("\nPlease enter a new company type")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.CompanyType = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.CompanyType):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! The company type changed to: ", newProfile.CompanyType)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                    
                # update annual revenue
                elif decision == 6:
                    while True:
                        try:
                            print("\nPlease enter a new annual revenue")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.AnnualRevenue = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.AnnualRevenue):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! The company annual revenue changed to: ", newProfile.AnnualRevenue)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                # update employee size
                elif decision == 7:
                    while True:
                        try:
                            print("\nPlease enter a new employee size")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.EmployeeSize = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.EmployeeSize):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! The company employee size changed to: ", newProfile.EmployeeSize)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                # update foundation date
                elif decision == 8:
                    while True:
                        try:
                            print("\nPlease enter a new foundation date")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.FoundationDate = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.FoundationDate):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! The company foundation date changed to: ", newProfile.FoundationDate)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                # update international hires
                elif decision == 9:
                    while True:
                        try:
                            print("\nPlease enter a new international hires section")
                            input = MenuHelper.InputStream()
                            if input == "-1":
                                break
                            newProfile.InternationalHires = input
                            if MenuHelper.ValidateEmptyInput(input=newProfile.InternationalHires):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! The company international hires section changed to: ", newProfile.InternationalHires)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                
                elif decision == -1:
                    break
            
            except Exception as e:
                MenuHelper.WarnInvalidInput()
        
        while True:
            try:
                print("\nThis is the company's new profile information: ")
                print("About: ", newProfile.About)
                print("Location: ", newProfile.Location)
                print("Industry: ", newProfile.Industry)
                print("Service Type: ", newProfile.ServiceType)
                print("Company Type: ", newProfile.CompanyType)
                print("Annual Revenue: ", newProfile.AnnualRevenue)
                print("Employee Size: ", newProfile.EmployeeSize)
                print("Foundation Date: ", newProfile.FoundationDate)
                print("International Hires: ", newProfile.InternationalHires)

                # ask for change confirmation
                if MenuHelper.ConfirmChanges():
                    # send the local profile object and either add or update the profile row in the database
                    if not userHasProfile:
                        try:
                            if CompanyUserDBActions.InsertNewProfile(newProfile=newProfile):
                                MenuHelper.InformSuccessOperation()
                                return True
                            else:
                                MenuHelper.InformFailureOperation()
                                return False
                        except Exception as e:
                            MenuHelper.DisplayErrorException(exception=e, errorSource="UpdateProfile::UpdateCompanyProfile::InsertNewProfile")
                    else:
                        try:
                            if CompanyUserDBActions.UpdateProfile(newProfile=newProfile):
                                MenuHelper.InformSuccessOperation()
                                return True
                            else:
                                MenuHelper.InformFailureOperation()
                                return False
                        except Exception as e:
                            MenuHelper.DisplayErrorException(exception=e, errorSource="UpdateProfile::UpdateCompanyProfile::UpdateProfile")
                else:
                    MenuHelper.InformMenuQuit()
                    return True

            except:
                MenuHelper.WarnInvalidInput()