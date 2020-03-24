def fib_gen(N):
    n1 = 0
    n2 = 1
    yield 0
    for n in range(N-1):
        yield n1 + n2
        n1 = n1 + n2
        n2 = n1 - n2

def main():
    print(list(fib_gen(20)))

if __name__ == '__main__':
    main()