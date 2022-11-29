from dataclasses import dataclass, field


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