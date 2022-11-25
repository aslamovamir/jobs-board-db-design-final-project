from dataclasses import dataclass
import hashlib


# class for the ApplicantModelHelper
@dataclass
class ApplicantModelHelper:

    # helper method to create a user id encrypted for the ApplicantUser class
    def CreateApplicantUserId(username: str, password: str) -> str:
        return hashlib.sha256(str.encode(username.join(password))).hexdigest()