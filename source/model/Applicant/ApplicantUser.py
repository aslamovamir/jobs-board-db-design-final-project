from dataclasses import dataclass, field
from model.Applicant.ApplicantProfile import ApplicantProfile
from model.Applicant.ApplicantModelHelper import ApplicantModelHelper
from datetime import datetime


# general Applicant user entity
@dataclass
class ApplicantUser:
    ID: str
    Username: str
    Email: str
    FirstName: str
    LastName: str
    pk: str = None
    Profile: ApplicantProfile = None
    DateRegistered: datetime = field(default_factory=datetime.now)
    DateLastLogin: datetime = field(default_factory=datetime.now)

    def __init__(self, Username: str, Password: str, Email: str, FirstName: str, LastName: str) -> None:
        # we never statically store the password of the user for security purposes - instead, we hash password with username
        self.ID = ApplicantModelHelper.CreateApplicantUserId(username=Username, password=Password)
        self.Username = Username
        self.Email = Email
        self.FirstName = FirstName
        self.LastName = LastName