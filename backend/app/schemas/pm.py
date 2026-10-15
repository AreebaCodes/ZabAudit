from pydantic import BaseModel,EmailStr
from typing import Annotated,List
from pydantic import Field
#MAKING PROGRAM MANAGER SIGNUP FORM SCHEMA
class PMSignup(BaseModel):
    name:str=Field(min_length=3,description="Program Manager Name")
    email:EmailStr  #EMAILSTR VALIDATION
    password:str=Field(min_length=8,max_length=16)
    program:str=Field(min_length=3)
    year:int

#MAKING PROGRAM MANAGER LOGIN FORM SCHEMA
class PMLogin(BaseModel):
    email:EmailStr
    password:str=Field(min_length=8,max_length=16)