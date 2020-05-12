from abc import ABC, abstractmethod
from Lab3.Zad4.model import AbstractModel


class AbstractView(ABC):
    def __init__(self, name, model: AbstractModel):
        super().__init__()
        self.__name = name
        self.__model = model
        self.__components = dict()
        self.__pre_view = False

    @property
    def pre_view(self):
        return self.__pre_view

    @pre_view.setter
    def pre_view(self, b: bool):
        self.__pre_view = b

    @property
    def name(self):
        return self.__name

    @property
    def model(self):
        return self.__model

    @property
    def components(self):
        return self.__components

    def get_children(self):
        return self.__components.values()

    def remove_component(self, value):
        if isinstance(value, str) and value in self.__components:
            del self.__components[value]
        elif value in self.__components.values():
            del self.__components[value.name]

    @abstractmethod
    def add_component(self, component):
        if component.name not in self.__components:
            self.__components[component.name] = component

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def show(self):
        pass
