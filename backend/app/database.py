from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv
#BUILDING UP DATABASE STEPUP - POSTGRESQL
load_dotenv()
db_connection=os.getenv("Database_url") #IMPORTING DB URL FROM .ENV FILE

#ENGINE SETUP
engine=create_engine(db_connection)
#SESSION SETUP
local_session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
#BASE SETUP
Base=declarative_base()
#SETTING UP DATABASE CONNECTION
def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()

