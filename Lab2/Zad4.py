from Lab2.productionline import ProductionLine, ResizeProcess, RotateProcess, InvertProcess, SmoothProcess
from cv2 import cv2
import logging


def main():
    logging.basicConfig(level=logging.DEBUG)

    # Tworzenie "linii produkcyjnej"
    pl = ProductionLine('./lena.jpg')

    # Dodanie kroków produkcyjnych
    pl.add_process(RotateProcess(cv2.ROTATE_90_CLOCKWISE))
    pl.add_process(ResizeProcess(3, 2))
    pl.add_process(InvertProcess())
    pl.add_process(SmoothProcess(11))

    # Uruchomienie procesów
    pl.run()

    # Wyświetlenie rezultatu
    pl.show()


if '__main__' == __name__:
    main()
