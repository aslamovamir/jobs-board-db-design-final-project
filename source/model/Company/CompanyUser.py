from dataclasses import dataclass, field
from datetime import datetime
from CompanyProfile import CompanyProfile


# general Company user entity
@dataclass
class CompanyUser:
    pk: str
    ID: str
    Username: str
    CompanyName: str
    Email: str
    Profile: CompanyProfile = None
    DateRegistered: datetime = field(default_factory=datetime.now)
    DateLastLogin: datetime = field(default_factory=datetime.now)