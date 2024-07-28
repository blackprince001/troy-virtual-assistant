from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.FeedbackInDB)
def create_feedback(
    feedback: schemas.FeedbackCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_lecturer),
):
    if current_user.role != "lecturer":
        raise HTTPException(
            status_code=403, detail="Only lecturers can provide feedback"
        )
    return crud.feedback.create_feedback(
        db=db, feedback=feedback, user_id=current_user.id
    )


@router.get("/{chat_message_id}", response_model=schemas.FeedbackInDB)
def read_feedback(
    chat_message_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_lecturer),
):
    feedback = crud.feedback.get_feedback(db, chat_message_id=chat_message_id)
    if feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback
