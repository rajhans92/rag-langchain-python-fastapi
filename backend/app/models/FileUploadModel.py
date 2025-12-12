from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class FileUploadModel(Base):
    __tablename__ = "fileUploads"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"))
    fileTopic = Column(String(255), nullable=False)
    fileName = Column(String, unique=True, index=True, nullable=False)

    user = relationship("Users", back_populates="files")