from .abstract_controller import AbstractController


class ConsoleInputController(AbstractController):
    def __init__(self):
        super().__init__()
        self.__no_parameters = 0
        from Lab3.Zad4.app import ConsoleMenu
        self.__select = ConsoleMenu.MAIN_MENU
        self.__student = None

    @property
    def no_parameters(self):
        return self.__no_parameters

    @no_parameters.setter
    def no_parameters(self, new_no_parameters):
        self.__no_parameters = new_no_parameters

    def get_user_input(self):
        while True:
            obj = input('Wprowadź ({}) dane: '.format(self.__no_parameters))
            obj = obj.split(' ')
            if len(obj) == self.__no_parameters:
                from Lab3.Zad4.app import ConsoleMenu
                if self.select == ConsoleMenu.ADD_STUDENT:
                    name = '{0} {1}'.format(obj[0], obj[1])
                    self.model.add_student(name)
                    self._set_reply('Pomyślnie dodano studenta {}'.format(name))
                    self.select = ConsoleMenu.MAIN_MENU
                    break
                if self.select == ConsoleMenu.STUDENT_LIST:
                    if str(obj[0]).isnumeric():
                        self.__student = int(obj[0])
                        self.model.student_grade_list(int(obj[0]))
                        self._set_reply('Wyświetlam dane studenta {}'.format(obj[0]))
                        self.select = ConsoleMenu.GRADE_LIST
                        break
                    elif obj[0] == 'A':
                        self.select = ConsoleMenu.ADD_STUDENT
                        break
                    elif obj[0] == 'M':
                        self.select = ConsoleMenu.MAIN_MENU
                        break
                    elif obj[0] == 'q':
                        print('Wyjście z programu')
                        return False
                    else:
                        print('Nie podano numeru')
                        continue
                if self.select == ConsoleMenu.GRADE_LIST:
                    if obj[0] == 'M':
                        self.select = ConsoleMenu.MAIN_MENU
                        break
                    if obj[0] == 'S':
                        self.select = ConsoleMenu.STUDENT_LIST
                        break
                    if obj[0] == 'G':
                        self.select = ConsoleMenu.GRADE_STUDENT
                        self._set_reply('Wybrano studenta o ID: {}'.format(self.__student))
                        break
                    if obj[0] == 'R':
                        self.model.remove_student(self.__student)
                        self._set_reply('Usunięto studenta o ID {}'.format(self.__student))
                        self.__student = None
                        self.select = ConsoleMenu.STUDENT_LIST
                        break
                    if obj[0] == 'q':
                        print('Wyjście z programu')
                        return False
                if self.select == ConsoleMenu.GRADE_STUDENT:
                    if len(obj) == 2:
                        self.model.grade_student(self.__student, int(obj[0]), int(obj[1]))
                        self._set_reply('Dodano ocenę {} o wadze {} studentowi {}'
                                        .format(obj[0], obj[1], self.__student))
                        self.select = ConsoleMenu.GRADE_LIST
                        break
                    else:
                        if obj[0] == 'M':
                            self.select = ConsoleMenu.MAIN_MENU
                            break
                        if obj[0] == 'S':
                            self.select = ConsoleMenu.STUDENT_LIST
                            break
                        elif obj[0] == 'q':
                            print('Wyjście z programu')
                            return False
            else:
                print('Błąd! Spróbuj ponownie')
        return True
