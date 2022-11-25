from dataclasses import dataclass

# class for MenuHelper
@dataclass
class MenuHelper:

    # helps to print a line to distinguish between different sections in program
    def HelpDefineSectionBreak():
        print("----------------------------------------------------------------------------------------------")
    

    # takes in a list of otions and prints in a formatted way
    def HelpDisplayMenuOptions(options: list[str]):
        i: int = 1
        for option in options:
            print(f"{i} - {option}")
            i += 1

    
    # gives the user general instruction to select a menu option
    def HelpRequestInput():
        print("\nPlease select an option to continue:")

    
    # informs the user that they decided to quit a menu selection
    def HelpInformMenuQuit():
        print("\nYou have selected to Quit.\n")


    # inputs the menu option number from the user
    def HelpInputOption() -> int:
        return int(input("Enter (-1 to Quit): "))

    
    # displays the menu option selected for confirmation purposes
    def HelpDisplaySelectedOption(selectedOption: str):
        print("Selected: ", selectedOption)


    # displays an error message that entered input is invalid
    def HelpWarnInvalidInput():
        print("\nError! Invalid Entry! Please try again.")

    
    # prints an error message in case of exceptions and displays those exceptions
    def HelpDisplayErrorException(exception: str):
        print(f"\nFailure! Something went wrong for some reason. Please address the following exception: {exception}")

    
    # prints the copyright information
    def HelpDisplayCopyright():
        print("\n\nCopyright: © JobsBoard, November 2022.\nAll rights reserved.\nFor any queries, consult author and engineer: Amir Aslamov.\n")