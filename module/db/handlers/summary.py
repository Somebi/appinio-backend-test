# Internal
from typing import List

# Installed dependencies
from sqlalchemy.orm import Session

# App imports
from module.db.models.summary import Summary

def create(db: Session, id: str, summary: str, original: str, created_at: str) -> Summary:
    new_summary = Summary(id=id, summary=summary, original=original, created_at=created_at)
    db.add(new_summary)
    db.commit()
    return new_summary

def read(db: Session) -> List[Summary]:
    return db.query(Summary).order_by(Summary.created_at.desc()).all()

