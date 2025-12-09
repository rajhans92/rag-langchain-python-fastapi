from fastapi import FastAPI, HTTPException
from app.helpers.databaseHandler import Base, engine
from app.helpers.config import API_VERSION

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}