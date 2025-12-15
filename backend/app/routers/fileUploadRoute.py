import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, Form
from app.helpers.databaseHandler import get_db
from sqlalchemy.orm import Session
from app.helpers.jwt import get_current_user
from app.models.fileUploadModel import FileUpload
from app.models.topicsModel import Topics
from app.helpers.fileContentUploadInVectorDb import uploadFileToVectorDb
from app.models.usersModel import Users

route = APIRouter(prefix="/file-upload", tags=["file-upload"])

@route.post("/multiple")
async def upload_multiple_files(files: list[UploadFile] = File(...), topic: str = Form(...) ,users: Users = Depends(get_current_user), db: Session = Depends(get_db)):

    try:
        file_count = len(files)
        file_record = Topics(
            userId=users.id,
            topic=topic
        )
        db.add(file_record)
        db.commit()
        db.refresh(file_record)
        for uploader in files:
            unique_filename = f"{str(uuid.uuid4())}_{uploader.filename}"
            contents = (await uploader.read()).decode("utf-8", errors="ignore")
            if not uploadFileToVectorDb(contents, unique_filename, topic,file_record.id,users.id):
                raise HTTPException(status_code=500, detail="Error in uploading file to vector DB")
            else:
                db_file = FileUpload(
                    topicId=file_record.id,
                    fileName=unique_filename,
                )
                db.add(db_file)
                db.commit()
                db.refresh(db_file)
        return {"message": "Files uploaded successfully", "topic": topic, "topicId": file_record.id, "fileCount": file_count}        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")   
