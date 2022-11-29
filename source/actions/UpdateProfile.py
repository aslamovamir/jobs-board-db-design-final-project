from model.Applicant.ApplicantUser import ApplicantUser
from model.Applicant.ApplicantProfile import ApplicantProfile, Experience, Education
from model.Company.CompanyUser import CompanyUser
# from model.Company.CompanyProfile import CompanyProfile
from helpers.MenuHelper import MenuHelper
from database.ApplicantUserDBActions import ApplicantUserDBActions


class UpdateProfile:


    # method to update the profile of an applicant user:
    def UpdateApplicantProfile(loggedUser: ApplicantUser) -> ApplicantProfile:

        # if user has profile, initialie the new profile parameters with what the user originally had
        # first check if the user has profile
        userHasProfile: bool = False
        try:
            if ApplicantUserDBActions.CheckUserHasProfile(loggedUser=loggedUser):
                userHasProfile = True
                print("\nUSER HAS A PROFILE IN THE DB!\n")
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="UpdateProfile::UpdateApplicantProfile::ApplicantUserDBActions::CheckUserHasProfile")

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

        if userHasProfile:
            # if the user already has a profile, we fetch the origingal profile
            # orginalProfile: ApplicantProfile = FINISH!
            pass
        
        MenuHelper.DefineSectionBreak()

         # entry
        print("\nPlease indicate what you would like to update in your account.")

        # menu options
        options: list[str] = ["Title", "About", "Gender", "Ethnicity", "Disability Status",
            "Location", "Phone Number", "Education", "Experience"]

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
                    
                # update education
                elif decision == 8:
                    while True:
                        try:
                            # TODO: MODIFY THE EDUCAION LIST SECTION INPUT CHANGE
                            # print("\nPlease enter a new education")
                            # ethnicity = MenuHelper.InputStream()
                            # if ethnicity == "-1":
                            #     break
                            # if MenuHelper.ValidateEmptyInput(input=ethnicity):
                            #     MenuHelper.WarnInvalidInput()
                            #     continue
                            # print("Success! Your ethnicity changed to: ", ethnicity)
                            # break
                            pass
                        except:
                            MenuHelper.WarnInvalidInput()

                # update experience
                elif decision == 9:
                    while True:
                        try:
                            # TODO: MODIFY THE EXPERIENCE LIST SECTION INPUT CHANGE
                            # print("\nPlease enter a new ethnicity")
                            # ethnicity = MenuHelper.InputStream()
                            # if ethnicity == "-1":
                            #     break
                            # if MenuHelper.ValidateEmptyInput(input=ethnicity):
                            #     MenuHelper.WarnInvalidInput()
                            #     continue
                            # print("Success! Your ethnicity changed to: ", ethnicity)
                            # break
                            pass
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
                # TODO: PRINT EDUCATION AND EXPERIENCE LIST

                # ask for change confirmation
                if MenuHelper.ConfirmChanges():
                    # TODO: send the local profile object and either add or update the profile row in the database
                    pass
                else:
                    MenuHelper.InformMenuQuit()
                    # TODO: Return the original profile if the user had a profile
                    # otherwise, return None
                    pass

            except:
                MenuHelper.WarnInvalidInput()


    # method to update the profile of a company user
    def UpdateCompanyProfile(loggedUser: CompanyUser) -> bool:
        pass