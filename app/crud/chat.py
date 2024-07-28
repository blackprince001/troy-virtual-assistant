from sqlalchemy.orm import Session

from app.core.model import troy_model
from app.models.chat import ChatMessage
from app.schemas.chat import ChatMessageCreate


def create_chat_message(db: Session, chat_message: ChatMessageCreate, user_id: int):
    response = troy_model.generate_response(chat_message.message, max_length=1000)

    db_chat_message = ChatMessage(
        user_id=user_id,
        course_id=chat_message.course_id,
        message=chat_message.message,
        response=response,
    )
    db.add(db_chat_message)
    db.commit()
    db.refresh(db_chat_message)
    return db_chat_message


def get_chat_messages(db: Session, course_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(ChatMessage)
        .filter(ChatMessage.course_id == course_id)
        .order_by(ChatMessage.timestamp.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_chat_message(db: Session, message_id: int):
    return db.query(ChatMessage).filter(ChatMessage.id == message_id).first()
