from abc import ABC, abstractmethod


class AbstractController(ABC):
    def __init__(self, model=None, view=None):
        super().__init__()
        self.__model = model
        self.__view = view
        self.__select = None
        self._reply = None

    @property
    def select(self):
        return self.__select

    def reply(self):
        if self._reply is not None:
            print(self._reply)
            self._reply = None

    def _set_reply(self, new_reply):
        self._reply = new_reply

    @select.setter
    def select(self, new_select):
        self.__select = new_select

    @abstractmethod
    def get_user_input(self):
        pass

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, new_view):
        self.__view = new_view
