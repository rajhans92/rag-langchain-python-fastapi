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


CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))

EMBADDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
VECTOR_DB_PERSIST_DIR = os.getenv("VECTOR_DB_PERSIST_DIR", "./chroma_db")

VECTOR_DB_COLLECTION_NAME = os.getenv("VECTOR_DB_COLLECTION_NAME", "rag_documents")