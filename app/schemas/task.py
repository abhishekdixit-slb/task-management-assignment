from pydantic import BaseModel, Field
from typing import Optional, Annotated
from enum import Enum
from datetime import datetime

class TaskStatus(str, Enum):
    """
    Enum class for task status
    """
    
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"



class TaskBase(BaseModel):
    """
    Base class for task schema
    """
    
    title:       Annotated[str, Field(min_length=3, description="Task title")]
    description: Annotated[Optional[str], Field(max_length=500, description="Task details", default=None)]
    status:      Annotated[TaskStatus, Field(description="Task status", default=TaskStatus.PENDING)]



class TaskCreate(TaskBase):
    """
    Class for task creation schema
    """
    pass



class TaskUpdate(BaseModel):
    """
    Class for task update schema
    """
    
    title:       Annotated[Optional[str], Field(min_length=3, default=None)]
    description: Annotated[Optional[str], Field(max_length=500, default=None)]
    status:      Annotated[Optional[TaskStatus], Field(default=None)]



class TaskResponse(TaskBase):
    """
    Class for task response schema
    """
   
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        """
        Config class for task response schema
        """
        from_attributes = True