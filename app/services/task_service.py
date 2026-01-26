from sqlalchemy.orm import Session
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate
from app.models.task import Task

class TaskService:
    def __init__(self, db: Session):
        """
        Initialize the task service.
        """

        self.repository = TaskRepository(db)



    def create_task(self, task: TaskCreate) -> Task:
        """
        Creates a new task in the database.
        """

        return self.repository.create_task(task)



    def get_tasks(self, skip: int = 0, limit: int = 100, status: str | None = None) -> list[Task]:
        """
        Get all tasks from the database.
        """

        return self.repository.get_tasks(skip, limit, status)



    def get_task(self, task_id: int) -> Task | None:
        """
        Get a task by its id from the database.
        """

        return self.repository.get_task_by_id(task_id)



    def update_task(self, task_id: int, task_update: TaskUpdate) -> Task | None:
        """
        Update a task in the database.
        """

        db_task = self.repository.get_task_by_id(task_id)
        if not db_task:
            return None
        
        return self.repository.update_task(db_task, task_update)



    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the database.
        """
        
        db_task = self.repository.get_task_by_id(task_id)
        if not db_task:
            return False
        self.repository.delete_task(db_task)
        return True
