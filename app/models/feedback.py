import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    chat_message_id = Column(Integer, ForeignKey("chat_messages.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    rating = Column(Integer)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    chat_message = relationship("ChatMessage", back_populates="feedback")
    user = relationship("User", back_populates="feedback")
