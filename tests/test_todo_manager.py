import pytest
from controllers.todo_manager import TodoManager
from models.todo_item import TodoItem
from typing import List
from datetime import date, time


@pytest.fixture
def todo_test_data() -> List[TodoItem]:
    return [
        # Has date and priority (Level 2), not complete
        TodoItem(
            todo_id="str(uuid.uuid4())",
            description="Buy milk and eggs",
            due_date=date(2025, 10, 5),
            priority=2,
        ),
        # Highest priority (Level 1), specific due date AND time
        TodoItem(
            todo_id="str(uuid.uuid4())",
            description="Finish Python Project",
            due_date=date(2025, 10, 3),
            due_time=time(17, 0, 0),  # 5:00 PM
            priority=1,
        ),
        # Recurring daily (frequency=1), marked complete, no date/time
        TodoItem(
            todo_id="str(uuid.uuid4())",
            description="Check email",
            is_complete=True,
            priority=3,
            recurring=True,
            frequency="D",
        ),
        # Urgent (Level 1), past due date/time (assuming today is Oct 1st)
        TodoItem(
            todo_id="str(uuid.uuid4())",
            description="Call doctor's office",
            due_date=date(2025, 10, 1),
            due_time=time(10, 30, 0),
            priority=1,
        ),
        # Recurring monthly (frequency=30), high priority (Level 1)
        TodoItem(
            todo_id="str(uuid.uuid4())",
            description="Pay rent",
            due_date=date(2025, 11, 1),
            priority=1,
            recurring=True,
            frequency="M",
        ),
        # Completed item, past date, default priority (None)
        TodoItem(
            todo_id="str(uuid.uuid4())",
            description="Review presentation",
            is_complete=True,
            due_date=date(2025, 9, 28),
        ),
        # Minimalist item, all optionals are None/default
        TodoItem(
            todo_id="str(uuid.uuid4())",
            description="Take out trash",
        ),
    ]


def test_todo_list_initializes_to_empty():
    manager = TodoManager()
    assert len(manager.todo_list) == 0


def test_get_all_todo_items(todo_test_data: List[TodoItem]):
    manager = TodoManager()
    manager.todo_list = todo_test_data
    todo_list_to_test = manager.get_all_todo_items()
    # Sort both lists by id
    test_sort_key = lambda item: item.todo_id
    todo_list_to_test.sort(key=test_sort_key)
    todo_test_data.sort(key=test_sort_key)

    assert isinstance(todo_list_to_test, List)
    assert all(isinstance(item, TodoItem) for item in todo_list_to_test)
    # Separate check for length for additional info
    assert len(todo_list_to_test) == len(todo_test_data)
    assert todo_list_to_test == todo_test_data
