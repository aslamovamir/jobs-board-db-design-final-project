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
    About: str
    Location: str
    Industry: str
    ServiceType: str
    CompanyType: str
    AnnualRevenue: str
    EmployeeSize: int
    FoundationDate: str
    InternationalHires: bool
    Products: list[Product] = field(default_factory=list)

