from dataclasses import dataclass

# job posting entity
@dataclass
class JobPosting:
    pk: str
    CompanyID: str
    PositionName: str
    Pay: str
    Location: str
    Description: str
    Department: str

    # constructor
    def __init__(self, CompanyID: str, PositionName: str, 
        Pay: str, Location: str, Description: str, Department: str) -> None:
        
        self.CompanyID = CompanyID
        self.PositionName = PositionName
        self.Pay = Pay
        self.Location = Location
        self.Description = Description
        self.Department = Department