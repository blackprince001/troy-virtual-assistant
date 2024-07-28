from typing import List, Optional

from pydantic import BaseModel


class CourseBase(BaseModel):
    name: str
    description: str


class CourseCreate(CourseBase):
    pass


class CourseUpdate(CourseBase):
    name: Optional[str] = None
    description: Optional[str] = None


class CourseInDB(CourseBase):
    id: int
    lecturer_id: int

    class Config:
        from_attributes = True


class CourseWithEnrollment(CourseInDB):
    enrolled_students: List[int]
