from models.todo_manager import TodoManager, ALLOWED_ATTRIBUTES
from models.todo_item import TodoItem, EditTodoItem
from typing import List
from copy import deepcopy
from tests.fixtures import (
    todo_test_data,
    todo_dto_multi_change,
    todo_dto_single_change,
    fixture_list_to_dict,
)


def test_edit_todo_item_does_not_alter_count(
    todo_test_data: List[TodoItem], todo_dto_single_change: EditTodoItem
):
    """Asserts number of items in TodoManager.todo_list is not changes by edit operation"""
    manager = TodoManager()
    manager.todo_items = fixture_list_to_dict(todo_test_data)
    initial_length = len(todo_test_data)
    id_to_edit = todo_test_data[0].todo_id
    manager.edit_todo_item(id_to_edit, todo_dto_single_change)

    assert (
        len(manager.todo_items) == initial_length
    ), "The length of the list containing item to edit must remain unchanged"


def test_edit_todo_item_changes_item_simple(
    todo_test_data: List[TodoItem], todo_dto_single_change: EditTodoItem
):
    """
    Asserts method will change the value of a single attribute
    without effecting other list items or incorrect attributes
    """
    manager = TodoManager()
    original_items = deepcopy(todo_test_data)
    original_items = fixture_list_to_dict(original_items)
    manager.todo_items = fixture_list_to_dict(todo_test_data)
    id_to_edit = todo_test_data[0].todo_id
    manager.edit_todo_item(id_to_edit, todo_dto_single_change)

    assert (
        manager.todo_items[id_to_edit] != original_items[id_to_edit]
    ), "The item to edit remained unchanged"
    assert (
        manager.todo_items[id_to_edit].description == todo_dto_single_change.description
    ), "The attribute did not match the expected value"
    for key in manager.todo_items:
        if key == id_to_edit:
            continue
        assert (
            manager.todo_items[key] == original_items[key]
        ), "An incorrect item was changed"


def test_edit_todo_item_changes_item_complex(
    todo_test_data: List[TodoItem], todo_dto_multi_change: EditTodoItem
):
    """
    Asserts method will change the value of multiple attributes without
    changing other items or incorrect fields
    """
    manager = TodoManager()
    original_items = deepcopy(todo_test_data)
    original_items = fixture_list_to_dict(original_items)
    manager.todo_items = fixture_list_to_dict(todo_test_data)
    id_to_edit = todo_test_data[0].todo_id
    manager.edit_todo_item(id_to_edit, todo_dto_multi_change)

    for attribute in ALLOWED_ATTRIBUTES:
        expected_value = getattr(todo_dto_multi_change, attribute)
        if expected_value is not None:
            actual_value = getattr(manager.todo_items[id_to_edit], attribute)
            assert (
                actual_value == expected_value
            ), f"An attribute '{attribute}' did not match the expected value"

    assert (
        manager.todo_items[id_to_edit] != original_items[id_to_edit]
    ), "The item to edit remained unchanged"
    for key in manager.todo_items:
        if key == id_to_edit:
            continue
        assert (
            manager.todo_items[key] == original_items[key]
        ), f"An incorrect item '{manager.todo_items[key].description}' was changed"
