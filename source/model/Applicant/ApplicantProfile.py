from dataclasses import dataclass, field


# class for Experience
@dataclass
class Experience:
    ApplicantID: str
    Title: str
    Employer: str
    DateStarted: str
    DateEnded: str
    Location: str
    Description: str
    Industry: str


# class for Education
@dataclass
class Education:
    ApplicantID: str
    SchoolName: str
    Degree: str
    YearsAttended: int
    Location: str
    Major: str
    GPA: str


# Applicant profile entity
@dataclass
class ApplicantProfile:
    ApplicantID: str
    Title: str
    About: str
    Gender: str
    Ethnicity: str
    DisabilityStatus: str
    Location: str
    PhoneNumber: str
    EducationList: list[Education] = field(default_factory=list)
    ExperienceList: list[Experience] = field(default_factory=list)


    # constructor
    def __init__(self, ApplicantID: str, Title: str, About: str, Gender: str, Ethnicity: str,
        DisabilityStatus: str, Location: str, PhoneNumber: str) -> None:
        self.ApplicantID = ApplicantID
        self.Title = Title
        self.About = About
        self.Gender = Gender
        self.Ethnicity = Ethnicity
        self.DisabilityStatus = DisabilityStatus
        self.Location = Location
        self.PhoneNumber = PhoneNumber