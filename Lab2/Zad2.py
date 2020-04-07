from Lab2.stack import StackPlus


def main():
    stack = StackPlus()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print('Minimalna wartość na stosie: {}'.format(stack.min()))

    while not stack.is_empty():
        print(stack.top())
        stack.pop()


if '__main__' == __name__:
    main()
