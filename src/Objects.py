import os.path
import random

import yaml

from src.map_objects import *
from src.res.Important import max_x, max_y


class Objects:
    def __init__(self):
        self.l = []
        self.lists = {'Monster': [], 'Gold': [], 'Wall': [], 'Food': [], 'Map item': []}

        self.singulars = {'StairsUp': StairsUp(1, 1), 'StairsDown': StairsDown(max_x, max_y),
                          'Hero': Hero(int(max_x / 2), int(max_y / 2)),
                          'Heroine': Heroine(int(max_x / 2) + 1, int(max_y / 2))
                          }

        absolute_path = os.path.abspath(os.path.dirname(__file__))
        items_path = os.path.join(absolute_path, 'res/Items.yml')
        with open(items_path, 'r') as file:
            self.item_keys = list(yaml.load(file).keys())

    def check_limit(self):
        object_count = len(self.singulars)
        for i in self.lists.keys():
            object_count = object_count + len(self.lists.get(i))

        object_limit = max_x * max_y

        if (object_count >= object_limit):
            return True
        return False

    def check_coords(self, new_x, new_y):
        """verify if coords of object to be created are not in use"""

        # Verify lists.
        for i in self.lists.keys():
            for j in self.lists.get(i):
                if (new_x == j.x and new_y == j.y):
                    return True

        # Verify singular objects.
        for i in self.singulars.keys():
            j = self.singulars.get(i)
            if (new_x == j.x and new_y == j.y):
                return True

        return False

    def get_object(self, x, y, blacklist=None):
        """
        returns object at given coords or None if empty
        blacklist allows ignoring some objects (type_name)
        """
        for i in self.lists.keys():
            for j in self.lists.get(i):
                if (j.x == x and j.y == y and j.type_name != blacklist):
                    return j
        for i in self.singulars.keys():
            j = self.singulars.get(i)
            if (j.x == x and j.y == y and j.type_name != blacklist):
                return j
        return None

    def create_object(self, object_type, x, y):
        if (object_type == 'Monster'):
            self.lists.get(object_type).append(Monster(x, y))
        elif (object_type == 'Gold'):
            self.lists.get(object_type).append(Gold(x, y))
        elif (object_type == 'Wall'):
            self.lists.get(object_type).append(Wall(x, y))
        elif (object_type == 'Food'):
            self.lists.get(object_type).append(Food(x, y))
        elif (object_type == 'Map item'):
            new_id = self.item_keys[random.randint(0, len(self.item_keys) - 1)]
            self.lists.get(object_type).append(MapItem(new_id, x, y))

    def remove_object(self, removed_object):
        """removes given object"""
        x = removed_object.x
        y = removed_object.y
        for i in self.lists.keys():
            for j in self.lists.get(i):
                if (j.x == x and j.y == y):
                    self.lists.get(i).remove(j)
                    return 0
        for i in self.singulars.keys():
            j = self.singulars.get(i)
            if (j.x == x and j.y == y):
                del self.singulars[i]
                return 0
        return 1

    def count(self):
        result = 0
        for i in self.lists.keys():
            for j in self.lists.get(i):
                result += 1
        return result

    def hello(self, stdscr):
        y = 5
        for i in self.lists.keys():
            for j in self.lists.get(i):
                j.hello(stdscr, y)
                y += 1
        for i in self.singulars.keys():
            self.singulars.get(i).hello(stdscr, y)
            y += 1

    def hello2(self, stdscr):
        y = 5
        for i in range(max_x):
            for j in range(max_y):
                k = self.get_object(i, j)
                if (k is not None):
                    k.hello(stdscr, y)
                    y += 1
                j += 1
            i += 1
