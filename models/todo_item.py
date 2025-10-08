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


class TodoItem:
    """
    The standard todo item to populate todo lists
    """

    def __init__(
        self,
        todo_id: Optional[str],
        description: str,
        is_complete: bool = False,
        due_date: Optional[date] = None,
        due_time: Optional[time] = None,
        past_due: bool = False,
        priority: Optional[int] = None,
        recurring: bool = False,
        frequency: Optional[str] = None,
        created_at: datetime = datetime.now(),
        last_updated: datetime = datetime.now(),
    ):
        self.todo_id = todo_id
        self.description = description
        self.is_complete = is_complete
        self.due_date = due_date
        self.due_time = due_time
        self.past_due = past_due
        self.priority = priority
        self.is_recurring = recurring
        self.frequency = frequency
        self.created_at = created_at
        self.last_updated = last_updated

    @staticmethod
    def generate_unique_id():
        return str(uuid.uuid4())

    def __repr__(self):
        status = "COMPLETE" if self.is_complete else "NOT complete"
        return f"{status} {self.todo_id} | {self.description} (Due: {self.due_date or 'N/A'})"

    def __eq__(self, other):
        if not isinstance(other, TodoItem):
            return NotImplemented
        return (
            self.todo_id == other.todo_id
            and self.description == other.description
            and self.is_complete == other.is_complete
            and self.due_date == other.due_date
            and self.due_time == other.due_time
            and self.past_due == other.past_due
            and self.priority == other.priority
            and self.is_recurring == other.is_recurring
            and self.frequency == other.frequency
            and self.created_at == other.created_at
            and self.last_updated == other.last_updated
        )

    def __hash__(self):
        return hash(self.todo_id)


class EditTodoItem:
    """
    TodoItem Data Transfer Object.  Used in Update operations.
    """

    def __init__(
        self,
        description: Optional[str] = None,
        is_complete: Optional[bool] = None,
        due_date: Optional[date] = None,
        due_time: Optional[time] = None,
        priority: Optional[int] = None,
        frequency: Optional[str] = None,
    ):
        self.description = description
        self.is_complete = is_complete
        self.due_date = due_date
        self.due_time = due_time
        self.priority = priority
        self.frequency = frequency
