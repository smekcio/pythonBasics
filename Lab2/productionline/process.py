from abc import ABC, abstractmethod
from cv2 import cv2
import logging


class Process(ABC):
    def __init__(self):
        self._img = None

    @abstractmethod
    def run(self):
        pass

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        self._img = value
        # logging.info('Ustalono img {}'.format(id(self._img)))


class RotateProcess(Process):
    def __init__(self, degree):
        super().__init__()
        self.__degree = degree

    def run(self):
        logging.info('Obrócono')
        self._img = cv2.rotate(self._img, self.__degree)
        return self._img


class ResizeProcess(Process):
    def __init__(self, x, y):
        super().__init__()
        self.__x = x
        self.__y = y

    def run(self):
        logging.info('Przeskalowano')
        self._img = cv2.resize(self._img, None, fx=self.__x, fy=self.__y)
        return self._img


class InvertProcess(Process):
    def __init__(self):
        super().__init__()

    def run(self):
        logging.info('Odwrócono kolory')
        self._img = cv2.bitwise_not(self._img)
        return self._img


class SmoothProcess(Process):
    def __init__(self, gauss):
        super().__init__()
        if not gauss % 2:
            gauss += 1  # Wartość musi byc nieparzysta
        self.__gauss = gauss

    def run(self):
        logging.info('Wygładzono')
        self.img = cv2.GaussianBlur(self._img, (self.__gauss, self.__gauss), cv2.BORDER_DEFAULT)
        return self.img
