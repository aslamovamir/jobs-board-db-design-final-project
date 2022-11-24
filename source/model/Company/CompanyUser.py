from dataclasses import dataclass, field
from datetime import datetime
from CompanyProfile import CompanyProfile


# general Company user entity
@dataclass
class CompanyUser:
    Id: str
    Username: str
    CompanyName: str
    Email: str
    DateRegistered: str
    Profile: CompanyProfile = None
    _lastLoginTimestamp: datetime = field(default_factory=datetime.now)
    _SignUpTimestamp: datetime = field(default_factory=datetime.now)