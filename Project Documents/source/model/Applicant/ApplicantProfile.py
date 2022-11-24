from dataclasses import dataclass, field


# class for Experience
@dataclass
class Experience:
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
    SchoolName: str
    Degree: str
    YearsAttended: int
    Location: str
    Major: str
    GPA: str


# Applicant profile entity
@dataclass
class ApplicantProfile:
    Title: str
    About: str
    Gender: str
    Ethnicity: str
    DisabilityStatus: str
    Location: str
    PhoneNumber: str
    EducationList: list[Education] = field(default_factory=list)
    ExperienceList: list[Experience] = field(default_factory=list)