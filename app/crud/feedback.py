from sqlalchemy.orm import Session

from app.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreate


def create_feedback(db: Session, feedback: FeedbackCreate, user_id: int):
    db_feedback = Feedback(
        chat_message_id=feedback.chat_message_id,
        user_id=user_id,
        content=feedback.content,
        rating=feedback.rating,
    )
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback


def get_feedback(db: Session, chat_message_id: int):
    return (
        db.query(Feedback).filter(Feedback.chat_message_id == chat_message_id).first()
    )
