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