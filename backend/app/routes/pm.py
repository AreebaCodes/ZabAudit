from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from ..import schemas,models #IMPORTING PM MODEL AND SCHEMAS FROM MODELS AND SCHEMAS FOLDER
from ..database import get_db #DB CONNECTION
from ..security import hash_password,verify_password#ENCRYPTION
from ..auth import create_access_token
#ROUTER
router=APIRouter()

#MAKING ENDPOINTS FOR PM
@router.post('/pm/signup')
def pm_signup(pm_data:schemas.PMSignup,db:Session=Depends(get_db)):
    existing = db.query(models.PM).filter(models.PM.email == pm_data.email).first() #CHECKING IF MAIL ALREADU DOESN'T
    if existing:
       raise HTTPException(status_code=400, detail="Email already registered") #CAN'T REGISTER WITH DUPLICATE EMAIL
    #NOW HASHING THE PASSWORD FOR BETTER ENCRYPTION
    hashed_pwd=hash_password(pm_data.password)
    #NOW CREATINGOBJECT
    new_pm=models.PM(
       name=pm_data.name,
       email=pm_data.email,
       password_hash=hashed_pwd,
       program=pm_data.program,
       year=pm_data.year
    )
    #SAVING THE DATA OF NEW PM INTO DATABASE
    db.add(new_pm)
    db.commit()
    db.refresh(new_pm)
    #RETURNING JSON RESPONSE
    return {"message": "PM registered successfully", "pm_id": new_pm.id}

#MAKING A ROUTE FOR PM
@router.post("/pm/login")
def pm_login(login_data:schemas.PMLogin,db:Session=Depends(get_db)):
    pm=db.query(models.PM).filter(models.PM.email==login_data.email).first()
    if not pm or not verify_password(login_data.password,pm.password_hash):
        raise HTTPException(status_code=401,detail="Invalid password or email")
    token=create_access_token({"sub":pm.email,"role":"PM"})
    return {"access_token":token,"token_type":"bearer","name":pm.name}
    
    