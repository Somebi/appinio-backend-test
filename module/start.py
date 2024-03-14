# App imports
from module.api import init
from .services.summary import SummaryService
from .db.base import engine, session, Base

# Init db
Base.metadata.create_all(bind=engine)
db = session()

# Create summary service instance
summary_service = SummaryService(db=db)

# Start REST server, using summary service
app = init(summary_service=summary_service)

if __name__ == '__main__':
    app.run()


