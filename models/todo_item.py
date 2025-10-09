from dataclasses import dataclass
from typing import Optional
import uuid
from enum import Enum
from datetime import date, time, datetime


# Frequencies recurring tasks repeat
class FREQUENCIES(Enum):
    daily = "D"
    weekly = "W"
    bi_weekly = "BW"
    monthly = "M"
    bi_monthly = "BM"
    yearly = "Y"
    custom = "C"
    none = "N"


@dataclass()
class TodoItem:
    """
    The standard todo item to populate todo lists
    """

    todo_id: Optional[str]
    description: str
    is_complete: bool = False
    due_date: Optional[date] = None
    due_time: Optional[time] = None
    past_due: bool = False
    priority: Optional[int] = None
    recurring: bool = False
    frequency: Optional[str] = None
    created_at: datetime = datetime.now()
    last_updated: datetime = datetime.now()

    @staticmethod
    def generate_unique_id():
        return str(uuid.uuid4())

    def __hash__(self):
        return hash(self.todo_id)


@dataclass()
class EditTodoItem:
    """
    TodoItem Data Transfer Object.  Used in Update operations.
    """

    description: Optional[str] = None
    is_complete: Optional[bool] = None
    due_date: Optional[date] = None
    due_time: Optional[time] = None
    priority: Optional[int] = None
    frequency: Optional[str] = None
