from dataclasses import dataclass
from model.Interview.InterviewModelHelper import InterviewModelHelper


# class for interview
@dataclass
class Interview:
    pk: str
    ID: str
    CompanyID: str
    ApplicantID: str
    JobPostingID: str
    Location: str
    MeetingTime: str


    # constructor
    def __init__(self, CompanyID: str, ApplicantID: str, JobPostingID: str, Location: str, MeetingTime: str) -> None:
        self.ID = InterviewModelHelper.CreateInterviewId(companyID=CompanyID, applicantID=ApplicantID)
        self.CompanyID = CompanyID
        self.ApplicantID = ApplicantID
        self.JobPostingID = JobPostingID
        self.Location = Location
        self.MeetingTime = MeetingTime