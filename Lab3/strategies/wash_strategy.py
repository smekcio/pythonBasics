from abc import ABC, abstractmethod


class WashStrategy(ABC):
    def __init__(self):
        super().__init__()
        self._price = 0

    @property
    def price(self):
        return self._price

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class WheelWashStrategy(WashStrategy):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def __call__(self):
        print('Myję koła')


class ChassisWashStrategy(WashStrategy):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def __call__(self):
        print('Myję karoserię')


class StandardWheelWashStrategy(WheelWashStrategy):
    def __init__(self):
        super().__init__()
        self._price += 5

    def __call__(self):
        super().__call__()
        print('Poziom standardowy')


class PremiumWheelWashStrategy(WheelWashStrategy):
    def __init__(self):
        super().__init__()
        self._price += 10

    def __call__(self):
        super().__call__()
        print('Poziom premium')


class StandardChassisWashStrategy(ChassisWashStrategy):
    def __init__(self):
        super().__init__()
        self._price += 15

    def __call__(self):
        super().__call__()
        print('Poziom standardowy')


class PremiumChassisWashStrategy(ChassisWashStrategy):
    def __init__(self):
        super().__init__()
        self._price += 25

    def __call__(self):
        super().__call__()
        print('Poziom premium')
