from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hashPassword(password: str):
    return pwd_context.hash(password)

def verifyPassword(plain, hashed):
    return pwd_context.verify(plain, hashed)