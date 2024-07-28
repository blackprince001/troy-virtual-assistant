from datetime import datetime
from typing import List

from pydantic import BaseModel

from .feedback import FeedbackInDB


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

    feedback: List[FeedbackInDB] = []

    class Config:
        from_attributes = True
