from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate, TaskStatus
from app.services.task_service import TaskService


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    API Endpoint to create a new task.
    """
    
    service = TaskService(db)
    return service.create_task(task)



@router.get("/", response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
def get_tasks(skip: int = 0, limit: int = 100, status: TaskStatus | None = None, db: Session = Depends(get_db)):
    """
    API Endpoint to get all tasks.
    """

    service = TaskService(db)
    return service.get_tasks(skip, limit, status)



@router.get("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def get_task(task_id: int, db: Session = Depends(get_db)):
    """
    API Endpoint to get a task by id.
    """
    
    service = TaskService(db)
    task = service.get_task(task_id)
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task



@router.put("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    """
    API Endpoint to update a task by id.
    """

    service = TaskService(db)
    task = service.update_task(task_id, task_update)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task



@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    API Endpoint to delete a task by id.
    """
    service = TaskService(db)
    success = service.delete_task(task_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
