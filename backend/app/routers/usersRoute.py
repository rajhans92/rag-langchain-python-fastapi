from fastapi import APIRouter, HTTPException, Depends
from app.helpers.database import get_db
from sqlalchemy.orm import Session
from app.schemas.usersSchema import UserCreateSchema, UserLoginSchema
from app.models.usersModels import Users
from app.helpers.hashing import hashPassword, verifyPassword


router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
def registerUser(userRequest: UserCreateSchema, db: Session = Depends(get_db)):
    userExist = db.query(Users).flter(Users.emial == userRequest.email).first()
    if userExist:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashPassword = hashPassword(userRequest.password)

    newUser = Users(
        email=userRequest.email,
        password=hashPassword,
        name=userRequest.name
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return {"message": "User registered successfully"}

@router.post("/login")
def loginUser(userRequest: UserLoginSchema, db: Session = Depends(get_db)):
    dbUser = db.query(Users).flter(Users.email == userRequest.email).first()
    if not dbUser:
        raise HTTPException(status_code=400, detail="Invalid email")
    
    if not verifyPassword(userRequest.password, dbUser.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    return {"message": "User logged in successfully"}