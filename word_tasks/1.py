from abc import ABC, abstractmethod


def repack_boxes(*args: 'Box'):
    objects = []
    for el in args:
        objects += el.empty()

    for i in range(len(objects)):
        args[i % len(args)].add(objects[i])


class Box(ABC):
    @abstractmethod
    def add(self, *args):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def count(self):
        pass


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class ListBox(Box):
    def __init__(self):
        self.lis = list()

    def add(self, *args):
        self.lis += args

    def count(self):
        return len(self.lis)

    def empty(self):
        spis = self.lis.copy()
        self.lis.clear()
        return spis


class DictBox(Box):
    def __init__(self):
        self.diction = dict()

    def add(self, *args):
        for i in range(len(args)):
            self.diction[id(args[i])] = args[i]

    def count(self):
        return len(self.diction)

    def empty(self):
        spis = list(self.diction.values())
        self.diction.clear()
        return spis


a = ListBox()
b = ListBox()
c = DictBox()

a.add(Item('a', 1), Item('b', 2))
b.add(Item('c', 3), Item('d', 4), Item('e', 5))
c.add(Item('f', 6))

repack_boxes(a, b, c)
print(a.__dict__, b.__dict__, c.__dict__)
