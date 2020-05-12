from abc import abstractmethod
from .abstract_view import AbstractView
from Lab3.Zad4.model import GradebookModel


class ConsoleView(AbstractView):
    def __init__(self, name, model=None):
        super().__init__(name, model)
        self.__name = name
        super().add_component(ConsoleTitleView('title', model))

    @property
    def name(self):
        return self.__name

    def update(self, *args, **kwargs):
        pass

    def show(self):
        for component in self.get_children():
            component.show()

    def add_component(self, component):
        if len(self.get_children()) is 1:
            super().add_component(component)
            self.components['title'].update(component.full_name)
        else:
            raise Exception('ConsoleView może mieć tylko jeden komponent - zawartość widoku. '
                            'Najpierw usuń poprzedni widok')


class ConsoleTitleView(AbstractView):
    def __init__(self, name, model):
        super().__init__(name, model)
        self.__title = ''

    def add_component(self, component):
        pass

    def update(self, *args, **kwargs):
        self.__title = args[0]

    def show(self):
        print('\n--- {0} ---'.format(self.__title))


class ConsoleBodyView(AbstractView):
    def __init__(self, name, model: GradebookModel):
        super().__init__(name, model)
        self.__body_view_type = None
        self.__full_name = ''

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, new_full_name):
        self.__full_name = new_full_name

    @property
    def body_view_type(self):
        return self.__body_view_type

    @body_view_type.setter
    def body_view_type(self, new_update_type):
        self.__body_view_type = new_update_type

    def add_component(self, component):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def show(self):
        pass
