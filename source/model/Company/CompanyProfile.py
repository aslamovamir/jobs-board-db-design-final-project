from dataclasses import dataclass, field
from datetime import datetime



# class for Product
@dataclass
class Product:
    ProductName: str
    About: str
    MarketPrice: str
    ApplicationUse: str


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
    Products: list[Product] = field(default_factory=list)


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