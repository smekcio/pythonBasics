from Lab3.composite import Leaf, Composite


def main():
    # Użyłem własnej architektury, gdyż nie zrozumiałem sensu zaproponowanej

    workstation = Composite('Stacja robocza', price=0)

    input_devices = Composite('Urządzenia wejścia', price=0)
    mouse = Leaf('Myszka', price=5)
    keyboard = Leaf('Klawiatura', price=10)

    output_devices = Composite('Urządzenia wyjścia', price=0)
    display = Leaf('Monitor', price=100)
    printer = Leaf('Drukarka', price=40)

    computer = Composite('Komputer', price=0)
    case = Leaf('Obudowa', price=40)
    power_supply = Leaf('Zasilacz', price=60)
    motherboard = Composite('Płyta główna', price=70)
    cpu = Leaf('Procesor', price=110)
    gpu = Leaf('Karta graficzna', price=170)
    memory = Composite('Pamięć', price=60)
    ssd = Leaf('SSD', price=50)
    ram = Leaf('RAM', price=60)

    workstation.add_component(input_devices)
    workstation.add_component(output_devices)
    workstation.add_component(computer)

    input_devices.add_component(mouse)
    input_devices.add_component(keyboard)
    output_devices.add_component(display)
    output_devices.add_component(printer)
    computer.add_component(motherboard)
    motherboard.add_component(cpu)
    motherboard.add_component(memory)
    memory.add_component(ssd)
    memory.add_component(ram)
    motherboard.add_component(gpu)
    computer.add_component(case)
    computer.add_component(power_supply)

    print('-- Nazwa [cena własna i komponentów] --', end='\n\n')
    workstation.do_operation()


if __name__ == '__main__':
    main()
