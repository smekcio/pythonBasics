from Lab3.Zad4.app import ConsoleApp
from Lab3.Zad4.controller import ConsoleController


def main():
    controller = ConsoleController()
    consoleapp = ConsoleApp(controller)
    consoleapp.run_app()


if __name__ == '__main__':
    main()
