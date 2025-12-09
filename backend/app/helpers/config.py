from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file only once

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
API_VERSION = os.getenv("API_VERSION", "v1")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_TOKEN_TIME_HOURS = int(os.getenv("JWT_TOKEN_TIME_HOURS", 1))
