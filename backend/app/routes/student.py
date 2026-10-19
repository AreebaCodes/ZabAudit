from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from ..import schemas,models #IMPORTING PM MODEL AND SCHEMAS FROM MODELS AND SCHEMAS FOLDER
from ..database import get_db #DB CONNECTION
from ..security import hash_password,verify_password#ENCRYPTION
from ..auth import create_access_token
#ROUTER
router=APIRouter()

#MAKINGE ENDPOINT FOR STUDENT
@router.post("/student/signup")
def student_signup(student_data:schemas.StudentSignup,db:Session=Depends(get_db)):
    #DUPLICATE EMAIL CHECK
    if db.query(models.Student).filter(models.Student.email==student_data.email).first():
         raise HTTPException(status_code=400,detail="EMAIL ALREADY REGISTERED") #2 CONDITIONS CHECK HOGI ISMEIN
    #DUPLICATE REGISTRATION NUMBER CHECK
    if db.query(models.Student).filter(models.Student.reg_no==student_data.reg_no).first():
         raise HTTPException(status_code=400,detail="REGNO ALREADY REGISTERED")
    #NOW HAShing the password for encryption
    hashed_pwd=hash_password(student_data.password)
    #NOW CREATING NEW STUDENT AND COMMITING TO THE DATABASE
    new_student=models.Student(
        reg_no=student_data.reg_no,
        name=student_data.name,
        program=student_data.program,
        email=student_data.email,
        password_hash=hashed_pwd

    )
    db.add(new_student) #SAVING NEW STUDENT IN THE DATABASE
    db.commit()
    db.refresh(new_student)
        #RETURNING JSON RESPONSE
    return {"message": "Student registered successfully", "pm_id": new_student.id}

#LOGIN
@router.post("/student/login")
def student_login(student_login_data:schemas.StudentLogin,db:Session=Depends(get_db)):
    student=db.query(models.PM).filter(models.PM.email==student_login_data.email).first()
    if not student or not verify_password(student_login_data.password,student.password_hash):
            raise HTTPException(status_code=401,detail="Invalid password or email")
    token=create_access_token({"sub":student.email,"role":"Student"})
    return {"access_token":token,"token_type":"bearer","name":student.name}
        