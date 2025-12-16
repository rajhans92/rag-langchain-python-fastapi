import os
import io
from fastapi import HTTPException, UploadFile
from pypdf import PdfReader
from docx import Document

async def fileContentParser(file: UploadFile)-> str:
    try:
        ext = os.path.splitext(file.filename)[1].lower()
        content = await file.read()
        print(f"File extension identified: {ext}")
        match ext.lower():
            case ".txt":
                return content.decode("utf-8", errors="ignore")

            case ".pdf":
                return parse_pdf(content)

            case ".docx":
                return parse_docx(content)

            case ".csv":
                return parse_csv(content)

            case _:
                raise ValueError(f"Unsupported file type: {ext}")
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading file content: {str(e)}")
    
def parse_pdf(content: bytes) -> str:
    try:
        reader = PdfReader(io.BytesIO(content))
        text = []
        for page in reader.pages:
            text.append(page.extract_text() or "")
        return "\n".join(text)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing PDF file: {str(e)}")

def parse_docx(content: bytes) -> str:
    try:
        doc = Document(io.BytesIO(content))
        return "\n".join(p.text for p in doc.paragraphs)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing PDF file: {str(e)}")


def parse_csv(content: bytes) -> str:
    pass