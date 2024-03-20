# Internal
import os

# Installed dependencies
from flask import Flask, g
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRESQL_URL = os.getenv('POSTGRESQL_URL', '')

# Database connection (SQLite in-memory database for simplicity)
engine = create_engine(POSTGRESQL_URL, echo=True)
session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def db_session_handler(app: Flask):

    @app.before_request
    def start_session():
        # Create a new session (bound to the specific request)
        g.db_session = session_maker()

    @app.teardown_appcontext
    def shutdown_session(response_or_exc):
        # Close the session at the end of the request, ensuring cleanup
        db_session = g.pop('db_session', None)
        if db_session is not None:
            db_session.close()
