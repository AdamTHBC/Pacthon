from Important import max_x, max_y
from unicurses import *


class Map:
    def __init__(self):
        "nothing"

    def draw_spot(self, x, y, objects):
        """Decide what should be drawn on a given spot"""

        "verify singular objects"
        for i in objects.non_lists:
            j = objects.lists.get(i)
            if (x == j.x and y == j.y):
                return j.mark

        "verify lists"
        for i in objects.list_keys:
            for j in objects.lists.get(i):
                if (x == j.x and y == j.y):
                    return j.mark

        return ' '

    def draw(self, stdscr, objects):
        hero = objects.lists.get('hero')
        y = 1

        stdscr.addch(0, 0, "/")
        x = 1
        while (x <= max_x):
            stdscr.addch(0, x, "-")
            x += 1
        stdscr.addch(0, max_x + 1, "\\")

        while (y <= max_y):
            x = 1
            stdscr.addch(y, 0, "|")
            while (x <= max_x):
                char_to_draw = self.draw_spot(x, y, objects)
                stdscr.addch(y, x, char_to_draw)
                x += 1

            stdscr.addch(y, x, "|")
            y += 1

        stdscr.addch(max_y + 1, 0, "\\")
        x = 1
        while (x <= max_x):
            stdscr.addch(max_y + 1, x, "-")
            x += 1
        stdscr.addch(max_y + 1, max_x + 1, "/")

        stdscr.addstr(1, max_x + 5, "HP " + str(hero.hp))
        stdscr.addstr(2, max_x + 5, "XP " + str(hero.experience))
        stdscr.addstr(3, max_x + 5, "G " + str(hero.gold))

        stdscr.refresh()

    def look_at(self, stdscr, objects, direction):
        look_x = objects.lists.get('hero').x
        look_y = objects.lists.get('hero').y

        if direction == 'w':
            look_y -= 1
        if direction == 's':
            look_y += 1
        if direction == 'a':
            look_x -= 1
        if direction == 'd':
            look_x += 1
        for i in objects.list_keys:
            for j in objects.lists.get(i):
                if (look_x == j.x and look_y == j.y):
                    j.response(stdscr)

    def attack(self, stdscr, objects, direction):
        attack_x = objects.lists.get('hero').x
        attack_y = objects.lists.get('hero').y

        if direction == 'i':
            attack_y -= 1
        if direction == 'k':
            attack_y += 1
        if direction == 'j':
            attack_x -= 1
        if direction == 'l':
            attack_x += 1
        for i in objects.list_keys:
            for j in objects.lists.get(i):
                if (attack_x == j.x and attack_y == j.y):
                    result = j.defeat_result(stdscr)
                    if (result.remove == True):
                        objects.lists.get(i).remove(j)
                    return result
        return 0

    def collision(self, stdscr, objects):
        for i in objects.list_keys:
            for j in objects.lists.get(i):
                if (objects.lists.get('hero').x == j.x and objects.lists.get('hero').y == j.y):
                    result = j.collision_result(stdscr)
                    if (result.remove == True):
                        objects.lists.get(i).remove(j)
                    return result
        return 0

    def __del__(self):
        endwin()
