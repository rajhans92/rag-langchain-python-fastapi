from pydantic import BaseModel, EmailStr, Field

class UserCreateSchema(BaseModel):
    email: EmailStr = Field(..., min_length=3, max_length=100)
    password: str = Field(..., min_length=4, max_length=128)
    name: str = Field(..., min_length=4, max_length=255)

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(..., min_length=3, max_length=100)
    password: str = Field(..., min_length=4, max_length=128)