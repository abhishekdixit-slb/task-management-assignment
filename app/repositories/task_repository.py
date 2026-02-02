from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

class TaskRepository:
    def __init__(self, db: Session):
        """
        Initialize the task repository.
        """
        
        self.db = db

    def create_task(self, task: TaskCreate) -> Task:
        """
        Create a new task.
        """

        db_task = Task(
            title=task.title,
            description=task.description,
            status=task.status.value
        )
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task



    def get_tasks(self, skip: int = 0, limit: int = 100, status: str | None = None) -> list[Task]:
        """
        Get all tasks from the database.
        """
        
        query = self.db.query(Task).filter(Task.is_deleted == False)
        if status:
            query = query.filter(Task.status == status)

        return query.offset(skip).limit(limit).all()



    def get_task_by_id(self, task_id: int) -> Task | None:
        """
        Get a task by its id.
        """

        return self.db.query(Task).filter(Task.id == task_id, Task.is_deleted == False).first()



    def update_task(self, db_task: Task, task_update: TaskUpdate) -> Task:
        """
        Update a task.
        """

        update_data = task_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            if key == 'status' and value:
                setattr(db_task, key, value.value)
            else:
                setattr(db_task, key, value)
        
        self.db.commit()
        self.db.refresh(db_task)
        return db_task



    def delete_task(self, db_task: Task) -> None:
        """
        Delete a task (Soft Delete).
        """

        setattr(db_task, 'is_deleted', True)
        self.db.commit()
        self.db.refresh(db_task)

