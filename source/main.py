from helpers.MenuHelper import MenuHelper
from actions.DisplayAboutApp import DisplayAboutApp


# this is the main run file
class Main:
    
    # basic introduction
    MenuHelper.HelpDefineSectionBreak()
    print("\nWelcome to JobsBoard!",
        "\n\nJobsBoard is a commercial application designed to serve 2 types of players in the job market:\n",
        "1) Applicants\n 2) Companies.\n\nWe do recognize the trouble of finding jobs at the right company",
        " and the trouble of finding\nthe right job candidate for job openings. Therefore, JobsBoard helps ",
        "faciliate this \ninterconnection between the right job candidate and the right company.")
    # copyright
    MenuHelper.HelpDisplayCopyright()
    MenuHelper.HelpDefineSectionBreak()

    # entry
    print("\nWelcome to JobsBoard!")
    while True:
        try:
            MenuHelper.HelpRequestInput()

            # menu options for the user
            menuOptions: list[str] = [
                "About JobsBoard",
                "Log In",
                "Sign Up",]

            # display menu options to the user
            MenuHelper.HelpDisplayMenuOptions(menuOptions)

            # take in the menu option entered
            decision: int = MenuHelper.HelpInputOption()

            # check the menu option selected and redirect the user correspondignly
            if decision == 1:
                MenuHelper.HelpDisplaySelectedOption(selectedOption=menuOptions[decision-1])
                DisplayAboutApp()
            
            elif decision == 2:
                MenuHelper.HelpDisplaySelectedOption(selectedOption=menuOptions[decision-1])
            
            elif decision == 3:
                MenuHelper.HelpDisplaySelectedOption(selectedOption=menuOptions[decision-1])
            
            elif decision == -1:
                MenuHelper.HelpInformMenuQuit()
                break

            else:
                MenuHelper.HelpWarnInvalidInput()
        
        except Exception as e:
            MenuHelper.HelpWarnInvalidInput()
