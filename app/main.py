from fastapi import FastAPI

from app.api.endpoints import admin, auth, chat, courses, feedback, users
from app.core.config import settings
from app.core.model import TroyModel
from app.database import Base, engine

app = FastAPI(title=settings.PROJECT_NAME)


@app.on_event("startup")
async def startup_event():
    global troy_model
    troy_model = TroyModel()

    Base.metadata.create_all(bind=engine)


app.include_router(auth.router, prefix="/api", tags=["auth"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(courses.router, prefix="/api/courses", tags=["courses"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(feedback.router, prefix="/api/feedback", tags=["feedback"])
