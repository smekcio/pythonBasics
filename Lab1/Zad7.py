from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Wywołano {} z argumentami:".format(func.__name__), end=' ')
        for arg in args:
            print(arg, end=' ')
        for key, value in kwargs.items():
            print("{}={}".format(key, value), end=' ')
        print()
        func(*args, **kwargs)
    return wrapper

@decorator
def f(a,b,c,d):
    print()

def main():
    f(1,2,c=3,d=4)

if __name__ == '__main__':
    main()