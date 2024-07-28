from datetime import datetime

from pydantic import BaseModel


class ChatMessageBase(BaseModel):
    message: str
    course_id: int


class ChatMessageCreate(ChatMessageBase):
    pass


class ChatMessageInDB(ChatMessageBase):
    id: int
    user_id: int
    response: str
    timestamp: datetime

    class Config:
        from_attributes = True
