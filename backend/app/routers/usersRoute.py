from fastapi import APIRouter, HTTPException, Depends
from app.helpers.databaseHandler import get_db
from sqlalchemy.orm import Session
from app.schemas.usersSchema import UserCreateSchema, UserLoginSchema
from app.models.usersModel import Users
from app.helpers.hashing import hashPassword, verifyPassword
from app.helpers.jwt import create_jwt_token, get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
def registerUser(userRequest: UserCreateSchema, db: Session = Depends(get_db)):
    userExist = db.query(Users).filter(Users.email == userRequest.email).first()
    if userExist:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashPasswordData = hashPassword(userRequest.password)

    newUser = Users(
        email=userRequest.email,
        password=hashPasswordData,
        name=userRequest.name
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return {"message": "User registered successfully"}

@router.post("/login")
def loginUser(userRequest: UserLoginSchema, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.email == userRequest.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email")
    
    if not verifyPassword(userRequest.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    jwt_token = create_jwt_token({"user_id":db_user.id, "user_name": db_user.name, "user_email":db_user.email})

    return {"message": "User logged in successfully", "token":jwt_token, "user_name": db_user.name, "user_email":db_user.email}

@router.post("/profile")
def get_user_profile(user: Users = Depends(get_current_user)):
    return {"message": "User profile data", "user": {"id": user.id, "name": user.name, "email": user.email}}