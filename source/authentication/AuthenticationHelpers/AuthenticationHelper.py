

class AuthenticationHelper:
    
    # this method will validate the password
    def ValidatePassword(password: str) -> bool:
        checkLength = False
        checkUpperCase = False
        checkDigit = False
        checkSpecialCharacter = False
        if len(password) >= 8 and len(password) <= 12:
            checkLength = True

        for charCheck in password:
            if charCheck.isupper():
                checkUpperCase = True
            elif charCheck.isdigit():
                checkDigit = True
            elif charCheck.islower() == False:
                checkSpecialCharacter = True
        
        if checkDigit and checkLength and checkSpecialCharacter and checkUpperCase:
            return True
        else:
            return False

    
    # this method will validate the email address
    def ValidateEmail(email: str) -> bool:
        try:
            if len(email) == 0:
                return False
            
            split: str = email.split('@')
            print(split)
            

            return True
        
        except:
            return False

