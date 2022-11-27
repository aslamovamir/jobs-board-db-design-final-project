from helpers.MenuHelper import MenuHelper
from actions.DisplayAboutApp import DisplayAboutApp
from authentication.Signup import Signup
from authentication.Signin import Signin


# this is the main run file
class Main:
    
    # basic introduction
    MenuHelper.DefineSectionBreak()
    print("\nWelcome to JobsBoard!",
        "\n\nJobsBoard is a commercial application designed to serve 2 types of players in the job market:\n",
        "1) Applicants\n 2) Companies.\n\nWe do recognize the trouble of finding jobs at the right company",
        " and the trouble of finding\nthe right job candidate for job openings. Therefore, JobsBoard helps ",
        "faciliate this \ninterconnection between the right job candidate and the right company.")
    # copyright
    MenuHelper.DisplayCopyright()
    MenuHelper.DefineSectionBreak()

    # entry
    print("\nWelcome to JobsBoard!")
    while True:
        try:
            # menu options for the user
            menuOptions: list[str] = [
                "About JobsBoard",
                "Log In",
                "Sign Up",]

            MenuHelper.RequestInput()
            # display menu options to the user
            MenuHelper.DisplayMenuOptions(menuOptions)

            # take in the menu option entered
            decision: int = MenuHelper.InputOption()

            # check the menu option selected and redirect the user correspondignly
            if decision == 1:
                MenuHelper.DisplaySelectedOption(selectedOption=menuOptions[decision-1])
                DisplayAboutApp()
            
            elif decision == 2:
                MenuHelper.DisplaySelectedOption(selectedOption=menuOptions[decision-1])
                Signin.Signin()
            
            elif decision == 3:
                MenuHelper.DisplaySelectedOption(selectedOption=menuOptions[decision-1])
                Signup.SignUp()
            
            elif decision == -1:
                MenuHelper.InformMenuQuit()
                break

            else:
                MenuHelper.WarnInvalidInput()
        
        except Exception as e:
            MenuHelper.WarnInvalidInput()
