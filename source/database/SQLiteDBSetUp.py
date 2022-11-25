import sqlite3
from dataclasses import dataclass
from model.Applicant.ApplicantUser import ApplicantUser
from model.Applicant.ApplicantProfile import ApplicantProfile
from model.Company.CompanyUser import CompanyUser
from model.Company.CompanyProfile import CompanyProfile


#NOTE: Methods of this class must be run only once: they are run when running the app for
# the first time internally by developers to set up the database and the neceassary tables 

# class for the database set-up
@dataclass
class DatabaseSetUp:

    # method to create an SQL table for the ApplicantUser entity
    def CreateApplicantUserTable(applicantUser: ApplicantUser) -> bool:
        pass

    # method to create an SQL table for the ApplicantProfile entity
    def CreateApplicantProfileTable(applicantProfile: ApplicantProfile) -> bool:
        pass

    # method to create an SQL table for the CompanyUser entity
    def CreateCompanyUserTable(companyUser: CompanyUser) -> bool:
        pass

    # method to create an SQL table for the CompanyProfile entity
    def CreateCompanyProfileTable(companyProfile: CompanyProfile) -> bool:
        pass

