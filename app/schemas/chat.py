from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.schemas import FeedbackInDB


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

    feedback: Optional[FeedbackInDB] = None

    class Config:
        from_attributes = True
