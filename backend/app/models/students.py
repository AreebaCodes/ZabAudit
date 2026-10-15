from sqlalchemy import Column,Integer,String
from ..database import Base

class Student(Base):
    __tablename__="students"  #TABLE NAME IN DATABASE
    id=Column(Integer,primary_key=True,index=True)
    reg_no=Column(String,nullable=False,unique=True,index=True) #SZABIST PROVIDED ID bscs2312129
    name=Column(String,nullable=False)
    program=Column(String,nullable=False) #THE PROGRAM IN WHICH HE/SHE WAS ENROLLED
    email=Column(String,unique=True,nullable=False) #SZABIST PROVIDE UNIQUE EMAIL TO EACH STUDENT
    password_hash=Column(String,nullable=False)
