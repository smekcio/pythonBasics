from enum import Enum


class ConsoleMenu(Enum):
    MAIN_MENU = 1
    STUDENT_LIST = 2
    REPORT = 3
    ADD_STUDENT = 4
    GRADE_LIST = 5
    GRADE_STUDENT = 6

    # Pozostałości / Zrezygnowałem z tego pomysłu
    @staticmethod
    def MENU():
        menu = dict()
        menu[ConsoleMenu.MAIN_MENU] = (
                    ('1', ConsoleMenu.STUDENT_LIST, 'Lista studentów'),
                    ('2', ConsoleMenu.REPORT, 'Raport ocen'),
                    ('3', ConsoleMenu.ADD_STUDENT, 'Dodaj nowego studenta')
                )
        menu[ConsoleMenu.STUDENT_LIST] = (
                    ('M', ConsoleMenu.MAIN_MENU)
                )
        menu[ConsoleMenu.REPORT] = (
            (
                ('M', ConsoleMenu.MAIN_MENU)
            )
        )
        return menu
