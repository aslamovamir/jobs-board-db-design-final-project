import hashlib


# class for JobPostingModelHelper
class JobPostingModelHelper:

    # helper method to create a job posting id encrypted for the JobPosting class
    def CreateJobPostingId(companyID: str, positionName: str) -> str:
        return hashlib.sha256(str.encode(companyID.join(positionName))).hexdigest()

    
    # helper method to create a job posting id encrypted for the AppliedJob class
    def CreateAppliedJobId(jobPostingID: str, companyID: str, applicantID: str) -> str:
        return hashlib.sha256(str.encode(jobPostingID.join(companyID).join(applicantID))).hexdigest()