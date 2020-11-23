from typing import List

from menu.menu_item import MenuItem


class Menu:
    items: List[MenuItem]

    def __init__(self, items: List[MenuItem], parent=None):
        self.items = items
        self.parent = parent

    def display(self):
        self.print_parent_text()
        self.__print()
        n = len(self.items)
        entry = self.__receive_valid_input(n)
        self.handle_entry(entry)

    def handle_entry(self, entry):
        if entry == 0:
            if self.parent is None:
                exit(0)
            else:
                self.parent.display()
        else:
            self.items[entry - 1].invoke()

    def print_parent_text(self):
        if self.parent is None:
            print("0. Quit the application")
        else:
            print("0. Return to previous menu")

    @staticmethod
    def __receive_valid_input(n: int) -> int:
        entry = -1
        is_valid_integer = True
        while entry < 0 or entry > n or not is_valid_integer:
            entry = input(f"Choose an option from above [1-{n}]: ")
            try:
                entry = int(entry)
                is_valid_integer = True
            except ValueError:
                entry = -1
                is_valid_integer = False
        return entry

    def __print(self):
        i = 1
        for item in self.items:
            print(f"{i}. {item.name}")
            i += 1
