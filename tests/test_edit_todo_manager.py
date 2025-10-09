from models.todo_manager import TodoManager, ALLOWED_ATTRIBUTES
from models.todo_item import TodoItem, EditTodoItem
from typing import List
from copy import deepcopy
from tests.fixtures import (
    todo_test_data,
    todo_dto_multi_change,
    todo_dto_single_change,
)


def test_edit_todo_item_does_not_alter_count(
    todo_test_data: List[TodoItem], todo_dto_single_change: EditTodoItem
):
    """Asserts number of items in TodoManager.todo_list is not changes by edit operation"""
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
    initial_length = len(todo_test_data)
    id_to_edit = todo_test_data[0].todo_id
    manager.edit_todo_item(id_to_edit, todo_dto_single_change)

    assert (
        len(manager.todo_list) == initial_length
    ), "The length of the list containing item to edit must remain unchanged"


def test_edit_todo_item_changes_item_simple(
    todo_test_data: List[TodoItem], todo_dto_single_change: EditTodoItem
):
    """
    Asserts method will change the value of a single attribute
    without effecting other list items or incorrect attributes
    """
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
    id_to_edit = todo_test_data[0].todo_id
    manager.edit_todo_item(id_to_edit, todo_dto_single_change)

    assert (
        manager.todo_list[0] != todo_test_data[0]
    ), "The item to edit remained unchanged"
    assert (
        manager.todo_list[0].description == todo_dto_single_change.description
    ), "The attribute did not match the expected value"
    for i in range(1, len(manager.todo_list)):
        assert (
            manager.todo_list[i] == todo_test_data[i]
        ), "An incorrect field was changed"


def test_edit_todo_item_changes_item_complex(
    todo_test_data: List[TodoItem], todo_dto_multi_change: EditTodoItem
):
    """
    Asserts method will change the value of multiple attributes without
    changing other items or incorrect fields
    """
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
    id_to_edit = todo_test_data[0].todo_id
    manager.edit_todo_item(id_to_edit, todo_dto_multi_change)

    for attribute in ALLOWED_ATTRIBUTES:
        expected_value = getattr(todo_dto_multi_change, attribute)
        if expected_value is not None:
            actual_value = getattr(manager.todo_list[0], attribute)
            assert (
                actual_value == expected_value
            ), f"An attribute '{attribute}' did not match the expected value"

    assert (
        manager.todo_list[0] != todo_test_data[0]
    ), "The item to edit remained unchanged"
    for i in range(1, len(todo_test_data)):
        assert (
            manager.todo_list[i] == todo_test_data[i]
        ), f"An incorrect attribute '{manager.todo_list[i]}' was changed"
