from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from app.helpers.databaseHandler import Base

class Topics(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    topic = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)