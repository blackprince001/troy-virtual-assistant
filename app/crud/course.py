from sqlalchemy.orm import Session

from app.models.course import Course
from app.models.user import User
from app.schemas.course import CourseCreate, CourseUpdate


def create_course(db: Session, course: CourseCreate, lecturer_id: int):
    db_course = Course(**course.dict(), lecturer_id=lecturer_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Course).offset(skip).limit(limit).all()


def update_course(db: Session, course_id: int, course_update: CourseUpdate):
    db_course = get_course(db, course_id)
    if db_course:
        update_data = course_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_course, key, value)
        db.commit()
        db.refresh(db_course)
    return db_course


def delete_course(db: Session, course_id: int):
    db_course = get_course(db, course_id)
    if db_course:
        db.delete(db_course)
        db.commit()
    return db_course


def enroll_student(db: Session, course_id: int, user_id: int):
    course = get_course(db, course_id)
    user = db.query(User).filter(User.id == user_id).first()
    if course and user:
        course.enrolled_students.append(user)
        db.commit()
        return True
    return False


def unenroll_student(db: Session, course_id: int, user_id: int):
    course = get_course(db, course_id)
    user = db.query(User).filter(User.id == user_id).first()
    if course and user:
        course.enrolled_students.remove(user)
        db.commit()
        return True
    return False


def get_enrolled_students(db: Session, course_id: int):
    course = get_course(db, course_id)
    if course:
        return course.enrolled_students
    return []
