from .process import Process
from cv2 import imread, imwrite, cv2


class ProductionLine:
    def __init__(self, file):
        self.finished = False
        self.__product = imread(file)
        self.__processList = []

    def add_process(self, process: Process):
        self.__processList.append(process)

    def show(self):
        cv2.imshow("Wynik", self.__product)
        cv2.waitKey(0)

    def run(self):
        for process in self.__processList:
            process.img = self.__product
            self.__product = process.run()

        imwrite('./lena2.jpg', self.__product)
        self.finished = True
