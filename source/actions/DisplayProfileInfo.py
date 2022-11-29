from model.Applicant.ApplicantUser import ApplicantUser
from model.Applicant.ApplicantProfile import ApplicantProfile
from model.Company.CompanyUser import CompanyUser
from model.Company.CompanyProfile import CompanyProfile
from database.ApplicantUserDBActions import ApplicantUserDBActions
from database.CompanyUserDBActions import CompanyUserDBActions
from helpers.MenuHelper import MenuHelper


class DisplayProfileInfo:

    # method to retrieve and display applicant user profile
    def DisplayApplicantProfile(loggedUser: ApplicantUser):
        # first retrive the user's profile from the database
        try:
            userProfile: ApplicantProfile = ApplicantUserDBActions.RetrieveProfile(loggedUser=loggedUser)
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="DisplayApplicantProfileInfo::RetrieveProfile")
        
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

        MenuHelper.DefineSectionBreak()


    # method to retrieve and display company user profile
    def DisplayCompanyProfile(loggedUser: CompanyUser):
        # first retrive the user's profile from the database
        try:
            userProfile: CompanyProfile = CompanyUserDBActions.RetrieveProfile(loggedUser=loggedUser)
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="DisplayCompanyProfileInfo::RetrieveProfile")
        
        # now we can display the profile
        MenuHelper.DefineSectionBreak()

        print("The company profile information:\n")
        print("About: ", userProfile.About)
        print("Location: ", userProfile.Location)
        print("Industry: ", userProfile.Industry)
        print("Service Type: ", userProfile.ServiceType)
        print("Company Type: ", userProfile.CompanyType)
        print("Annual Revenue: ", userProfile.AnnualRevenue)
        print("Employee Size: ", userProfile.EmployeeSize)
        print("Foundation Date: ", userProfile.FoundationDate)
        print("International Hires: ", userProfile.InternationalHires)

        MenuHelper.DefineSectionBreak()