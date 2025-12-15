from pydantic import BaseModel


class ChatRequestSchema(BaseModel):
    topicId: int
    question: str