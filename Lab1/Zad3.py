def unique_elements(lista):
    seq2 = set()
    for el in lista:
        if not el in list(seq2):
            seq2.add(el)
        else:
            lista.remove(el)
    print(lista)


def main():
    seq = list(range(20))
    seq.append(5)
    print(seq)
    unique_elements(seq)


if __name__ == '__main__':
    main()