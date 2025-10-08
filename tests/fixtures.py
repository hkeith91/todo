import pytest
from typing import List
from models.todo_item import TodoItem, EditTodoItem
from datetime import date, time
import uuid


@pytest.fixture
def todo_test_data() -> List[TodoItem]:
    return [
        # Has date and priority (Level 2), not complete
        TodoItem(
            todo_id=str(uuid.uuid4()),
            description="Buy milk and eggs",
            due_date=date(2025, 10, 5),
            priority=2,
        ),
        # Highest priority (Level 1), specific due date AND time
        TodoItem(
            todo_id=str(uuid.uuid4()),
            description="Finish Python Project",
            due_date=date(2025, 10, 3),
            due_time=time(17, 0, 0),  # 5:00 PM
            priority=1,
        ),
        # Recurring daily (frequency=1), marked complete, no date/time
        TodoItem(
            todo_id=str(uuid.uuid4()),
            description="Check email",
            is_complete=True,
            priority=3,
            recurring=True,
            frequency="D",
        ),
        # Urgent (Level 1), past due date/time (assuming today is Oct 1st)
        TodoItem(
            todo_id=str(uuid.uuid4()),
            description="Call doctor's office",
            due_date=date(2025, 10, 1),
            due_time=time(10, 30, 0),
            priority=1,
        ),
        # Recurring monthly (frequency=30), high priority (Level 1)
        TodoItem(
            todo_id=str(uuid.uuid4()),
            description="Pay rent",
            due_date=date(2025, 11, 1),
            priority=1,
            recurring=True,
            frequency="M",
        ),
        # Completed item, past date, default priority (None)
        TodoItem(
            todo_id=str(uuid.uuid4()),
            description="Review presentation",
            is_complete=True,
            due_date=date(2025, 9, 28),
        ),
        # Minimalist item, all optionals are None/default
        TodoItem(
            todo_id=str(uuid.uuid4()),
            description="Take out trash",
        ),
    ]


@pytest.fixture
def todo_test_item():
    return TodoItem(
        todo_id=str(uuid.uuid4()),
        description="Study SQL",
        priority=3,
        recurring=True,
        frequency="D",
    )


@pytest.fixture
def todo_dto_single_change():
    return EditTodoItem(description="Update a single item")


@pytest.fixture
def todo_dto_multi_change():
    return EditTodoItem(
        description="Update multiple items",
        priority=2,
        frequency="m",
    )


def test_fixture_items_have_unique_ids(todo_test_data: List[TodoItem]):
    id_set = {item.todo_id for item in todo_test_data}

    assert len(id_set) == len(todo_test_data)
