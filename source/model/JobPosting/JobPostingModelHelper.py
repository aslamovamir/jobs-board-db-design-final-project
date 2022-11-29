import hashlib
from datetime import datetime


# class for JobPostingModelHelper
class JobPostingModelHelper:

    # helper method to create a job posting id encrypted for the JobPosting class
    def CreateJobPostingId(companyID: str) -> str:
        return hashlib.sha256(str.encode(companyID.join(datetime.now()))).hexdigest()