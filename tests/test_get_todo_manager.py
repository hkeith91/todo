from models.todo_manager import TodoManager
from models.todo_item import TodoItem
from typing import List
from copy import deepcopy
from tests.fixtures import todo_test_data


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


def test_get_all_todo_items_returns_list(todo_test_data: List[TodoItem]):
    """Asserts that a List object is the return value"""
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
    todo_list_to_test = manager.get_all_todo_items()

    assert isinstance(
        todo_list_to_test, List
    ), "TodoManager did not return data of type List"


def test_get_all_todo_items_returns_todo_item_objects(todo_test_data: List[TodoItem]):
    """Asserts that returned List items are all instances of TodoItem objects"""
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
    todo_list_to_test = manager.get_all_todo_items()

    assert all(
        isinstance(item, TodoItem) for item in todo_list_to_test
    ), "Every item in list must be a TodoItem instance"


def test_get_all_todo_items_returns_correct_count(todo_test_data: List[TodoItem]):
    """Asserts the returned List object contains the correct number or elements"""
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
    todo_list_to_test = manager.get_all_todo_items()

    assert len(todo_list_to_test) == len(
        todo_test_data
    ), "Returned list length must match test fixture length"


def test_get_all_todo_items_returns_correct_content(todo_test_data: List[TodoItem]):
    """Asserts all elements in returned List are the correct elements"""
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
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
    manager.todo_list = deepcopy(todo_test_data)
    test_todo_item = todo_test_data[0]
    todo_item_to_test = manager.get_todo_item_by_id(test_todo_item.todo_id)

    assert isinstance(todo_item_to_test, TodoItem), "Item must be of instance TodoItem"


def test_get_todo_item_by_id_returns_correct_object(todo_test_data: List[TodoItem]):
    """Asserts the correct TodoItem is returned"""
    manager = TodoManager()
    manager.todo_list = deepcopy(todo_test_data)
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
    manager.todo_list = deepcopy(todo_test_data)

    non_existent_id = "Does not exist"
    item_to_test = manager.get_todo_item_by_id(non_existent_id)

    assert (
        item_to_test is None
    ), "Method must return None when searching ID that does not exist"
