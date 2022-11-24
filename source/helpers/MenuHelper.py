from dataclasses import dataclass

# class for MenuHelper
@dataclass
class MenuHelper:

    # helps to print a line to distinguish between different sections in program
    def HelpDefineSectionBreak():
        print("---------------------------------------------------------------------------------------------")