from pydantic import BaseModel,EmailStr
from typing import Annotated,List
from pydantic import Field,field_validator
#MAKING PROGRAM MANAGER SIGNUP FORM SCHEMA
class PMSignup(BaseModel):
    name:str=Field(min_length=3,description="Program Manager Name")
    email:EmailStr  #EMAILSTR VALIDATION
    password:str=Field(min_length=8,max_length=16)
    program:str=Field(min_length=3)
    year:int
    #EMAIL VALIDATION FOR SZABIST PROGRAM MANAGER
    @field_validator("email") #DECORATOR
    @classmethod #DECORATOR
    def validate_email(cls,value):  #THIS WILL CHECK IF PROGRAM MANAGER EMAIL ENDS WITH @szabist.edu.pk
        value_lower=value.lower() #EMAIL BY DEFAULT LOWER MAI HOTI HY BUT STILL SAFETY K LIYEE
        if  not value_lower.endswith(("@szabist.edu.pk","@szabist.pk")):#condition for szabist program manager
            raise ValueError("Program Manager email should end with @szabist.edu.pk or @szabist.pk")
        return value_lower

#MAKING PROGRAM MANAGER LOGIN FORM SCHEMA
class PMLogin(BaseModel):
    email:EmailStr
    password:str=Field(min_length=8,max_length=16)