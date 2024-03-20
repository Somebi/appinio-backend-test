# Internal
from typing import List

# Installed dependencies
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# App imports
from module.db.models.summary import Summary

def create(db: Session, id: str, summary: str, original: str, created_at: str) -> Summary:
    try:
        new_summary = Summary(id=id, summary=summary, original=original, created_at=created_at)
        db.add(new_summary)
        db.commit()
        return new_summary
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def read(db: Session) -> List[Summary]:
    return db.query(Summary).order_by(Summary.created_at.desc()).all()

