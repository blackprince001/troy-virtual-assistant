from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str = "student"


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: str


class AdminCreate(UserCreate):
    is_admin: bool = True


class UserInDB(UserBase):
    id: int

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str
