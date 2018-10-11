import random

from Important import max_x,max_y


class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hello(self,stdscr):
        stdscr.addstr(max_y+1,0,"Item " + str(self.x) + " " + str(self.y) + "\n")


class Objects:
    def __init__(self):
        self.l = []

    def spawn(self):
        new_x = random.randint(1, max_x - 1)
        new_y = random.randint(1, max_y - 1)
        for i in self.l:
            if (new_x == i.x and new_y == i.y):
                self.spawn()
                return
        self.l.append(Item(new_x, new_y))

    def hello(self,stdscr):
        for i in self.l:
            i.hello(stdscr)