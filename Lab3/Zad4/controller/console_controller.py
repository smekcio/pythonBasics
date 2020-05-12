from .abstract_controller import AbstractController


class ConsoleController(AbstractController):
    def __init__(self):
        super().__init__()

        from Lab3.Zad4.app import ConsoleMenu
        self.select = ConsoleMenu.MAIN_MENU

    def get_user_input(self):
        from Lab3.Zad4.app import ConsoleMenu
        obj = input('Wybierz: ')
        if obj == 'q':
            print('Wyjście z programu')
            return False
        if obj == 'M':
            self.select = ConsoleMenu.MAIN_MENU
            return True
        else:
            if self.select == ConsoleMenu.MAIN_MENU:
                if obj == 'S':
                    self.select = ConsoleMenu.STUDENT_LIST
                    return True
                if obj == 'R':
                    self.select = ConsoleMenu.REPORT
                    return True
                if obj == 'A':
                    self.select = ConsoleMenu.ADD_STUDENT
                    return True
                else:
                    return True
