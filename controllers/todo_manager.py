# TODO: Add Todo item
# TODO: Get Todo by id
# TODO: Edit Todo by id
# TODO: Delete Todo by id
# TODO: Sort Todo's by priority
# TODO: Sort Todo's by date_date
# TODO: Create multiple lists
from models.todo_item import TodoItem
from typing import List, Optional


class TodoManager:
    def __init__(self):
        self.todo_list = []

    def get_all_todo_items(self) -> List[TodoItem]:
        return self.todo_list

    def get_todo_item_by_id(self, id_to_search: str) -> Optional[TodoItem]:
        return next(
            (item for item in self.todo_list if item.todo_id == id_to_search), None
        )
