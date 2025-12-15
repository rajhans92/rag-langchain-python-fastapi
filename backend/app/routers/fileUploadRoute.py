import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, Form
from app.helpers.databaseHandler import get_db
from sqlalchemy.orm import Session
from app.helpers.jwt import get_current_user
from app.models.fileUploadModel import FileUpload
from app.helpers.fileContentUploadInVectorDb import uploadFileToVectorDb
from app.models.usersModel import Users

route = APIRouter(prefix="/file-upload", tags=["file-upload"])

@route.post("/multiple")
async def upload_multiple_files(files: list[UploadFile] = File(...), topic: str = Form(...) ,users: Users = Depends(get_current_user), db: Session = Depends(get_db)):

    try:
        for uploader in files:
            unique_filename = f"{str(uuid.uuid4())}_{uploader.filename}"
            contents = (await uploader.read()).decode("utf-8", errors="ignore")
            file_record = FileUpload(
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
