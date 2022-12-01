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
        print("Your title: ", userProfile.Title)
        print("Your about: ", userProfile.About)
        print("Your gender: ", userProfile.Gender)
        print("Your ethnicity: ", userProfile.Ethnicity)
        print("Your disability status: ", userProfile.DisabilityStatus)
        print("Your location: ", userProfile.Location)
        print("Your phone number: ", userProfile.PhoneNumber)

        MenuHelper.DefineSectionBreak()

    
    # method to display an applicant's profile to a company user
    def DisplayApplicantProfileToCompany(applicantUser: ApplicantUser):
        # first retrive the user's profile from the database
        try:
            userProfile: ApplicantProfile = ApplicantUserDBActions.RetrieveProfile(loggedUser=applicantUser)
        except Exception as e:
            MenuHelper.DisplayErrorException(exception=e, errorSource="DisplayApplicantProfileInfo::RetrieveProfile")
        
        # now we can display the profile
        MenuHelper.DefineSectionBreak()

        print("The applicant's profile information:\n")
        print("Title: ", userProfile.Title)
        print("About: ", userProfile.About)
        print("Gender: ", userProfile.Gender)
        print("Ethnicity: ", userProfile.Ethnicity)
        print("Disability status: ", userProfile.DisabilityStatus)
        print("Location: ", userProfile.Location)
        print("Phone number: ", userProfile.PhoneNumber)

        MenuHelper.DefineSectionBreak()


    # method to retrieve and display company user profile
    def DisplayCompanyProfile(loggedUser: CompanyUser):
        # first retrive the user's profile from the database
        try:
            userProfile: CompanyProfile = CompanyUserDBActions.RetrieveProfile(companyUsername=loggedUser.Username)
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

    
    # method to retrieve and display company user profile provided
    def DisplayCompanyProfileProvided(profile: CompanyProfile):
        
        # now we can display the profile
        MenuHelper.DefineSectionBreak()

        print("The company profile information:\n")
        print("About: ", profile.About)
        print("Location: ", profile.Location)
        print("Industry: ", profile.Industry)
        print("Service Type: ", profile.ServiceType)
        print("Company Type: ", profile.CompanyType)
        print("Annual Revenue: ", profile.AnnualRevenue)
        print("Employee Size: ", profile.EmployeeSize)
        print("Foundation Date: ", profile.FoundationDate)
        print("International Hires: ", profile.InternationalHires)

        MenuHelper.DefineSectionBreak()