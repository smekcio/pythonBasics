def word_counter(file_name):
    counter = 0
    try:
        with open(file_name, encoding='UTF-8') as tf:
            for line in tf:
                counter += len([word for word in line.strip().split(' ') if word])
    except FileNotFoundError as Ex:
        print(Ex)
        return counter-1
    return counter

def main():
    file = 'pan-tadeusz.txt'
    print("Liczba słów w pliku {}: {}".format(file, word_counter(file)))

if __name__ == '__main__':
    main()