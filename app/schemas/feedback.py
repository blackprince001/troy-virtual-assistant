from datetime import datetime

from pydantic import BaseModel


class FeedbackBase(BaseModel):
    content: str
    rating: int


class FeedbackCreate(FeedbackBase):
    chat_message_id: int


class FeedbackInDB(FeedbackBase):
    id: int
    chat_message_id: int
    user_id: int
    timestamp: datetime

    class Config:
        from_attributes = True
