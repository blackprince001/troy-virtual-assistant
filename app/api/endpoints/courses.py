from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.CourseInDB)
def create_course(
    course: schemas.CourseCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_lecturer),
):
    return crud.course.create_course(db=db, course=course, lecturer_id=current_user.id)


@router.get("/", response_model=List[schemas.CourseInDB])
def read_courses(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
):
    courses = crud.course.get_courses(db, skip=skip, limit=limit)
    return courses


@router.get("/{course_id}", response_model=schemas.CourseWithEnrollment)
def read_course(
    course_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
):
    course = crud.course.get_course(db, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    course_data = {
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "lecturer_id": course.lecturer_id,
        "enrolled_students": [student.id for student in course.enrolled_students],
    }

    return schemas.CourseWithEnrollment(**course_data)


@router.put("/{course_id}", response_model=schemas.CourseInDB)
def update_course(
    course_id: int,
    course_update: schemas.CourseUpdate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_lecturer),
):
    course = crud.course.get_course(db, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    if course.lecturer_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to update this course"
        )
    return crud.course.update_course(
        db, course_id=course_id, course_update=course_update
    )


@router.delete("/{course_id}", response_model=schemas.CourseInDB)
def delete_course(
    course_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_lecturer),
):
    course = crud.course.get_course(db, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    if course.lecturer_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to delete this course"
        )
    return crud.course.delete_course(db, course_id=course_id)


@router.post("/{course_id}/enroll", response_model=schemas.CourseWithEnrollment)
def enroll_in_course(
    course_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_student),
):
    if crud.course.enroll_student(db, course_id, current_user.id):
        return read_course(course_id, db, current_user)
    raise HTTPException(status_code=400, detail="Unable to enroll in the course")


@router.post("/{course_id}/unenroll", response_model=schemas.CourseWithEnrollment)
def unenroll_from_course(
    course_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_student),
):
    if crud.course.unenroll_student(db, course_id, current_user.id):
        return read_course(course_id, db, current_user)
    raise HTTPException(status_code=400, detail="Unable to unenroll from the course")
