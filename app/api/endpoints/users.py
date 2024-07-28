from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.UserInDB])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
):
    if not current_user.role == "lecturer" or not current_user.role == "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    users = crud.user.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.UserInDB)
def read_user(
    user_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
):
    if not current_user.role == "lecturer" or not current_user.role == "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    db_user = crud.user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{user_id}", response_model=schemas.UserInDB)
def update_user(
    user_id: int,
    user: schemas.UserUpdate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    if current_user.id != user_id and current_user.role != "admin":
        raise HTTPException(
            status_code=403, detail="Not authorized to update this user"
        )
    return crud.user.update_user(db=db, user_id=user_id, user=user)


@router.delete("/{user_id}", response_model=schemas.UserInDB)
def delete_user(
    user_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    if current_user.id != user_id and current_user.role != "admin":
        raise HTTPException(
            status_code=403, detail="Not authorized to delete this user"
        )
    user = crud.user.delete_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/me", response_model=schemas.UserInDB)
def get_current_user(current_user: models.User = Depends(deps.get_current_user)):
    return current_user
