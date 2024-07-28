from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.ChatMessageInDB)
def create_chat_message(
    chat_message: schemas.ChatMessageCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_student),
):
    course = crud.course.get_course(db, course_id=chat_message.course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    if current_user.role == "student" and current_user not in course.enrolled_students:
        raise HTTPException(
            status_code=403, detail="You are not enrolled in this course"
        )
    elif current_user.role == "lecturer" and current_user.id != course.lecturer_id:
        raise HTTPException(
            status_code=403, detail="You are not the lecturer for this course"
        )

    return crud.chat.create_chat_message(
        db=db, chat_message=chat_message, user_id=current_user.id
    )


@router.get("/{course_id}", response_model=List[schemas.ChatMessageInDB])
def read_chat_messages(
    course_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
):
    if not current_user.role == "lecturer" or not current_user.role == "student":
        raise HTTPException(status_code=403, detail="Not authorized")

    course = crud.course.get_course(db, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    if current_user.role == "student" and current_user not in course.enrolled_students:
        raise HTTPException(
            status_code=403, detail="You are not enrolled in this course"
        )
    elif current_user.role == "lecturer" and current_user.id != course.lecturer_id:
        raise HTTPException(
            status_code=403, detail="You are not the lecturer for this course"
        )

    messages = crud.chat.get_chat_messages(
        db, course_id=course_id, skip=skip, limit=limit
    )
    return messages


@router.get("/message/{message_id}", response_model=schemas.ChatMessageInDB)
def read_chat_message(
    message_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
):
    if not current_user.role == "lecturer" or not current_user.role == "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    message = crud.chat.get_chat_message(db, message_id=message_id)
    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")

    course = crud.course.get_course(db, course_id=message.course_id)
    if current_user.role == "student" and current_user not in course.enrolled_students:
        raise HTTPException(
            status_code=403, detail="You do not have access to this message"
        )
    elif current_user.role == "lecturer" and current_user.id != course.lecturer_id:
        raise HTTPException(
            status_code=403, detail="You do not have access to this message"
        )

    return message
