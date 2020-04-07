from typing import List
from .student import Student
import copy
import logging


class GradeBook:
    def __init__(self, name, student_list=None):
        self.__name = name
        self.__student_list: List[Student] = student_list if student_list is not None else []
        logging.info('Tworze dziennik \"{}\"'.format(name))

    def add_student(self, name):
        if isinstance(name, str):
            self.__student_list.append(Student(len(self.__student_list)+1, name))
        elif isinstance(name, Student):
            if int(name.id) == len(self.__student_list)+1:
                self.__student_list.append(name)
            else:
                raise Exception('Nieprawidlowa numeracja uczniów')
        else:
            raise Exception('Nieznany typ identyfikujący studenta')

    @property
    def name(self):
        return self.__name

    @property
    def student_list(self):
        return self.__student_list

    def __get_student(self, value) -> Student:
        # Na podstawie instancji
        if isinstance(value, Student):
            if value in self.__student_list:
                return value
        # Na podstawie ID
        if isinstance(value, int):
            if 1 <= value <= len(self.__student_list):
                return self.__student_list[value-1]
            else:
                raise Exception('ID poza zakresem')
        # Na podstawie nazwy
        elif isinstance(value, str):
            for student in self.__student_list:
                if student.name == value:
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
        print('\nOceny studenta {} o id {}:'.format(student.name, student.id))
        for g in student.grades:
            print('{} ({})'.format(g.value, g.weight))
        if len(student.grades) == 0:
            print('Brak ocen')

    def get_report(self):
        print('\n{}\nŚrednia ważona ocen uzyskanych przez uczniow:'.format(self.__name))
        for s in self.__student_list:
            g = s.weight_arith_mean() if s.weight_arith_mean() is not None else 'Brak ocen'
            print('[{}] {}: {}'.format(s.id, s.name, g))

    @classmethod
    def based_gradebook(cls, name, book):
        return cls(name, student_list=copy.deepcopy(book.student_list))
