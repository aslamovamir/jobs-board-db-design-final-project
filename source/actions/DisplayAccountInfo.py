from model.Applicant.ApplicantUser import ApplicantUser
from model.Company.CompanyUser import CompanyUser
from helpers.MenuHelper import MenuHelper


# class for DisplayAccountInfo
class DisplayAccountInfo:

    # method to print applicant user info
    def DisplayApplicantInfo(loggedUser: ApplicantUser):
        MenuHelper.DefineSectionBreak()

        print("Your account information:\n")
        print("Your username: ", loggedUser.Username)
        print("Your email: ", loggedUser.Email)
        print("Your first name: ", loggedUser.FirstName)
        print("Your last name: ", loggedUser.LastName)
        print("The date you registered: ", loggedUser.DateRegistered)
        print("The last time you logged in: ", loggedUser.DateLastLogin)

        MenuHelper.DefineSectionBreak()


    # method to print company user info
    def DisplayCompanyInfo(loggedUser: CompanyUser):
        MenuHelper.DefineSectionBreak()

        print("Company account information:\n")
        print("Company username: ", loggedUser.Username)
        print("Company email: ", loggedUser.Email)
        print("Company name: ", loggedUser.CompanyName)
        print("The date company registered: ", loggedUser.DateRegistered)
        print("The last time company logged in: ", loggedUser.DateLastLogin)

        MenuHelper.DefineSectionBreak()
