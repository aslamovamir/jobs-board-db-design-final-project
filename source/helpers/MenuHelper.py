

# class for MenuHelper
class MenuHelper:

    # helps to print a line to distinguish between different sections in program
    def DefineSectionBreak():
        print("----------------------------------------------------------------------------------------------")
    

    # takes in a list of otions and prints in a formatted way
    def DisplayMenuOptions(options: list[str]):
        i: int = 1
        for option in options:
            print(f"{i} - {option}")
            i += 1

    
    # gives the user general instruction to select a menu option
    def RequestInput():
        print("\nPlease select an option to continue:")

    
    # informs the user that they decided to quit a menu selection
    def InformMenuQuit():
        print("\nYou have selected to Quit.\n")


    # inputs the menu option number from the user
    def InputOption() -> int:
        return int(input("Enter (-1 to Quit): "))

    
    # displays the menu option selected for confirmation purposes
    def DisplaySelectedOption(selectedOption: str):
        print("Selected: ", selectedOption)


    # displays an error message that entered input is invalid
    def WarnInvalidInput():
        print("\nError! Invalid Entry! Please try again.")

    
    # prints an error message in case of exceptions and displays those exceptions
    def DisplayErrorException(exception: str):
        print(f"\nFailure! Something went wrong for some reason. Please address the following exception: {exception}")

    
    # prints the copyright information
    def DisplayCopyright():
        print("\n\nCopyright: © JobsBoard, November 2022.\nAll rights reserved.\nFor any queries, consult author and engineer: Amir Aslamov.\n")