from Lab3.observer import ProgressObserver, Subject


def main():
    subject = Subject()
    observer1 = ProgressObserver('1')
    observer2 = ProgressObserver('2')
    subject.register_observer(observer1)
    subject.register_observer(observer2)
    subject.notify(range(200))
    subject.notify(range(20))


if __name__ == '__main__':
    main()
