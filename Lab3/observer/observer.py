from abc import ABC, abstractmethod
from progressbar import progressbar
from time import sleep


class Observer:
    def __init__(self):
        super().__init__()

    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class ProgressObserver(Observer):
    def __init__(self, name):
        super().__init__()
        self.__name = name

    def update(self, *args, **kwargs):
        # Nie wiem skąd wynikają błędy
        # N/A% (0 of 20) |                         | Elapsed Time: 0:00:00 ETA:  --:--:--

        print('\nobserver {}\ngot {}'.format(self.__name, args[0]))
        for i in progressbar(args[0]):
            sleep(0.02)
