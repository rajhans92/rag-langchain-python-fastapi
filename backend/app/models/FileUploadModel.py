# app/models/fileUploadModel.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime, timezone
from app.helpers.databaseHandler import Base

class FileUpload(Base):
    __tablename__ = "fileUploads"   # table name can be anything; class name must match relationship string

    id = Column(Integer, primary_key=True, index=True)
    topicId = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    fileName = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
