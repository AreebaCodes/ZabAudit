#IMPORTING ESSENTIALS LIBRARIES
import os
from dotenv import load_dotenv
from datetime import datetime,timedelta
from jose import jwt,JWTError
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .database import get_db
from .models import PM,Student
#LOAD DOTENV 
load_dotenv()
#CREATING 3 CONSTANTS VARIABLES WHICH ARE ESSENTIAL IN JWT
Secret_key=os.getenv("SECRET_KEY")
Algo="HS256"  #HASHING ALOGIRTHM WIDELY USED
TOKEN_EXPIRE_MINUTES=30 #TOKEN WILL EXPIRE AFTER 30 MINS

#CREATING OAUTH2SCHEMA OBJECT // ESSENTIAL FOR AUTHORIZATION
oauth2_schema=OAuth2PasswordBearer(tokenUrl="pm/login") #JB BH PM LOGIN KREGA YE NEW TOKEN GENERATE KRDEGA

#CREATING ACCESS_TOKEN FUNCTION
def create_access_token(data:dict):
    encoded_data=data.copy() #ORIGINAL DATA PASS NHI KRENGAI
    token_expire_time=datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES) #TOKEN EXPIRATION LOGIC
    encoded_data["exp"]=token_expire_time #SETTING A KEY OF EXP AND ITS VALUE IS TOKEN_EXPIRE_TIME
    return jwt.encode(encoded_data,Secret_key,algorithm=Algo) #JWT KO 3 CHEEZAIN PASS KI JATI


#ACCESS TO CURRENT_USER
def get_current_user(token:str=Depends(oauth2_schema),db:Session=Depends(get_db)):
    try:
        pay_load=jwt.decode(token,Secret_key,algorithms=[Algo]) #THERE IS A LIST OF ALGORITHM NOT A SINGLE ALGORITHM
        email=pay_load.get("sub") #EMAIL GET
        role=pay_load.get("role")  #ROLE EITHER STUDENT OR PM\
    except JWTError:
        raise HTTPException(status_code=401,detail="Token is invalid or it is expired")
    #SEARCHING IN THE DATABASES ON THE BASE OF ROLE
    if role=="PM":
       user= db.query(PM).filter(PM.email==email).first() #JO BH PEHLA MATCHING EMAIL WALA PM MILE
    elif role=="Student":
       user= db.query(Student).filter(Student.email==email).first()
    else:
        raise HTTPException(status_code=401,detail="INVALID ROLE") #AGAR PROGRAM MANAGER YA STUDENT K ILAWA KOI OR ROLE HO
    
     
    if user is None: #AGAR USER HI PRESENT NA HO TW
        raise HTTPException(status_code=401,detail="User not found")

    return user


        


