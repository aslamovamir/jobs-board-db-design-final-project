import hashlib


# class for the interview model helper
class InterviewModelHelper:

    # helper method to create a job posting id encrypted for the JobPosting class
    def CreateInterviewId(companyID: str, applicantID: str) -> str:
        return hashlib.sha256(str.encode(companyID.join(applicantID))).hexdigest()