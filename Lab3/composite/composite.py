from .component import Component
from .leaf import Leaf


class Composite(Component):
    def __init__(self, name, price):
        super().__init__(name, price=price)
        self.__children = []
        self.__children_price = 0

    @property
    def children_price(self):
        return self.__children_price

    def add_component(self, component):
        for c in component.get_children():
            c._depth = c._depth + component._depth
        component._depth = self._depth + component._depth
        self.__children.append(component)

    def remove_component(self, component):
        self.__children.remove(component)

    def do_operation(self):
        self.calc_children_price()
        print('{0}{1} [{2}]'.format('  ' * (self._depth-1), self._name, self.price + self.__children_price))
        for c in self.__children:
            c.do_operation()

    def calc_children_price(self):
        children_price = 0
        for c in self.__children:
            if isinstance(c, Composite):
                c.calc_children_price()
                children_price += c.children_price
            elif isinstance(c, Leaf):
                children_price += c.price
        self.__children_price = children_price

    def get_children(self):
        return self.__children
