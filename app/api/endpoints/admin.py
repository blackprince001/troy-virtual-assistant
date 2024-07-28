from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.UserInDB)
def create_admin(
    admin: schemas.AdminCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    db_user = crud.user.get_user_by_email(db, email=admin.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.user.create_admin(db=db, admin=admin)


@router.get("/", response_model=List[schemas.UserInDB])
def read_admins(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    admins = crud.user.get_admins(db, skip=skip, limit=limit)
    return admins
