class Subject:
    def __init__(self):
        self.__observerList = []

    def register_observer(self, observer):
        self.__observerList.append(observer)

    def unregister_observer(self, observer):
        self.__observerList.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self.__observerList:
            observer.update(*args, **kwargs)
