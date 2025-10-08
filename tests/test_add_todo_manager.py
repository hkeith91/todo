import pytest
from typing import List
from models.todo_item import TodoItem
from models.todo_manager import TodoManager
from copy import deepcopy
from tests.fixtures import todo_test_item, todo_test_data


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
    manager.todo_list = deepcopy(todo_test_data)
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
    manager.todo_list = deepcopy(todo_test_data)
    item_to_add = todo_test_item
    manager.add_todo_item(item_to_add)

    assert (
        manager.todo_list[-1] == item_to_add
    ), "The tested item did not match the expected value"


def test_add_non_unique_id_raises_exception(todo_test_data: List[TodoItem]):
    """Asserts the method will raise a ValueError when adding an ID that already exists"""
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
    with pytest.raises(ValueError):
        manager.add_todo_item(todo_test_data[0])
