import chromadb


def uploadFileToVectorDb(fileContent: str, fileName: str, topic: str):
    print("Uploading to vector DB...", fileName, topic, len(fileContent))
    return True