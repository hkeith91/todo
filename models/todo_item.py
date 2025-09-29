from typing import Optional
import uuid
from enum import Enum


class Frequencies(Enum):
    daily = 0
    weekly = 1
    bi_weekly = 2
    monthly = 3
    bi_monthly = 4
    yearly = 5


class TodoItem:
    """
    The standard todo item to populate todo lists
    """

    def __init__(
        self,
        todo_id: str,
        description: str,
        due_date: Optional[str] = None,
        priority: Optional[int] = None,
        recurring: bool = False,
        frequency: Optional[int] = None,
    ):
        self.todo_id = str(uuid.uuid4())
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.recurring = recurring
        self.frequency = frequency
