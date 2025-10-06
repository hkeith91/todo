# TODO: Edit Todo by id
# TODO: Delete Todo by id
# TODO: Sort Todo's by priority
# TODO: Sort Todo's by date_date
# TODO: Create multiple lists
from typing import List, Optional

from black.comments import children_contains_fmt_on

from models.todo_item import TodoItem


class TodoManager:
    def __init__(self):
        self.todo_list = []

    def check_id_is_unique(self, id_to_check: str) -> bool:
        todo_id_set = {item.todo_id for item in self.todo_list}
        initial_length = len(todo_id_set)
        todo_id_set.add(id_to_check)
        return len(todo_id_set) == initial_length + 1

    def get_all_todo_items(self) -> List[TodoItem]:
        return self.todo_list

    def get_todo_item_by_id(self, id_to_search: str) -> Optional[TodoItem]:
        return next(
            (item for item in self.todo_list if item.todo_id == id_to_search), None
        )

    def add_todo_item(self, item_to_add: TodoItem) -> Optional[TodoItem]:
        if item_to_add.todo_id is None:
            item_to_add.todo_id = TodoItem.generate_unique_id()

        if self.check_id_is_unique(item_to_add.todo_id):
            self.todo_list.append(item_to_add)
            return item_to_add
        else:
            raise ValueError("Supplied todo_id already exists in Manager list")

    def delete_todo_item(self, id_to_delete):
        pass
