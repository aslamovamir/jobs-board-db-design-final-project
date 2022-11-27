from dataclasses import dataclass, field
from model.Company.CompanyModelHelper import CompanyModelHelper
from  model.Company.CompanyProfile import CompanyProfile
from datetime import datetime


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


    # constructor
    def __init__(self, Username: str, Password: str, Email: str, CompanyName: str) -> None:
        # we never statically store the password of the user for security purposes - 
        # instead, we hash password with username and pass to ID
        self.ID = CompanyModelHelper.CreateCompanyUserId(username=Username, password=Password)
        
        self.Username = Username
        self.Email = Email
        self.CompanyName = CompanyName