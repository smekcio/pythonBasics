from functools import wraps

def decorator(func):
    licznik = dict()
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal licznik
        licznik[func.__name__] = licznik[func.__name__] + 1 if func.__name__ in licznik else 1
        print("Funkcję {} wywołano {} razy".format(func.__name__, licznik[func.__name__]), end=' ')
        func(*args, **kwargs)
        print()
    return wrapper

@decorator
def f():
    pass

@decorator
def g():
    pass

def main():
    f()
    f()
    g()
    f()
    g()

if __name__ == '__main__':
    main()