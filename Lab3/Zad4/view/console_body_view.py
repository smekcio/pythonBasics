from .console_view import ConsoleBodyView


class ConsoleStudentListView(ConsoleBodyView):
    def __init__(self, model):
        super().__init__('student_list', model)
        self.full_name = 'Lista studentów'
        from Lab3.Zad4.app import ConsoleMenu
        self.body_view_type = ConsoleMenu.STUDENT_LIST
        self.__student_list = None

    def update(self, student_list):
        self.__student_list = student_list

    def show(self):
        if self.__student_list is None or len(self.__student_list) == 0:
            print('Lista studentów pusta.\n[A] Dodaj studenta [M] Menu [q] Wyjście')
            return
        for student in self.__student_list:
            print('[{0}] {1}'.format(student[0], student[1]))
        print('Aby sprawdzić oceny ucznia wprowadź jego numer identyfikacyjny\n[A] Dodaj studenta [M] Menu [q] Wyjście')


class ConsoleGradeListView(ConsoleBodyView):
    def __init__(self, model):
        super().__init__('grade_list', model)
        self.full_name = 'Lista ocen studenta'
        from Lab3.Zad4.app import ConsoleMenu
        self.body_view_type = ConsoleMenu.GRADE_LIST
        self.__grade_list = None

    def update(self, grade_list):
        self.__grade_list = grade_list

    def show(self):
        if len(self.__grade_list) == 0:
            print('Brak ocen')
        else:
            for student in self.__grade_list:
                print('{0} (Waga {1})'.format(student[0], student[1]))
        print('[G] Dodaj ocenę [R] Usuń studenta [M] Menu [S] Lista studentów [q] Wyjście')


class ConsoleReportView(ConsoleBodyView):
    def __init__(self, model):
        super().__init__('report', model)
        self.full_name = 'Raport ocen'
        from Lab3.Zad4.app import ConsoleMenu
        self.body_view_type = ConsoleMenu.REPORT
        self.__report = None

    def update(self, report):
        self.__report = report

    def show(self):
        self.model.report()
        if self.__report is None or len(self.__report) == 0:
            print('Nie można wygenerować raportu')
            print('[M] Menu [q] Wyjście')
            return
        for student in self.__report:
            print('[{0}] {1}: {2}'.format(student[0], student[1], student[2]))
        print('[M] Menu [q] Wyjście')


class ConsoleMainView(ConsoleBodyView):
    def __init__(self, model=None):
        super().__init__('main', model)
        self.pre_view = True
        self.full_name = 'Menu główne'
        from Lab3.Zad4.app import ConsoleMenu
        self.body_view_type = ConsoleMenu.MAIN_MENU
        self.__menu = []
        for el in ConsoleMenu.MENU()[ConsoleMenu.MAIN_MENU]:
            self.__menu.append(el[2])

    def update(self, report):
        pass

    def show(self):
        for k, pos in enumerate(['S', 'R', 'A']):
            print('[{1}] - {0}'.format(self.__menu[k], pos))


class ConsoleAddStudentView(ConsoleBodyView):
    def __init__(self, model=None):
        super().__init__('add', model)
        self.pre_view = False
        self.full_name = 'Dodaj nowego studenta'
        self.__input = 1
        from Lab3.Zad4.app import ConsoleMenu
        self.body_view_type = ConsoleMenu.ADD_STUDENT

    @property
    def input(self):
        return self.__input

    def update(self):
        pass

    def show(self):
        print('Podaj imię i nazwisko')


class ConsoleGradeStudentView(ConsoleBodyView):
    def __init__(self, model=None):
        super().__init__('grade_student', model)
        self.pre_view = False
        self.full_name = 'Dodaj ocenę'
        from Lab3.Zad4.app import ConsoleMenu
        self.body_view_type = ConsoleMenu.GRADE_STUDENT

    def update(self):
        pass

    def show(self):
        print('Podaj ocenę i jej wagę oddzielone spacją')
