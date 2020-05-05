from .component import Component


class Leaf(Component):
    def __init__(self, name, price):
        super().__init__(name, price=price)

    def do_operation(self):
        print('{0}{1} [{2}]'.format('  ' * (self._depth-1), self._name, self.price))
