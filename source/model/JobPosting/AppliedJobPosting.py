from dataclasses import dataclass, field
from datetime import datetime


# applied job entity
@dataclass
class AppliedJob:
    pk: str
    ID: str
    JobPostingID: str
    CompanyID: str
    ApplicantID: str
    Status: str
    DateApplied: datetime = field(default_factory=datetime.now)