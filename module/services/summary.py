# Internal
from datetime import datetime
import logging
import uuid

# Installed
from sqlalchemy.orm import Session

# App code
from module.ai.llm import generate_summary
from module.db.handlers.summary import create, read

class SummaryService():
    def __init__(self, db: Session):
        self.db = db

    def summarize(self, text: str):
        # Perform summarization of incoming text
        logging.info(f'[Summary] performing summary over user provided text: {text}')
        result = generate_summary(text)

        # Create new summary object
        summary = {
            "id": str(uuid.uuid4()),
            "summary": result['output_text'],
            "original": text,
            "created_at": datetime.utcnow()
        }

        # Save it into database
        create(
            self.db,
            **summary
        )

        return summary
    def get_summaries(self):
        results = read(self.db)
        response = []
        for summary in results:
            response.append(summary.to_dict())
        return response
