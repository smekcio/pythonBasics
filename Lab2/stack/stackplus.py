from .stack import Stack


class StackPlus(Stack):
    def min(self):
        if self.is_empty():
            return None
        else:
            copy = []
            for i in range(self.size()):
                copy.append(self.top())
                self.pop()
            minval = min(copy)
            copy.reverse()
            for i in copy:
                self.push(i)
            return minval
