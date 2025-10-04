import pytest
import uuid
from controllers.todo_manager import TodoManager
from models.todo_item import TodoItem
from typing import List
from datetime import date, time


# TODO: Add test to ensure each id is unique
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


def test_todo_list_initializes_to_empty():
    """
    Asserts that the TodoManager instance's in memory todo list initializes to an empty list
    """
    manager = TodoManager()

    assert len(manager.todo_list) == 0


def test_empty_manager_returns_empty_list():
    """Asserts an empty list is returned when TodoManager.todo_list is empty"""
    manager = TodoManager()

    assert manager.todo_list == []


def test_get_all_todo_items_returns_list(todo_test_data: List[TodoItem]):
    """Asserts that a List object is the return value"""
    manager = TodoManager()
    manager.todo_list = todo_test_data
    todo_list_to_test = manager.get_all_todo_items()

    assert isinstance(todo_list_to_test, List)


def test_get_all_todo_items_returns_todo_item_objects(todo_test_data: List[TodoItem]):
    """Asserts that returned List items are all instances of TodoItem objects"""
    manager = TodoManager()
    manager.todo_list = todo_test_data
    todo_list_to_test = manager.get_all_todo_items()

    assert all(isinstance(item, TodoItem) for item in todo_list_to_test)


def test_get_all_todo_items_returns_correct_count(todo_test_data: List[TodoItem]):
    """Asserts the returned List object contains the correct number or elements"""
    manager = TodoManager()
    manager.todo_list = todo_test_data
    todo_list_to_test = manager.get_all_todo_items()

    assert len(todo_list_to_test) == len(todo_test_data)


def test_get_all_todo_items_returns_correct_content(todo_test_data: List[TodoItem]):
    """Asserts all elements in returned List are the correct elements"""
    manager = TodoManager()
    manager.todo_list = todo_test_data
    todo_list_to_test = manager.get_all_todo_items()
    # Sort both lists by id
    test_sort_key = lambda item: item.todo_id
    todo_list_to_test.sort(key=test_sort_key)
    todo_test_data.sort(key=test_sort_key)

    assert todo_list_to_test == todo_test_data


def test_get_todo_item_by_id_returns_todo_item_object(todo_test_data: List[TodoItem]):
    """Asserts return type is instance of TodoItem object"""
    manager = TodoManager()
    manager.todo_list = todo_test_data
    test_todo_item = todo_test_data[0]
    todo_item_to_test = manager.get_todo_item_by_id(test_todo_item.todo_id)

    assert isinstance(todo_item_to_test, TodoItem)


def test_get_todo_item_by_id_returns_correct_object(todo_test_data: List[TodoItem]):
    """Asserts the correct TodoItem is returned"""
    manager = TodoManager()
    manager.todo_list = todo_test_data
    test_todo_item = todo_test_data[0]
    todo_item_to_test = manager.get_todo_item_by_id(test_todo_item.todo_id)

    assert todo_item_to_test == test_todo_item


def test_get_todo_item_by_id_returns_none_from_empty_manager():
    manager = TodoManager()

    assert manager.get_todo_item_by_id("Any_ID") is None
