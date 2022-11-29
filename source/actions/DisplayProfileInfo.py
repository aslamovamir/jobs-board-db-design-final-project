from model.Applicant.ApplicantUser import ApplicantUser
from model.Applicant.ApplicantProfile import ApplicantProfile
from database.ApplicantUserDBActions import ApplicantUserDBActions
from helpers.MenuHelper import MenuHelper


class DisplayProfileInfo:

    # method to retrieve and display applicant user profile
    def DisplayApplicantProfile(loggedUser: ApplicantUser):
        # first retrive the user's profile from the database
        try:
            userProfile: ApplicantProfile = ApplicantUserDBActions.RetrieveProfile(loggedUser=loggedUser)
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="DisplayProfileInfo::RetrieveProfile")
        
        # now we can display the profile
        MenuHelper.DefineSectionBreak()

        print("Your profile information:\n")
        print("Your Title: ", userProfile.Title)
        print("Your About: ", userProfile.About)
        print("Your gender: ", userProfile.Gender)
        print("Your ethnicity: ", userProfile.Ethnicity)
        print("Your disability status: ", userProfile.DisabilityStatus)
        print("Your location: ", userProfile.Location)
        print("Your phone number: ", userProfile.PhoneNumber)
        # TODO DIPLAY EDUCATION AND EXPERIENCE LIST TOO

        MenuHelper.DefineSectionBreak()