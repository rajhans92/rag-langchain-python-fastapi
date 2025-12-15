from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from app.helpers.config import CHUNK_SIZE, CHUNK_OVERLAP, EMBADDING_MODEL, VECTOR_DB_PERSIST_DIR

embedding = OpenAIEmbeddings(model=EMBADDING_MODEL)

def uploadFileToVectorDb(fileContent: str, fileName: str, topic: str, topicId: int, userId: int) -> bool:
    try:
        fileContent = cleanText(fileContent)
        textChunks = splitTextIntoChunks(fileContent,CHUNK_SIZE,CHUNK_OVERLAP)
        storeChunksInVectorDb(textChunks, fileName, topic, topicId, userId)

    except Exception as e:
        print(f"Error uploading to vector DB: {str(e)}")
        return False
    return True

def cleanText(text: str) -> str:
    text = text.replace("\x00", " ")
    text = text.replace("\n\n", "\n")
    return text.strip()

def splitTextIntoChunks(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> list:
    text_spliter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    
    return text_spliter.split_text(text)

def storeChunksInVectorDb(chunks: list, fileName: str, topic: str, topicId: int, userId: int):
    vectordb = Chroma(
        collection_name=topic,
        persist_directory=VECTOR_DB_PERSIST_DIR,
        embedding_function=embedding
    )
    vectordb.add_texts(
        texts=chunks,
        metadatas=[
            {
                "user_id": userId,
                "topic_id": topicId,
                "topic": topic,
                "file_name": fileName
            }
            for _ in chunks
        ]
    )