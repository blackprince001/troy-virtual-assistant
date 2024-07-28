from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.schemas.user import AdminCreate, UserCreate, UserUpdate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = get_user(db, user_id)
    if db_user:
        update_data = user.dict(exclude_unset=True)
        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(update_data["password"])
            del update_data["password"]
        for key, value in update_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user


def create_admin(db: Session, admin: AdminCreate):
    hashed_password = get_password_hash(admin.password)
    db_admin = User(
        username=admin.username,
        email=admin.email,
        hashed_password=hashed_password,
        role="admin",
        is_admin=True,
    )
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


def get_admins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).filter(User.is_admin == True).offset(skip).limit(limit).all()
