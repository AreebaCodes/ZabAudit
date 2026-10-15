#IMPORTING ESSENTIALS LIBRARIES
import os
from dotenv import load_dotenv
import datetime
from jose import jwt,JWTError
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .database import get_db
from .models import PM,Student
#LOAD DOTENV 
load_dotenv()
#CREATING 3 CONSTANTS VARIABLES WHICH ARE ESSENTIAL IN JWT
Secret_key=os.getenv("Database_url")
Algo="HS256"  #HASHING ALOGIRTHM WIDELY USED
TOKEN_EXPIRE_MINUTES=60

#WORK WILL BE CONTINUE...................