from .abstract_model import AbstractModel
from Lab3.Zad4.gradebook import GradeBook


class GradebookModel(AbstractModel):
    def __init__(self, name):
        super().__init__()
        self.__gradebook = GradeBook(name)

    @property
    def gradebook(self):
        return self.__gradebook

    @gradebook.setter
    def gradebook(self, new_gradebook):
        self.gradebook = new_gradebook

    def notify(self, action, data=None):
        for view in self._views.values():
            if action == view.body_view_type.value:
                view.update(data)

    def add_student(self, student):
        self.__gradebook.add_student(student)
        self.student_list()

    def remove_student(self, student):
        self.__gradebook.remove_student(student)
        self.student_list()

    def student_list(self):
        new_list = []
        for identyfikator, name in self.__gradebook.student_list.items():
            if name is not None:
                new_list.append((identyfikator, name.name))
        self.notify(2, data=new_list)

    def grade_student(self, student, grade, weight=1):
        self.__gradebook.grade_student(student, grade, weight)
        self.student_grade_list(student)

    def student_grade_list(self, student):
        grade_list = self.__gradebook.list_grades(student)
        self.notify(5, data=grade_list)

    def report(self):
        report = self.__gradebook.get_report()
        self.notify(3, data=report)
