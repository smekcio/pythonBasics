from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, name, depth=1, price=0):
        super().__init__()
        self._name = name
        self._depth = depth
        self._price = price

    @property
    def price(self):
        return self._price

    @abstractmethod
    def do_operation(self):
        pass

    def get_children(self):
        return []
