def mysort(lista, prio):
    def f(arg):
        if arg in prio:
            return (1, arg)
        return (0, arg)

    lista.sort(key=f)

    for p in prio:
        if p in lista: return True
    else:
        return False

def main():
    q = (1, 2)
    seq = [4, 1, 2, 7, 6]

    print("Prioretyzowana: " + str(mysort(seq, q)) + " " + str(seq))

if __name__ == '__main__':
    main()