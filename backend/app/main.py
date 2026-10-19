from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  #CORS ARE ESSENTIAL FOR CONNECTING FRONTEND AND BACKEND PROPERLY
from .database import engine,Base  
from .models import PM,Student
from .routes import pm,student #ROUTE INCLUDE KR RAHEE


#CREATING TABLES IN POSTGRESQL
Base.metadata.create_all(bind=engine)
#CREATING AN APP INSTANCE OF FASTAPI
app=FastAPI()

#MIDDLEWARE ROUTE FOR BACKEND ONLY
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], #BACKEND KA PORT
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#INCLUDING ROUTERS
app.include_router(pm.router) #PM K SAARE ROUTES INCLUDE 
app.include_router(student.router) #STUDENTS K SAARE ROUTES INCLUDE HOJAYENGAI
#TEST ROUTE
@app.get("/")
def read_root():
    return {"message": "ZabAudit backend running"}