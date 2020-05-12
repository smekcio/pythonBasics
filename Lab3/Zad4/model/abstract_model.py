from abc import ABC, abstractmethod


class AbstractModel(ABC):
    def __init__(self):
        super().__init__()
        self._views = dict()

    def add_view(self, new_view):
        if new_view not in self._views:
            self._views[new_view.name] = new_view

    def remove_view(self, view):
        if view.name in self._views:
            del self._views[view.name]

    @abstractmethod
    def notify(self, action, data):
        pass
