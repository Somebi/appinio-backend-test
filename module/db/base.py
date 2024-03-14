# Internal
import os

# Installed dependencies
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRESQL_URL = os.getenv('POSTGRESQL_URL', '')

# Database connection (SQLite in-memory database for simplicity)
engine = create_engine(POSTGRESQL_URL, echo=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
