# app/models/fileUploadModel.py
from sqlalchemy import Column, Integer, String, ForeignKey
from app.helpers.databaseHandler import Base

class FileUpload(Base):
    __tablename__ = "fileUploads"   # table name can be anything; class name must match relationship string

    id = Column(Integer, primary_key=True, index=True)
    fileName = Column(String(255), nullable=False)
    fileTopic = Column(String(100), nullable=False)
    userId = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
