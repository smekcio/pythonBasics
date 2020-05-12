from .abstract_app import AbstractApp
from Lab3.Zad4.model import GradebookModel
from Lab3.Zad4.view import ConsoleMainView, ConsoleReportView,\
                           ConsoleGradeListView, ConsoleStudentListView, ConsoleView,\
                           ConsoleAddStudentView, ConsoleGradeStudentView
from Lab3.Zad4.controller import ConsoleController, ConsoleInputController


class ConsoleApp(AbstractApp):
    def __init__(self, controller: ConsoleController):
        super().__init__(controller)
        self.__inputController = ConsoleInputController()
        self.__menuController = controller
        self.__model = GradebookModel('Dziennik elektroniczny WSB')
        self.__controller = controller

        from Lab3.Zad4.app import ConsoleMenu
        consoleview = ConsoleView(ConsoleMenu.MAIN_MENU, self.__model)

        self.__mainView = ConsoleMainView()
        consoleview.add_component(self.__mainView)

        self.__studentListView = ConsoleStudentListView(self.__model)
        self.__reportView = ConsoleReportView(self.__model)
        self.__addStudentView = ConsoleAddStudentView(self.__model)
        self.__gradeListView = ConsoleGradeListView(self.__model)
        self.__gradeStudentView = ConsoleGradeStudentView(self.__model)
        self.__bodyViews = []
        self.__bodyViews.append(self.__studentListView)
        self.__bodyViews.append(self.__reportView)
        self.__bodyViews.append(self.__mainView)
        self.__bodyViews.append(self.__addStudentView)
        self.__bodyViews.append(self.__gradeListView)
        self.__bodyViews.append(self.__gradeStudentView)

        self.__model.add_view(self.__studentListView)
        self.__model.add_view(self.__reportView)
        self.__model.add_view(self.__gradeListView)

        self.__view = consoleview

        controller.view = self.__view
        controller.model = self.__model
        self.__inputController.model = self.__model
        self.__inputController.view = self.__view

    def __switch_view(self, new_view):
        for component in self.__view.get_children():
            if component.name != 'title':
                self.__view.remove_component(component)
                break
        self.__view.add_component(new_view)

    def run_app(self):
        for view in self.__view.get_children():
            if view.pre_view:
                self.__view.show()
        while self.controller.get_user_input():
            self.controller.reply()
            from Lab3.Zad4.app import ConsoleMenu
            for view in self.__bodyViews:
                if view.body_view_type == self.controller.select:
                    self.__switch_view(view)
                    break
            if self.controller.select == ConsoleMenu.MAIN_MENU:
                self.controller = self.__menuController
            elif self.controller.select == ConsoleMenu.ADD_STUDENT:
                # Poprzednie menu
                self.controller.select = ConsoleMenu.MAIN_MENU
                # Tryb input
                self.__inputController.select = ConsoleMenu.ADD_STUDENT
                # Ilość parametrów
                self.__inputController.no_parameters = 2

                self.controller = self.__inputController
            elif self.controller.select == ConsoleMenu.STUDENT_LIST:
                # Poprzednie menu
                self.controller.select = ConsoleMenu.MAIN_MENU
                # Tryb input
                self.__inputController.select = ConsoleMenu.STUDENT_LIST
                # Ilość parametrów
                self.__inputController.no_parameters = 1

                self.controller = self.__inputController
            elif self.controller.select == ConsoleMenu.GRADE_LIST:
                # Poprzednie menu
                self.controller.select = ConsoleMenu.STUDENT_LIST
                # Tryb input
                self.__inputController.select = ConsoleMenu.GRADE_LIST
                # Ilość parametrów
                self.__inputController.no_parameters = 1

                self.controller = self.__inputController
            elif self.controller.select == ConsoleMenu.GRADE_STUDENT:
                # Poprzednie menu
                self.controller.select = ConsoleMenu.STUDENT_LIST
                # Tryb input
                self.__inputController.select = ConsoleMenu.GRADE_STUDENT
                # Ilość parametrów
                self.__inputController.no_parameters = 2

                self.controller = self.__inputController
            self.__view.show()
