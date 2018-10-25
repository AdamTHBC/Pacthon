import random

from Gold import Gold
from Hero import Hero
from Important import max_x, max_y
from Item import Item
from Monster import Monster


class Objects:
    def __init__(self):
        self.l = []
        self.lists = {'items': [], 'monsters': [], 'gold': [], 'hero': Hero()}
        self.lists.get('hero')
        self.list_keys = ['items', 'monsters', 'gold']
        self.non_lists = ['hero']

    def check_limit(self):
        object_count = len(self.non_lists)
        for i in self.list_keys:
            object_count = object_count + len(self.lists.get(i))

        object_limit = max_x * max_y

        if (object_count >= object_limit):
            print("Can't create more objects!")
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

    def spawn(self, object_type):
        """Generator of new objects of any available type"""

        "verify if object limit not reached"
        if (self.check_limit()):
            return

        "roll new coords"
        new_x = random.randint(1, max_x)
        new_y = random.randint(1, max_y)

        "verify if coords are valid (no object there)"
        "repeat spawn if cords were bad"
        if (self.check_coords(new_x, new_y)):
            self.spawn(object_type)
            return

        "create object otherwise"
        if (object_type == 'monster'):
            self.lists.get('monsters').append(Monster(new_x, new_y))
        elif (object_type == 'item'):
            self.lists.get('items').append(Item(new_x, new_y))
        elif (object_type == 'gold'):
            self.lists.get('gold').append(Gold(new_x, new_y))

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
