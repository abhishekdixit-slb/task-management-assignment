from fastapi import FastAPI
from app.core.database import engine, Base
from app.routers import task_router
from app.core.config import get_settings

# Create database tables
Base.metadata.create_all(bind=engine)

settings = get_settings()

app = FastAPI(title=settings.APP_NAME)

app.include_router(task_router.router) # appending the endpoints to the app

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Management API"}
