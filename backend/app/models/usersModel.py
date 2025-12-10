from sqlalchemy import Column, Integer, String
from app.helpers.databaseHandler import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primery_key=True, index=true)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)