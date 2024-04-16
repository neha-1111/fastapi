from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import time
from config import settings
from dotenv import load_dotenv
import os
from . import env
SQLALCHEMY_DATABASE_URL='postgresql://{settings.database_username}:{settings.database_password}@{settings.database.hostname}:{settings.database_port}/{settings.database_name}'
engine=create_engine(SQLALCHEMY_DATABASE_URL)
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
base=declarative_base()
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()  