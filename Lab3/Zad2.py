from Lab3.strategies import CarWash, StandardWheelWashStrategy, PremiumWheelWashStrategy, StandardChassisWashStrategy, PremiumChassisWashStrategy

def main():
    carwash = CarWash()
    carwash.define_chassis_wash_strategy(StandardChassisWashStrategy())
    carwash.run()

    carwash.define_wheel_wash_strategy(StandardWheelWashStrategy())
    carwash.run()

    carwash.define_wheel_wash_strategy(PremiumWheelWashStrategy())
    carwash.define_chassis_wash_strategy(PremiumChassisWashStrategy())
    carwash.run()


if __name__ == '__main__':
    main()