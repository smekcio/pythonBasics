from functools import wraps

N = 20


class Descriptor:
    licznik = dict()

    def __init__(self, func):
        self.__func = func
        wraps(self.__func)

    def __call__(self, *args, **kwargs):
        self.licznik[self.__func.__name__] = self.licznik[self.__func.__name__] + 1 \
            if self.__func.__name__ in self.licznik else 1
        print("Funkcję {} wywołano {} razy".format(self.__func.__name__, self.licznik[self.__func.__name__]), end=' ')
        return self.__func(*args, **kwargs)


class FibIter:
    def __init__(self, max_num):
        self.__n1 = 0
        self.__n2 = 1
        self.__num = 0
        self.__max_num = max_num

    def __next__(self):
        self.__num += 1
        if self.__num == 1:
            return 0
        elif self.__num <= self.__max_num:
            temp = self.__n1 + self.__n2
            self.__n1 = self.__n1 + self.__n2
            self.__n2 = self.__n1 - self.__n2
            # print("temp:{}, n1:{}, n2:{}".format(temp, self.__n1, self.__n2))
            return temp
        else:
            raise StopIteration

    def __iter__(self):
        return self


@Descriptor
def f():
    pass


def main():
    obj = FibIter(N)
    # it = iter(obj)  # opcjonalne

    for i, el in enumerate(obj):
        f()
        print("\t| Fibonacci {} = {}".format(i, el))


if __name__ == '__main__':
    main()
