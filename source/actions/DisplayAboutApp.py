from helpers.MenuHelper import MenuHelper


# displays general information about the JobsBoard app
def DisplayAboutApp():

    MenuHelper.HelpDefineSectionBreak()
    # display general information about the JobsBoard app
    print("\n© JobsBoard is a commercial app designed to help job-seekers to find jobs ",
        "and companies to\nfind job applicants for their job openings. It helps both app ",
        "users efficiently connect with\neach other by centralising the platform of information",
        "exchange based on their respective\nprofiles for potential match, managing the job ",
        "openings, job applications and interview\nschedules.\n")
    
    print("\nUsing © JobsBoard, companies can create job postings with detailed information on the",
        "\nopportunity, manage applicatios for them, review them, and finally connect with them ",
        "for an\ninterview. © JobsBoard helps manage interviews with the favoured applicants. ",
        "For applicants, \n© JobsBoard manages all job postings, and helps applicant users apply for ",
        "them. It also helps\nthem share their profile information with companies, schedule itnerviews ",
        "with the companies\nfavoured.\n")

    # copyright
    MenuHelper.HelpDisplayCopyright()
    MenuHelper.HelpDefineSectionBreak()