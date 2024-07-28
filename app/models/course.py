from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from app.database import Base

course_enrollment = Table(
    "course_enrollment",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("course_id", Integer, ForeignKey("courses.id")),
)


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    lecturer_id = Column(Integer, ForeignKey("users.id"))

    lecturer = relationship("User", back_populates="courses_taught")
    enrolled_students = relationship(
        "User", secondary=course_enrollment, back_populates="enrolled_courses"
    )
    messages = relationship("ChatMessage", back_populates="course")
