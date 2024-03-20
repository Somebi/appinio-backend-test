# App imports
from .api import init
from .services.summary import SummaryService
from .db.base import db_session_handler, engine, Base

# Installed dependencies
from flask import Flask

# Init db
Base.metadata.create_all(bind=engine)

# Create summary service instance
summary_service = SummaryService()

# Create api service instance
app = Flask(__name__)

# Attach pre-dispatch and post-dispatch hooks to properly handle db session lifecycle via factory
db_session_handler(app=app)

# Start REST server, using summary service
app = init(app=app, summary_service=summary_service)

if __name__ == '__main__':
    app.run()


