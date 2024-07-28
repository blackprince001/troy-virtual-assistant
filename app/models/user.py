from sqlalchemy import Boolean, Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(
        Enum("student", "lecturer", "admin", name="user_roles"), default="student"
    )
    is_admin = Column(Boolean, default=False)

    courses_taught = relationship("Course", back_populates="lecturer")
    enrolled_courses = relationship(
        "Course", secondary="course_enrollment", back_populates="enrolled_students"
    )
    messages = relationship("ChatMessage", back_populates="user")
