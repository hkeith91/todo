from typing import Optional
import uuid
from enum import Enum
from datetime import date, time


class Frequencies(Enum):
    daily = "D"
    weekly = "W"
    bi_weekly = "BW"
    monthly = "M"
    bi_monthly = "BM"
    yearly = "Y"
    custom = "C"


class TodoItem:
    """
    The standard todo item to populate todo lists
    """

    def __init__(
        self,
        todo_id: str,
        description: str,
        is_complete: bool = False,
        due_date: Optional[date] = None,
        due_time: Optional[time] = None,
        past_due: bool = False,
        priority: Optional[int] = None,
        recurring: bool = False,
        frequency: Optional[int] = None,
    ):
        self.todo_id = str(uuid.uuid4())
        self.description = description
        self.is_complete = is_complete
        self.due_date = due_date
        self.due_time = due_time
        self.past_due = past_due
        self.priority = priority
        self.recurring = recurring
        self.frequency = frequency

        def __repr__(self):
            status = "COMPLETE" if self.is_complete else "NOT complete"
            return f"{status} {self.todo_id} | {self.description} (Due: {self.due_date or 'N/A'})"
