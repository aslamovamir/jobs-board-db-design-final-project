from helpers.MenuHelper import MenuHelper
# from model.Applicant import ApplicantUser
# from model.Company import CompanyUser


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



    # method to add a new ApplicantUser
    def RegisterNewApplicantUser() -> bool:
        MenuHelper.DefineSectionBreak()
        pass