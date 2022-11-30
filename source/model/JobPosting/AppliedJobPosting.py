from dataclasses import dataclass, field
from datetime import datetime
from model.JobPosting.JobPostingModelHelper import JobPostingModelHelper


# applied job entity
@dataclass
class AppliedJob:
    pk: str
    ID: str
    JobPostingID: str
    CompanyID: str
    ApplicantID: str
    Status: str
    StartDate: str
    GoodFitExplanation: str
    SponsorshipRequirement: str
    DateApplied: datetime = field(default_factory=datetime.now)

    def __init__(self, JobPostingID: str, CompanyID: str, ApplicantID: str, Status: str, StartDate: str,
        GoodFitExplanation: str, SponsorshipRequirement: str, DateApplied: str) -> None:
        
        self.ID = JobPostingModelHelper.CreateAppliedJobId(jobPostingID=JobPostingID, companyID=CompanyID, applicantID=ApplicantID)
        self.JobPostingID = JobPostingID
        self.CompanyID = CompanyID
        self.ApplicantID = ApplicantID
        self.Status = Status
        self.StartDate = StartDate
        self.GoodFitExplanation = GoodFitExplanation
        self.SponsorshipRequirement = SponsorshipRequirement
        self.DateApplied = DateApplied