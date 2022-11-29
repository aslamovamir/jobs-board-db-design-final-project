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
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="UpdateProfile::UpdateApplicantProfile::ApplicantUserDBActions::CheckUserHasProfile")

        title: str = None
        about: str = None
        gender: str = None
        ethnicity: str = None
        disabilityStatus: str = None
        location: str = None
        phoneNumber: str = None
        educationList: list[Education] = None
        experienceList: list[Experience] = None

        # default initial profile object with parameters initialized to None
        newProfile: ApplicantProfile = ApplicantProfile(
            ApplicantID=ApplicantUserDBActions.ReturnIDUser(username=loggedUser.Username),
            Title=title,
            About=about,
            Gender=gender,
            Ethnicity=ethnicity,
            DisabilityStatus=disabilityStatus,
            Location=location,
            PhoneNumber=phoneNumber
        )

        if userHasProfile:
            # if the user already has a profile, we fetch the origingal profile
            # orginalProfile: ApplicantProfile = FINISH!
            pass
        
        MenuHelper.DefineSectionBreak()
        terminateOperation: bool = False

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
                            newProfile.Title = MenuHelper.InputStream()
                            if newProfile.title == "-1":
                                terminateOperation = True
                                break
                            if MenuHelper.ValidateEmptyInput(input=newProfile.Title):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your title changed to: ", newProfile.Title)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                    
                    if terminateOperation:
                        break

                # update about
                elif decision == 2:
                    while True:
                        try:
                            print("\nPlease enter a new about section")
                            newProfile.About = MenuHelper.InputStream()
                            if about == "-1":
                                terminateOperation = True
                                break
                            if MenuHelper.ValidateEmptyInput(input=newProfile.About):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your about section changed to: ", newProfile.About)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                    
                    if terminateOperation:
                        break
                
                # update gender
                elif decision == 3:
                    while True:
                        try:
                            print("\nPlease enter a new gender")
                            newProfile.Gender = MenuHelper.InputStream()
                            if gender == "-1":
                                terminateOperation = True
                                break
                            if MenuHelper.ValidateEmptyInput(input=newProfile.Gender):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your gender changed to: ", newProfile.Gender)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                    
                    if terminateOperation:
                        break

                # update ethnicity
                elif decision == 4:
                    while True:
                        try:
                            print("\nPlease enter a new ethnicity")
                            newProfile.Ethnicity = MenuHelper.InputStream()
                            if ethnicity == "-1":
                                terminateOperation = True
                                break
                            if MenuHelper.ValidateEmptyInput(input=newProfile.Ethnicity):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your ethnicity changed to: ", newProfile.Ethnicity)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                    
                    if terminateOperation:
                        break
                
                # update disability status
                elif decision == 5:
                    while True:
                        try:
                            print("\nPlease enter a new disability status")
                            newProfile.DisabilityStatus = MenuHelper.InputStream()
                            if disabilityStatus == "-1":
                                terminateOperation = True
                                break
                            if MenuHelper.ValidateEmptyInput(input=newProfile.DisabilityStatus):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your disability status changed to: ", newProfile.DisabilityStatus)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                    
                    if terminateOperation:
                        break
                
                # update location
                elif decision == 6:
                    while True:
                        try:
                            print("\nPlease enter a new location")
                            newProfile.Location = MenuHelper.InputStream()
                            if location == "-1":
                                terminateOperation = True
                                break
                            if MenuHelper.ValidateEmptyInput(input=newProfile.Location):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your location changed to: ", newProfile.Location)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                    
                    if terminateOperation:
                        break
                
                # update phone number
                elif decision == 7:
                    while True:
                        try:
                            print("\nPlease enter a new phone number")
                            newProfile.PhoneNumber = MenuHelper.InputStream()
                            if phoneNumber == "-1":
                                terminateOperation = True
                                break
                            if MenuHelper.ValidateEmptyInput(input=newProfile.PhoneNumber):
                                MenuHelper.WarnInvalidInput()
                                continue
                            print("Success! Your phone number changed to: ", newProfile.PhoneNumber)
                            break
                        except:
                            MenuHelper.WarnInvalidInput()
                    
                    if terminateOperation:
                        break

                # update education
                elif decision == 8:
                    while True:
                        try:
                            # TODO: MODIFY THE EDUCAION LIST SECTION INPUT CHANGE
                            # print("\nPlease enter a new education")
                            # ethnicity = MenuHelper.InputStream()
                            # if ethnicity == "-1":
                            #     terminateOperation = True
                            #     break
                            # if MenuHelper.ValidateEmptyInput(input=ethnicity):
                            #     MenuHelper.WarnInvalidInput()
                            #     continue
                            # print("Success! Your ethnicity changed to: ", ethnicity)
                            # break
                            pass
                        except:
                            MenuHelper.WarnInvalidInput()
                    
                    if terminateOperation:
                        break

                # update experience
                elif decision == 9:
                    while True:
                        try:
                            # TODO: MODIFY THE EXPERIENCE LIST SECTION INPUT CHANGE
                            # print("\nPlease enter a new ethnicity")
                            # ethnicity = MenuHelper.InputStream()
                            # if ethnicity == "-1":
                            #     terminateOperation = True
                            #     break
                            # if MenuHelper.ValidateEmptyInput(input=ethnicity):
                            #     MenuHelper.WarnInvalidInput()
                            #     continue
                            # print("Success! Your ethnicity changed to: ", ethnicity)
                            # break
                            pass
                        except:
                            MenuHelper.WarnInvalidInput()
                    
                    if terminateOperation:
                        break
                
                elif decision == -1:
                    terminateOperation = True
                    break
            
            except Exception as e:
                MenuHelper.WarnInvalidInput()

        if terminateOperation:
            if userHasProfile:
                # TODO: RETURN THE APPLICANT PROFILE CREATED FROM DB ACTION
                pass
            else:
                return None
        
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