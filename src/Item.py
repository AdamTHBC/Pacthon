import random

from Hero import Hero
from Important import max_x, max_y


class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hello(self):
        print("Item ", self.x, " ", self.y)


class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hello(self):
        print("Monster ", self.x, " ", self.y)


class Objects:
    def __init__(self):
        self.l = []
        self.lists = {'items': [], 'monsters': [], 'hero': Hero()}
        self.lists.get('hero')

    def spawn(self, object_type):
        "roll new coords"
        new_x = random.randint(0, max_x - 1)
        new_y = random.randint(0, max_y - 1)

        "verify if coords are valid (no object there)"
        bad_coords = False
        if (new_x == self.lists.get('hero').x and new_y == self.lists.get('hero').y):
            bad_coords = True
        for i in self.lists.get('monsters'):
            if (new_x == i.x and new_y == i.y):
                bad_coords = True
        for i in self.lists.get('items'):
            if (new_x == i.x and new_y == i.y):
                bad_coords = True
        "repeat spawn if cords were bad"
        if (bad_coords):
            self.spawn(object_type)
            return
        "create object otherwise"
        if (object_type == 'monster'):
            self.lists.get('monsters').append(Monster(new_x, new_y))
        elif (object_type == 'item'):
            self.lists.get('items').append(Item(new_x, new_y))

    def hello(self):
        for i in self.lists.get('items'):
            i.hello()
        for i in self.lists.get('monsters'):
            i.hello()
        self.lists.get('hero').hello()
