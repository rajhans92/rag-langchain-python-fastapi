from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.helpers.config import DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME

engine = create_engine(f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}")
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    print("DB connected stabilist")
    try:
        yield db
    finally:
        db.close()