# Internal
from datetime import datetime
import logging
import uuid

# Installed
import bleach
from sqlalchemy.orm import Session

# App code
from module.ai.llm import generate_summary
from module.db.handlers.summary import create, read

def sanitize_text(text: str) -> str:
    # Possibly <b>, <strong>, <ul>, <li> tags will be required later
    allowed_tags = []
    allowed_attributes = []

    # Clean the text to strip out all HTML tags except for the allowed ones
    clean_text = bleach.clean(text, tags=allowed_tags, attributes=allowed_attributes, strip=True)

    # Optionally, automatically linkify text and sanitize again to ensure safety
    # Disabled for now, possibly will be required,
    # linkified_text = bleach.linkify(clean_text)

    return clean_text

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
            "summary": sanitize_text(result['output_text']),
            "original": sanitize_text(text),
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
