# Installed dependencies
from sqlalchemy import DateTime, Column, String
from sqlalchemy.dialects.postgresql import UUID

# App imports
from module.db.base import Base

class Summary(Base):
    __tablename__ = 'summary'
    id = Column(UUID(as_uuid=True), primary_key=True)
    summary = Column(String)
    original = Column(String)
    created_at = Column(DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'summary': self.summary,
            'original': self.original,
            'created_at': self.created_at,
        }
