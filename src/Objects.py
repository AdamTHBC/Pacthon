from Food import Food
from Gold import Gold
from Hero import Hero
from Important import *
from Item import Item
from Monster import Monster
from Stairs import StairsUp, StairsDown
from Sword import Sword
from Wall import Wall


class Objects:
    def __init__(self):
        self.l = []
        self.lists = {'Item': [], 'Monster': [], 'Gold': [], 'Wall': [], 'Food': [],
                      'StairsUp': StairsUp(), 'StairsDown': StairsDown(), 'Sword': Sword(), 'Hero': Hero()}
        self.list_keys = ['Item', 'Monster', 'Gold', 'Wall', 'Food']
        self.non_lists = ['StairsUp', 'StairsDown', 'Sword', 'Hero']

    def check_limit(self):
        object_count = len(self.non_lists)
        for i in self.list_keys:
            object_count = object_count + len(self.lists.get(i))

        object_limit = max_x * max_y

        if (object_count >= object_limit):
            return True
        return False

    def check_coords(self, new_x, new_y):
        """verify if coords of object to be created are not in use"""

        "verify lists"
        for i in self.list_keys:
            for j in self.lists.get(i):
                if (new_x == j.x and new_y == j.y):
                    return True

        "verify singular objects"
        for i in self.non_lists:
            j = self.lists.get(i)
            if (new_x == j.x and new_y == j.y):
                return True

        return False

    def get_object(self, x, y):
        """returns object at given coords or None if empty"""
        for i in self.list_keys:
            for j in self.lists.get(i):
                if (j.x == x and j.y == y):
                    return j
        for i in self.non_lists:
            j = self.lists.get(i)
            if (j.x == x and j.y == y):
                return j
        return None

    def create_object(self, object_type, x, y):
        if (object_type == 'Monster'):
            self.lists.get(object_type).append(Monster(x, y))
        elif (object_type == 'Item'):
            self.lists.get(object_type).append(Item(x, y))
        elif (object_type == 'Gold'):
            self.lists.get(object_type).append(Gold(x, y))
        elif (object_type == 'Wall'):
            self.lists.get(object_type).append(Wall(x, y))
        elif (object_type == 'Food'):
            self.lists.get(object_type).append(Food(x, y))

    def remove_object(self, removed_object):
        """removes given object"""
        x = removed_object.x
        y = removed_object.y
        for i in self.list_keys:
            for j in self.lists.get(i):
                if (j.x == x and j.y == y):
                    self.lists.get(i).remove(j)
                    return 0
        for i in self.non_lists:
            j = self.lists.get(i)
            if (j.x == x and j.y == y):
                self.non_lists.remove(i)
                return 0
        return 1

    def count(self):
        result = 0
        for i in self.list_keys:
            for j in self.lists.get(i):
                result += 1
        return result

    def hello(self, stdscr):
        y = 5
        for i in self.list_keys:
            for j in self.lists.get(i):
                j.hello(stdscr, y)
                y += 1
        for i in self.non_lists:
            self.lists.get(i).hello(stdscr, y)
            y += 1

    def hello2(self, stdscr):
        y = 5
        for i in range(max_x):
            for j in range(max_y):
                k = self.get_object(i, j)
                if (k != None):
                    k.hello(stdscr, y)
                    y += 1
                j += 1
            i += 1
