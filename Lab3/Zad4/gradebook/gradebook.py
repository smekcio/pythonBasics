from typing import Dict
from .student import Student
import copy
import logging


class GradeBook:
    def __init__(self, name, student_list=None):
        self.__name = name
        self.__student_list: Dict[int] = student_list if student_list is not None else dict()
        logging.info('Tworze dziennik \"{}\"'.format(name))

    def add_student(self, student):
        if isinstance(student, str):
            new_id = 1 if len(self.__student_list) == 0 else max(self.__student_list.keys()) + 1
            self.__student_list[new_id] = Student(new_id, student)
        elif isinstance(student, Student):
            if int(student.id) == len(self.__student_list)+1:
                self.__student_list[student.id] = student
            else:
                raise Exception('Nieprawidlowa numeracja uczniów')

    def remove_student(self, student: Student):
        if isinstance(student, int):
            if student in self.__student_list.keys():
                if student == max(self.__student_list.keys()):
                    self.__student_list[student] = None
                else:
                    del self.__student_list[student]
            else:
                raise Exception('Nie ma studenta o takim id')
        elif isinstance(student, Student):
            if student in self.__student_list.values():
                del self.__student_list[student.id]
            else:
                raise Exception('Nie ma takiego studenta na liście')

    @property
    def name(self):
        return self.__name

    @property
    def student_list(self):
        return self.__student_list

    def __get_student(self, value) -> Student:
        # Na podstawie instancji
        if isinstance(value, Student):
            return value
        # Na podstawie ID
        if isinstance(value, int):
            if value in self.__student_list.keys():
                return self.__student_list[value]
            else:
                raise Exception('Nie ma studenta o takim ID')
        # Na podstawie nazwy
        elif isinstance(value, str):
            for student in self.__student_list.values():
                if student.name is value:
                    return student
            raise Exception('Nie ma takiego studenta')
        else:
            raise Exception('Nieznany typ identyfikujący studenta')

    def grade_student(self, student, grade, weight):
        student = self.__get_student(student)
        if student is not None:
            student.add_grade(grade, weight)

    def list_grades(self, student):
        student = self.__get_student(student)
        # print('\nOceny studenta {} o id {}:'.format(student.name, student.id))
        grades_list = []
        for g in student.grades:
            grades_list.append((g.value, g.weight))
            # print('{} ({})'.format(g.value, g.weight))
        if len(student.grades) == 0:
            # print('Brak ocen')
            pass
        return grades_list

    def get_report(self):
        report = []
        # print('\n{}\nŚrednia ważona ocen uzyskanych przez uczniow:'.format(self.__name))
        for s in self.__student_list.values():
            if s is not None:
                g = s.weight_arith_mean() if s.weight_arith_mean() is not None else 'Brak ocen'
                report.append((s.id, s.name, g))
                # print('[{}] {}: {}'.format(s.id, s.name, g))
        return report

    @classmethod
    def based_gradebook(cls, name, book):
        return cls(name, student_list=copy.deepcopy(book.student_list))
