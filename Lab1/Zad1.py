def print_room(height, width):
    for h in range(height + 1):
        for w in range(width + 1):
            if w % width == 0 and h % height == 0:
                print('*', end='')
            elif w % width == 0:
                print('|', end='')
            elif h % height == 0:
                print('-', end='')
            else:
                print(' ', end='')
        print('')


def main():
    height = int(input('Give height: '))
    width = int(input('Give width: '))
    print_room(height + 1, width + 1)


if __name__ == '__main__':
    main()