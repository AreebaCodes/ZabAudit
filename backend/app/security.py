from passlib.context import CryptContext

#MAKING CONTEXT OBJECT FOR PASSWORD HASHING
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#DEFINING FUNCTIONS FOR PASSWORD ENCRYPTION
#FIRST FUNCTION FOR HASHING PASSWORD
def hash_password(password:str):
    hashed_password=pwd_context.hash(password)  #HASHING WILL MAKE PASSWORD MORE SECURE AND ITS BETTER THAN ENCRYPTION
    return hashed_password

#2ND FUNCTION FOR VERIFYING PASSWORD
def verify_password(plain_password:str,hashed_password:str):
    verify_pass=pwd_context.verify(plain_password,hashed_password) #VERIFICATION
    return verify_pass