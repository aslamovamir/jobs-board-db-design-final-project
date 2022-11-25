from dataclasses import dataclass, field
from ApplicantProfile import ApplicantProfile
from datetime import datetime


# general Applicant user entity
@dataclass
class ApplicantUser:
    Id: str
    Username: str
    FirstName: str
    LastName: str
    Email: str
    Profile: ApplicantProfile = None
    _lastLoginTimestamp: datetime = field(default_factory=datetime.now)
    _SignUpTimestamp: datetime = field(default_factory=datetime.now)