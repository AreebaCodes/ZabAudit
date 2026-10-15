#IMPORTING ESSENTIAL LIBRARIES
from pydantic import BaseModel,EmailStr
from typing import List
from pydantic import Field,field_validator

#MAKING STUDENT SIGNUP FORM SCHEMA
class StudentSignup(BaseModel):
    name:str=Field(min_length=3)
    email:EmailStr #EMAIL PROVIDED BY SZABIST TO THEIR STUDENTS
    password:str=Field(min_length=8,max_length=16)
    program:str=Field(min_length=3,description="DEGREE NAME LIKE CS BBA BSAI")
    reg_no:str=Field(min_length=7)  #SZABIST REGNUM LIKE 2312393 7 DIGIT REG NO
    #EMAIL VALIDATION METHOD FOR SZABIST STUDENTS
    @field_validator("email") #DECORATOR
    @classmethod #IS CLASS KA METHOD TAAKE CLS USE KRSAKHE
    def validate_email(cls,value):
        lower_value=value.lower()
        if not lower_value.endswith("@szabist.pk"): #CONDITION IS CHECKED
            raise ValueError("SZABIST STUDENT EMAIL MUST BE END WITH @SZABIST.PK")
        return lower_value


#MAKING STUDENT LOGIN FORM SCHEMA
class StudentLogin(BaseModel):
    email:EmailStr
    password:str=Field(min_length=8,max_length=16)