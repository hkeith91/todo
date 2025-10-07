# TODO: Sort Todo's by priority
# TODO: Sort Todo's by date_date
# TODO: Create multiple lists
from typing import List, Optional
from models.todo_item import TodoItem, EditTodoItem
from datetime import datetime

# Attributes the user is allowed to modify
ALLOWED_ATTRIBUTES = [
    "description",
    "is_complete",
    "due_date",
    "due_time",
    "priority",
    "frequency",
]


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
        item_to_delete = self.get_todo_item_by_id(id_to_delete)
        if item_to_delete is None:
            raise ValueError("Item to delete not found")
        else:
            index = self.todo_list.index(item_to_delete)
            self.todo_list.pop(index)
            return True

    def edit_todo_item(self, id_to_edit: str, edit_todo_item: EditTodoItem):
        item_has_changed = False
        item_to_edit = self.get_todo_item_by_id(id_to_edit)
        if item_to_edit is None:
            raise ValueError("Item to edit not found")

        for attribute_name in ALLOWED_ATTRIBUTES:
            new_value = getattr(edit_todo_item, attribute_name)
            if new_value is not None:
                current_value = getattr(item_to_edit, attribute_name)
                if current_value != new_value:
                    setattr(item_to_edit, attribute_name, new_value)
                    item_has_changed = True

        if item_has_changed:
            item_to_edit.last_updated = datetime.now()
        return item_to_edit
