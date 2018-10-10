from Important import max_x,max_y
from curses import *


class Map:
    def __init__(self):
        "nothing"

    def draw(self, hero, objects, stdscr):
        y = 0
        stdscr.addstr(0,0,"/--------------------\\")
        while (y < max_y):
            x = 0
            stdscr.addch(y+1,x,"|")
            while (x < max_x):
                if (x == hero.x and y == hero.y):
                    stdscr.addch(y,x,"H")
                else:
                    for i in objects:
                        if (x == i.x and y == i.y):
                            stdscr.addch(y,x,"O")
                x +=  1
            stdscr.addch(y+1,x,"|")
            y += 1

        stdscr.addstr(y+1,0,"\\--------------------/")
        stdscr.getch()

    def collision(self, hero, objects):
        for i in objects:
            if (hero.x == i.x and hero.y == i.y):
                #print("munch!")
                objects.remove(i)
                hero.eat()

    def __del__(self):
        endwin()