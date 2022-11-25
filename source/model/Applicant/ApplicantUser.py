from dataclasses import dataclass, field
from ApplicantProfile import ApplicantProfile
from datetime import datetime


# general Applicant user entity
@dataclass
class ApplicantUser:
    pk: str
    ID: str
    Username: str
    Email: str
    FirstName: str
    LastName: str
    Profile: ApplicantProfile = None
    DateRegistered: datetime = field(default_factory=datetime.now)
    DateLastLogin: datetime = field(default_factory=datetime.now)