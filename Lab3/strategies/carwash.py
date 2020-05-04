from .wash_strategy import ChassisWashStrategy, WheelWashStrategy


class CarWash:
    def __init__(self):
        self.__wheel_wash_strategy = None
        self.__chassis_wash_strategy = None

    def define_wheel_wash_strategy(self, wheel_wash_strategy: WheelWashStrategy):
        if issubclass(wheel_wash_strategy.__class__, WheelWashStrategy):
            self.__wheel_wash_strategy = wheel_wash_strategy
        else:
            print('Nieprawidłowy program mycia kół')

    def define_chassis_wash_strategy(self, chassis_wash_strategy: ChassisWashStrategy):
        if issubclass(chassis_wash_strategy.__class__, ChassisWashStrategy):
            self.__chassis_wash_strategy = chassis_wash_strategy
        else:
            print('Nieprawidłowy program mycia karoserii')

    def run(self):
        print('Start programu')
        price = 0
        for wash in [self.__wheel_wash_strategy, self.__chassis_wash_strategy]:
            if wash is not None:
                wash()
                price += wash.price
        print('Należy się {}\n'.format(price))
