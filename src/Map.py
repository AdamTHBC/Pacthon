from Important import max_x, max_y
from unicurses import *


class Map:
    def __init__(self, objects):
        self.objects = objects

    def draw_spot(self, x, y):
        """Decide what should be drawn on a given spot"""

        "verify singular objects"
        for i in self.objects.non_lists:
            j = self.objects.lists.get(i)
            if (x == j.x and y == j.y):
                return j.mark

        "verify lists"
        for i in self.objects.list_keys:
            for j in self.objects.lists.get(i):
                if (x == j.x and y == j.y):
                    return j.mark

        return ' '

    def draw(self, stdscr):
        hero = self.objects.lists.get('hero')
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
                char_to_draw = self.draw_spot(x, y)
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

    def move(self, actor, direction):
        """move an actor in specified direction, or return 1 if hit a wall"""
        tmp_x = actor.x
        tmp_y = actor.y

        if (direction == 1):
            tmp_y += 1
        if (direction == 2):
            tmp_x += 1
        if (direction == 3):
            tmp_y -= 1
        if (direction == 4):
            tmp_x -= 1

        "check if map border was hit"
        if (tmp_x == 0 or tmp_x > max_x or tmp_y == 0 or tmp_y > max_y):
            "Hit a wall"
            return 1

        "check if obstacle was hit"
        o = self.objects.get_object(tmp_x, tmp_y)
        if (o != None and o.obstacle):
            return 1

        "free space"
        actor.x = tmp_x
        actor.y = tmp_y
        return 0

    def ster(self, key):
        """read control input, return 1 if hit a wall"""
        if key == 65:  # UP
            return self.move(self.objects.lists.get('hero'), 3)
        if key == 66:  # DOWN
            return self.move(self.objects.lists.get('hero'), 1)
        if key == 67:  # RIGHT
            return self.move(self.objects.lists.get('hero'), 2)
        if key == 68:  # LEFT
            return self.move(self.objects.lists.get('hero'), 4)
        else:
            "nothing"

    def look_at(self, stdscr, direction):
        look_x = self.objects.lists.get('hero').x
        look_y = self.objects.lists.get('hero').y

        if direction == 'w':
            look_y -= 1
        if direction == 's':
            look_y += 1
        if direction == 'a':
            look_x -= 1
        if direction == 'd':
            look_x += 1
        for i in self.objects.list_keys:
            for j in self.objects.lists.get(i):
                if (look_x == j.x and look_y == j.y):
                    j.response(stdscr)

    def attack(self, stdscr, direction):
        attack_x = self.objects.lists.get('hero').x
        attack_y = self.objects.lists.get('hero').y

        if direction == 'i':
            attack_y -= 1
        if direction == 'k':
            attack_y += 1
        if direction == 'j':
            attack_x -= 1
        if direction == 'l':
            attack_x += 1
        for i in self.objects.list_keys:
            for j in self.objects.lists.get(i):
                if (attack_x == j.x and attack_y == j.y):
                    result = j.defeat_result(stdscr)
                    if (result.remove == True):
                        self.objects.lists.get(i).remove(j)
                    return result
        return 0

    def collision(self, stdscr):
        for i in self.objects.list_keys:
            for j in self.objects.lists.get(i):
                if (self.objects.lists.get('hero').x == j.x and self.objects.lists.get('hero').y == j.y):
                    result = j.collision_result(stdscr)
                    if (result.remove == True):
                        self.objects.lists.get(i).remove(j)
                    return result
        return 0

    def __del__(self):
        endwin()
