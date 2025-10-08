import pytest
from models.todo_manager import TodoManager
from models.todo_item import TodoItem
from typing import List
from copy import deepcopy
from tests.fixtures import todo_test_data


def test_successful_deletion_returns_true(todo_test_data: List[TodoItem]):
    """Asserts the method returns a value of True upon success"""
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
    id_to_remove = todo_test_data[0].todo_id
    return_status = manager.delete_todo_item(id_to_remove)

    assert return_status, "Method did not return True"


def test_delete_todo_item_removes_one_item(todo_test_data: List[TodoItem]):
    """Asserts the method deletes only one item"""
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
    initial_length = len(todo_test_data)
    id_to_find = manager.todo_list[0].todo_id
    manager.delete_todo_item(id_to_find)

    assert (
        len(manager.todo_list) == initial_length - 1
    ), "Method failed to remove exactly one item"


def test_delete_todo_item_removes_correct_item(todo_test_data: List[TodoItem]):
    """Asserts the method deletes the correct item"""
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
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
    manager.todo_list = deepcopy(todo_test_data)
    id_to_delete = "non-existent-id"
    with pytest.raises(ValueError):
        manager.delete_todo_item(id_to_delete)
