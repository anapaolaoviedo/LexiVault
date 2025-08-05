# app/database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# enviroment variables from .env
load_dotenv()

# connecting to PostgreSQL
#format: "postgresql://user:password@host:port/dbname"
DATABASE_URL = os.getenv("DATABASE_URL")

# check if the DATABASE_URL is set, if not, raise an error
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in environment variables. Please create a .env file.")

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

def get_db():
    """
    A dependency function to provide a database session to FastAPI endpoints.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Note: the `engine` and `sessionLocal` are used to interact with the database,
# while the `Base` is used to define the structure of our tables in `models.py`
