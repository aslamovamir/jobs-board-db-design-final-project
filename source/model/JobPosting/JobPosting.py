from dataclasses import dataclass
from model.JobPosting.JobPostingModelHelper import JobPostingModelHelper

# job posting entity
@dataclass
class JobPosting:
    pk: str
    ID: str
    CompanyID: str
    PositionName: str
    Pay: str
    Location: str
    Description: str
    Department: str

    # constructor
    def __init__(self, CompanyID: str, PositionName: str, 
        Pay: str, Location: str, Description: str, Department: str) -> None:
        
        self.ID = JobPostingModelHelper.CreateJobPostingId(companyID=CompanyID)
        self.CompanyID = CompanyID
        self.PositionName = PositionName
        self.Pay = Pay
        self.Location = Location
        self.Description = Description
        self.Department = Department