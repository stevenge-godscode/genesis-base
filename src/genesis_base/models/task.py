from dataclasses import dataclass
from typing import Optional, Dict, Any
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TaskStatus:
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class TaskModel(Base):
    __tablename__ = 'tasks'

    task_id = Column(String(50), primary_key=True)
    input_text = Column(Text, nullable=False)
    video_path = Column(String(255), nullable=False)
    status = Column(SQLEnum(TaskStatus), default=TaskStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    error = Column(Text)

@dataclass
class Task:
    task_id: str
    input_text: str
    video_path: str
    status: str = TaskStatus.PENDING
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    error: Optional[str] = None

    @classmethod
    def from_model(cls, model: TaskModel) -> 'Task':
        return cls(
            task_id=model.task_id,
            input_text=model.input_text,
            video_path=model.video_path,
            status=model.status,
            created_at=model.created_at,
            updated_at=model.updated_at,
            error=model.error
        )

@dataclass
class TaskResult:
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None 