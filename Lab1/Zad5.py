def filtruj_pierwsze_v1(lista):
    return list(map(lambda p: p**2, filter(lambda num: all(num % n != 0 for n in range(2, num)) and num > 1, lista)))


def filtruj_pierwsze_v2(lista):
    return [num**2 for num in lista if all(num % n != 0 for n in range(2, num)) and num > 1]


def main():
    lista = range(101)
    # print(filtruj_pierwsze_v1(lista))
    # print(filtruj_pierwsze_v2(lista))
    print(filtruj_pierwsze_v1(lista) == filtruj_pierwsze_v2(lista))


if __name__ == '__main__':
    main()
