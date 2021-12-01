from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.env import DATABASE_URL, DATABASE_LOG
from typing import Dict, Generator


log = True if DATABASE_LOG == 'true' else False

engine = create_engine(
    DATABASE_URL, echo=log,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
