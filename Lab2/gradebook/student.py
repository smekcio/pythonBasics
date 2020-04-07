from typing import List, Optional
from .grade import Grade
import logging


class Student:

    def __init__(self, index, name):
        self.__id = index
        self.__name = name
        self.__grades: List[Grade] = []
        logging.info('Tworze studenta \"{}\" o id [{}]'.format(name, index))

    def __str__(self):
        return '[{}] {}'.format(self.__id, self.__name)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def grades(self):
        return self.__grades

    def add_grade(self, value, weight):
        if not isinstance(value, int) or not isinstance(weight, int):
            raise Exception('Ocena lub jej waga nie jest liczbą całkowitą')
        elif value not in range(1, 7) or weight not in range(1, 11):
            raise Exception('Ocena lub jej waga poza zakresem\nOcena: 1-6\nWaga: 1-10')
        logging.info('Nadaje {} ocene {} o wadze {}'.format(self.__name, value, weight))
        self.__grades.append(Grade(value, weight))

    def weight_arith_mean(self) -> Optional[float]:
        if len(self.__grades) > 0:
            sum1 = 0
            sum2 = 0
            for g in self.__grades:
                sum1 += g.value * g.weight
                sum2 += g.weight
            return sum1 / sum2
        else:
            return None
