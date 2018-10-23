from Important import max_x,max_y
from unicurses import *


class Map:
    def __init__(self):
        "nothing"

    def draw(self,stdscr, hero, objects):
        stdscr.erase()
        y = 0
        stdscr.addstr(0,0,"/--------------------\\")
        while (y <= max_y):
            x = 0
            stdscr.addch(y+1,x,"|")
            while (x <= max_x):
                if (x == hero.x and y == hero.y):
                    stdscr.addch(y,x,"H")
                else:
                    for i in objects:
                        if (x == i.x and y == i.y):
                            stdscr.addch(y,x,"O")
                x +=  1
            stdscr.addch(y+1,x,"|")
            y += 1

        stdscr.addstr(y,0,"\\--------------------/")
        stdscr.refresh()

    def collision(self,stdscr, hero, objects):
        for i in objects:
            if (hero.x == i.x and hero.y == i.y):
                stdscr.addstr(max_y+2,0,"Munch")
                objects.remove(i)
                hero.eat()

    def __del__(self):
        endwin()