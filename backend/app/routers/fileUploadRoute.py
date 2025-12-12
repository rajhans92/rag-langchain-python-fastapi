import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.helpers.database import get_db
from sqlalchemy.orm import Session
from app.helpers.jwt import get_current_user
from app.models.FileUploadModel import FileUploadModel

route = APIRouter(prefix="/file-upload", tags=["file-upload"])

@route.post("/multiple")
def upload_multiple_files(files: list[UploadFile] = File(...), topic: str = Files(...) ,users = Depends(get_current_user), db: Session = Depends(get_db)):

    try:
        for uploader in files:
            unique_filename = f"{str(uuid.uuid4())}_{uploader.filename}"
            contents = uploader.read().decode("utf-8")
            file_record = FileUploadModel(
                userId=users.id,
                fileTopic=topic,
                fileName=unique_filename
            )
            db.add(file_record)
            db.commit()
            db.refresh(file_record)
            upload_in_vector_db = uploadFileToVectorDb(contents, unique_filename, topic)
        return {"message": "Files uploaded successfully", "topic": topic}        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")   
