import jwt
from datetime import datetime, timedelta
from app.helpers.config import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_TOKEN_TIME_HOURS
from fastapi import Depends, HTTPException, status
from app.helpers.databaseHandler import get_db
# from fastapi.security import OAuth2PasswordBearer
from app.models.usersModel import Users
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login")

def create_jwt_token(data: dict):
    to_encode = data.copy()
    to_encode['exp'] = datetime.utcnow() + timedelta(hours=JWT_TOKEN_TIME_HOURS)
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db=Depends(get_db)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise HTTPException(401, "Invalid token")

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
        )

    except jwt.InvalidSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token signature"
        )

    except jwt.DecodeError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Token is corrupted or malformed"
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    user = db.query(Users).filter(Users.id == user_id).first()
    return user


