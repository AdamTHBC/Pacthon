from Hero import Hero
from Important import *


class Objects:
    def __init__(self):
        self.l = []
        self.lists = {'items': [], 'monsters': [], 'gold': [], 'walls': [], 'food': [], 'hero': Hero()}
        self.lists.get('hero')
        self.list_keys = ['items', 'monsters', 'gold', 'walls', 'food']
        self.non_lists = ['hero']

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
