import pytest
import uuid
from models.todo_manager import TodoManager, ALLOWED_ATTRIBUTES
from models.todo_item import TodoItem, EditTodoItem
from typing import List
from datetime import date, time
from copy import deepcopy


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


def test_todo_list_initializes_to_empty():
    """
    Asserts that the TodoManager instance's in memory todo list initializes to an empty list
    """
    manager = TodoManager()

    assert len(manager.todo_list) == 0, "TodoManager did not initialize to empty"


def test_empty_manager_returns_empty_list():
    """Asserts an empty list is returned when TodoManager.todo_list is empty"""
    manager = TodoManager()

    assert manager.todo_list == [], "TodoManager returned a value when empty"


def test_fixture_items_have_unique_ids(todo_test_data: List[TodoItem]):
    id_set = {item.todo_id for item in todo_test_data}

    assert len(id_set) == len(todo_test_data)


def test_get_all_todo_items_returns_list(todo_test_data: List[TodoItem]):
    """Asserts that a List object is the return value"""
    manager = TodoManager()
    manager.todo_list = todo_test_data
    todo_list_to_test = manager.get_all_todo_items()

    assert isinstance(
        todo_list_to_test, List
    ), "TodoManager did not return data of type List"


def test_get_all_todo_items_returns_todo_item_objects(todo_test_data: List[TodoItem]):
    """Asserts that returned List items are all instances of TodoItem objects"""
    manager = TodoManager()
    manager.todo_list = todo_test_data
    todo_list_to_test = manager.get_all_todo_items()

    assert all(
        isinstance(item, TodoItem) for item in todo_list_to_test
    ), "Every item in list must be a TodoItem instance"


def test_get_all_todo_items_returns_correct_count(todo_test_data: List[TodoItem]):
    """Asserts the returned List object contains the correct number or elements"""
    manager = TodoManager()
    manager.todo_list = todo_test_data
    todo_list_to_test = manager.get_all_todo_items()

    assert len(todo_list_to_test) == len(
        todo_test_data
    ), "Returned list length must match test fixture length"


def test_get_all_todo_items_returns_correct_content(todo_test_data: List[TodoItem]):
    """Asserts all elements in returned List are the correct elements"""
    manager = TodoManager()
    manager.todo_list = todo_test_data
    todo_list_to_test = manager.get_all_todo_items()
    # Sort both lists by id
    test_sort_key = lambda item: item.todo_id
    todo_list_to_test.sort(key=test_sort_key)
    todo_test_data.sort(key=test_sort_key)

    assert (
        todo_list_to_test == todo_test_data
    ), "Each List item must be identical from one List to another"


def test_get_todo_item_by_id_returns_todo_item_object(todo_test_data: List[TodoItem]):
    """Asserts return type is instance of TodoItem object"""
    manager = TodoManager()
    manager.todo_list = todo_test_data
    test_todo_item = todo_test_data[0]
    todo_item_to_test = manager.get_todo_item_by_id(test_todo_item.todo_id)

    assert isinstance(todo_item_to_test, TodoItem), "Item must be of instance TodoItem"


def test_get_todo_item_by_id_returns_correct_object(todo_test_data: List[TodoItem]):
    """Asserts the correct TodoItem is returned"""
    manager = TodoManager()
    manager.todo_list = todo_test_data
    test_todo_item = todo_test_data[0]
    todo_item_to_test = manager.get_todo_item_by_id(test_todo_item.todo_id)

    assert (
        todo_item_to_test == test_todo_item
    ), "Content of one TodoItem to the next must be identical"


def test_get_todo_item_by_id_returns_none_from_empty_manager():
    """
    Asserts return type will be None when searching for ID in an empty
    TodoManager.todo_list
    """
    manager = TodoManager()

    assert (
        manager.get_todo_item_by_id("Any_ID") is None
    ), "Method must return None when TodoManager.todo_list is empty"


def test_get_todo_item_by_id_returns_none_when_id_non_exists(
    todo_test_data: List[TodoItem],
):
    """
    Asserts return type will be None when searching for
    a non-existent ID
    """
    manager = TodoManager()
    manager.todo_list = todo_test_data

    non_existent_id = "Does not exist"
    item_to_test = manager.get_todo_item_by_id(non_existent_id)

    assert (
        item_to_test is None
    ), "Method must return None when searching ID that does not exist"


def test_add_todo_item_appends_to_empty_list(todo_test_data: List[TodoItem]):
    """Asserts a TodoItem can be added to an empty list"""
    manager = TodoManager()
    item_to_add = todo_test_data[0]
    manager.add_todo_item(item_to_add)

    assert len(manager.todo_list) == 1, "Failed to add item to empty list"


def test_add_todo_item_appends_correct_item_to_empty_list(
    todo_test_data: List[TodoItem],
):
    """Asserts the correct TodoItem is added to an empty list"""
    manager = TodoManager()
    item_to_add = todo_test_data[0]
    manager.add_todo_item(item_to_add)

    assert (
        manager.todo_list[0] == item_to_add
    ), "The tested item did not match item that was added"


def test_add_todo_item_appends_to_non_empty_list(
    todo_test_data: List[TodoItem], todo_test_item: TodoItem
):
    """Asserts the Manager appends the item to a non-empty list"""
    manager = TodoManager()
    manager.todo_list = todo_test_data[:]
    initial_length = len(manager.todo_list)
    item_to_add = todo_test_item
    manager.add_todo_item(item_to_add)

    assert (
        len(manager.todo_list) == initial_length + 1
    ), "The number of elements in the list did not match expected value"


def test_add_todo_item_appends_correct_item_to_non_empty_list(
    todo_test_data: List[TodoItem], todo_test_item: TodoItem
):
    """Asserts the Manager appends the correct item to a non-empty list"""
    manager = TodoManager()
    manager.todo_list = todo_test_data
    item_to_add = todo_test_item
    manager.add_todo_item(item_to_add)

    assert (
        manager.todo_list[-1] == item_to_add
    ), "The tested item did not match the expected value"


def test_add_non_unique_id_raises_exception(todo_test_data: List[TodoItem]):
    """Asserts the method will raise a ValueError when adding an ID that already exists"""
    manager = TodoManager()
    manager.todo_list = todo_test_data[:]
    with pytest.raises(ValueError):
        manager.add_todo_item(todo_test_data[0])


def test_successful_deletion_returns_true(todo_test_data: List[TodoItem]):
    """Asserts the method returns a value of True upon success"""
    manager = TodoManager()
    manager.todo_list = todo_test_data[:]
    id_to_remove = todo_test_data[0].todo_id
    return_status = manager.delete_todo_item(id_to_remove)

    assert return_status, "Method did not return True"


def test_delete_todo_item_removes_one_item(todo_test_data: List[TodoItem]):
    """Asserts the method deletes only one item"""
    manager = TodoManager()
    manager.todo_list = todo_test_data[:]
    initial_length = len(todo_test_data)
    id_to_find = manager.todo_list[0].todo_id
    manager.delete_todo_item(id_to_find)

    assert (
        len(manager.todo_list) == initial_length - 1
    ), "Method failed to remove exactly one item"


def test_delete_todo_item_removes_correct_item(todo_test_data: List[TodoItem]):
    """Asserts the method deletes the correct item"""
    manager = TodoManager()
    manager.todo_list = todo_test_data[:]
    item_to_delete = todo_test_data[0]
    id_to_delete = item_to_delete.todo_id
    manager.delete_todo_item(id_to_delete)

    assert (
        item_to_delete not in manager.todo_list
    ), "The correct item was not deleted properly"


def test_delete_todo_item_raises_exception_when_item_non_exists(
    todo_test_data: List[TodoItem],
):
    """Asserts an exception is raised when trying to delete a non-existent item"""
    manager = TodoManager()
    manager.todo_list = todo_test_data[:]
    id_to_delete = "non-existent-id"
    with pytest.raises(ValueError):
        manager.delete_todo_item(id_to_delete)


def test_edit_todo_item_does_not_alter_count(
    todo_test_data: List[TodoItem], todo_dto_single_change: EditTodoItem
):
    """Asserts number of items in TodoManager.todo_list is not changes by edit operation"""
    manager = TodoManager()
    manager.todo_list = todo_test_data[:]
    initial_length = len(todo_test_data)
    id_to_edit = todo_test_data[0].todo_id
    manager.edit_todo_item(id_to_edit, todo_dto_single_change)

    assert (
        len(manager.todo_list) == initial_length
    ), "The length of the list containing item to edit must remain unchanged"


def test_edit_todo_item_changes_item_simple(
    todo_test_data: List[TodoItem], todo_dto_single_change: EditTodoItem
):
    """Asserts method will change the value of a single attribute"""
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
    id_to_edit = todo_test_data[0].todo_id
    manager.edit_todo_item(id_to_edit, todo_dto_single_change)

    assert manager.todo_list[0] != todo_test_data[0]
    assert manager.todo_list[0].description == todo_dto_single_change.description
    for i in range(1, len(manager.todo_list)):
        assert manager.todo_list[i] == todo_test_data[i]


def test_edit_todo_item_changes_item_complex(
    todo_test_data: List[TodoItem], todo_dto_multi_change: EditTodoItem
):
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
    id_to_edit = todo_test_data[0].todo_id
    manager.edit_todo_item(id_to_edit, todo_dto_multi_change)

    for attribute in ALLOWED_ATTRIBUTES:
        expected_value = getattr(todo_dto_multi_change, attribute)
        if expected_value is not None:
            actual_value = getattr(manager.todo_list[0], attribute)
            assert actual_value == expected_value

    assert manager.todo_list[0] != todo_test_data[0]
    for i in range(1, len(todo_test_data)):
        assert manager.todo_list[i] == todo_test_data[i]
