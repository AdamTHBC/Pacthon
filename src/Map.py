import random

from Animation import *
from Food import Food
from Gold import Gold
from Important import *
from Item import Item
from Monster import Monster
from Wall import Wall
from unicurses import *


class Map:
    def __init__(self, stdscr, objects):
        self.objects = objects
        self.stdscr = stdscr  # map
        self.msgscr = stdscr  # messages
        self.sttscr = stdscr  # status
        self.errscr = stdscr  # errors
        for x in range(amountItem):
            self.spawn('item')
        for x in range(amountGold):
            self.spawn('gold')
        for x in range(amountMonster):
            self.spawn('monster')
        for x in range(amountWall):
            self.spawn('wall')
        for x in range(amountFood):
            self.spawn('food')

    def __del__(self):
        endwin()

    ########################### drawing ############################

    def all_refresh(self):
        self.stdscr.refresh()
        self.msgscr.refresh()
        self.sttscr.refresh()
        self.errscr.refresh()

    def all_erase(self):
        self.stdscr.erase()
        self.msgscr.erase()
        self.sttscr.erase()
        self.errscr.erase()

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

    def draw(self):
        hero = self.objects.lists.get('hero')
        y = 1

        self.stdscr.addch(0, 0, "/")
        x = 1
        while (x <= max_x):
            self.stdscr.addch(0, x, "-")
            x += 1
            self.stdscr.addch(0, max_x + 1, "\\")

        while (y <= max_y):
            x = 1
            self.stdscr.addch(y, 0, "|")
            while (x <= max_x):
                char_to_draw = self.draw_spot(x, y)
                self.stdscr.addch(y, x, char_to_draw)
                x += 1

                self.stdscr.addch(y, x, "|")
            y += 1

            self.stdscr.addch(max_y + 1, 0, "\\")
        x = 1
        while (x <= max_x):
            self.stdscr.addch(max_y + 1, x, "-")
            x += 1
            self.stdscr.addch(max_y + 1, max_x + 1, "/")

        self.sttscr.addstr(1, max_x + 5, "HP " + str(hero.hp))
        self.sttscr.addstr(2, max_x + 5, "XP " + str(hero.experience))
        self.sttscr.addstr(3, max_x + 5, "G " + str(hero.gold))

        self.all_refresh()

    ########################### interactions ############################

    def spawn(self, object_type):
        """Generator of new objects of any available type"""

        "verify if object limit not reached"
        if (self.objects.check_limit()):
            self.errscr.addstr(max_y + 5, 0, "Can't create more objects!")
            return

        "roll new coords"
        new_x = random.randint(1, max_x)
        new_y = random.randint(1, max_y)

        "verify if coords are valid (no object there)"
        "repeat spawn if cords were bad"
        if (self.objects.check_coords(new_x, new_y)):
            self.spawn(object_type)
            return

        "create object otherwise"
        if (object_type == 'monster'):
            self.objects.lists.get('monsters').append(Monster(new_x, new_y))
        elif (object_type == 'item'):
            self.objects.lists.get('items').append(Item(new_x, new_y))
        elif (object_type == 'gold'):
            self.objects.lists.get('gold').append(Gold(new_x, new_y))
        elif (object_type == 'wall'):
            self.objects.lists.get('walls').append(Wall(new_x, new_y))
        elif (object_type == 'food'):
            self.objects.lists.get('food').append(Food(new_x, new_y))

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
        target = self.objects.get_object(tmp_x, tmp_y)

        "check if map border was hit"
        if (tmp_x == 0 or tmp_x > max_x or tmp_y == 0 or tmp_y > max_y):
            self.msgscr.addstr(max_y + 2, 0, "World's end")
            return 0

        "check if obstacle was hit"
        if (target == None):
            actor.x = tmp_x
            actor.y = tmp_y
            return 0

        result = target.collision_result()
        if (result.remove == True):
            self.objects.remove_object(target)
        message = collision_message.get(target.type_name)
        self.msgscr.addstr(max_y + 2, 0, message)

        if (target.obstacle == False):
            actor.x = tmp_x
            actor.y = tmp_y
        return result

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

    def look_at(self, direction):
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
        target = self.objects.get_object(look_x, look_y)
        if (target == None):
            return 0
        message = look_message.get(target.type_name)
        self.msgscr.addstr(max_y + 2, 0, message)

    def attack(self, direction):
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
        target = self.objects.get_object(attack_x, attack_y)

        if (target == None):
            return 0

        result = target.defeat_result()
        if (result.remove == True):
            self.objects.remove_object(target)
        message = attack_message.get(target.type_name)
        self.msgscr.addstr(max_y + 2, 0, message)
        return result

    ########################### control ############################

    def show_help(self):
        self.stdscr.addstr(0, 0, """
        arrows - move
        """ + look_keys + """ - look
        """ + attack_keys + """  - attack
        q - quit
        any button - Start
        """)

    def game_start(self):
        show_animation(self.stdscr)
        self.show_help()
        """clean unused keys"""
        while (self.stdscr.getch() in ignore_keys):
            self.stdscr.getch()
        self.all_erase()
        self.draw()

    def action_spawn(self, key):
        if (chr(key) == 'n' and debug == True):
            # TODO change to error screen errscr
            self.objects.spawn(stdscr, 'item')
            self.objects.spawn(stdscr, 'gold')
            self.objects.spawn(stdscr, 'monster')
            self.objects.spawn(stdscr, 'wall')
            self.objects.spawn(stdscr, 'food')

    def action_move(self, key):
        h = self.objects.lists.get('hero')
        if (key in move_keys):
            result = self.ster(key)
            if (result != 0):
                h.hp -= result.damage
                h.experience += result.experience
                h.gold += result.gold

    def action_look(self, key):
        if chr(key) in look_keys:
            self.look_at(chr(key))

    def action_attack(self, key):
        h = self.objects.lists.get('hero')
        if chr(key) in attack_keys:
            result = self.attack(chr(key))
            if (result != 0):
                h.hp -= result.damage
                h.experience += result.experience
                h.gold += result.gold

    def check_quit(self, key):
        h = self.objects.lists.get('hero')
        objects_left = self.objects.count()
        if (chr(key) == 'q' or h.hp <= 0 or objects_left == 0):
            self.stdscr.erase()
            self.stdscr.addstr(0, 1, "final score:" + str(5 * h.experience + 4 * h.gold + 10 * h.hp))
            self.stdscr.addstr(1, 5, "THE END")
            return False
        return True

    def action(self):
        key = self.stdscr.getch()
        if (key in ignore_keys):
            return True
        self.all_erase()
        self.action_spawn(key)
        self.action_move(key)
        self.action_look(key)
        self.action_attack(key)
        self.draw()
        is_over = self.check_quit(key)
        return is_over
