from dataclasses import dataclass
import hashlib


@dataclass
class CompanyModelHelper:

    # helper method to create a user id encrypted for the CompanyUser class
    def CreateCompanyUserId(username: str, password: str) -> str:
        return hashlib.sha256(str.encode(username.join(password))).hexdigest()