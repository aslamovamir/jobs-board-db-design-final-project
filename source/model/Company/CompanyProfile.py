from dataclasses import dataclass, field


# Company profile entity
@dataclass
class CompanyProfile:
    CompanyID: str
    About: str
    Location: str
    Industry: str
    ServiceType: str
    CompanyType: str
    AnnualRevenue: str
    EmployeeSize: str
    FoundationDate: str
    InternationalHires: str


    # construtor
    def __init__(self, CompanyID: str, About: str, Location: str, Industry: str, ServiceType: str,
        CompanyType: str, AnnualRevenue: str, EmployeeSize: str, FoundationDate: str, InternationalHires: str) -> None:
        
        self.CompanyID = CompanyID
        self.About = About
        self.Location = Location
        self.Industry = Industry
        self.ServiceType = ServiceType
        self.CompanyType = CompanyType
        self.AnnualRevenue = AnnualRevenue
        self.EmployeeSize = EmployeeSize
        self.FoundationDate = FoundationDate
        self.InternationalHires = InternationalHires