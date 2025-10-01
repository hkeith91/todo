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
        frequency: Optional[str] = None,
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

    def __eq__(self, other):
        if not isinstance(other, TodoItem):
            return NotImplemented
        return (
            self.todo_id == other.todo_id
            and self.is_complete == other.is_complete
            and self.due_date == other.due_date
            and self.due_time == other.due_time
            and self.past_due == other.past_due
            and self.priority == other.priority
            and self.recurring == other.recurring
            and self.frequency == other.frequency
        )

    def __hash__(self):
        return hash(self.todo_id)
