import random

from Animation import *
from Important import *
from Map import Map
from unicurses import *


class Engine:
    def __init__(self, stdscr, objects):
        self.map = Map(stdscr, objects)
        self.msgscr = stdscr  # messages
        self.sttscr = stdscr  # status
        self.errscr = stdscr  # errors
        for x in range(amountItem):
            self.spawn('Item')
        for x in range(amountGold):
            self.spawn('Gold')
        for x in range(amountMonster):
            self.spawn('Monster')
        for x in range(amountWall):
            self.spawn('Wall')
        for x in range(amountFood):
            self.spawn('Food')

    def __del__(self):
        endwin()

    ########################### drawing ############################

    def all_refresh(self):
        self.map.stdscr.refresh()
        self.msgscr.refresh()
        self.sttscr.refresh()
        self.errscr.refresh()

    def all_erase(self):
        self.map.stdscr.erase()
        self.msgscr.erase()
        self.sttscr.erase()
        self.errscr.erase()

    def draw(self):
        hero = self.map.objects.lists.get('Hero')
        """draw map"""
        self.map.draw()
        """draw stats"""
        self.sttscr.addstr(1, max_x + 5, "HP " + str(hero.hp))
        self.sttscr.addstr(2, max_x + 5, "XP " + str(hero.experience))
        self.sttscr.addstr(3, max_x + 5, "G " + str(hero.gold))

        self.all_refresh()

    ########################### interactions ############################

    def spawn(self, object_type):
        """Generator of new objects of any available type"""

        "verify if object limit not reached"
        if (self.map.objects.check_limit()):
            self.errscr.addstr(max_y + 5, 0, "Can't create more objects!")
            return

        "roll new coords"
        new_x = random.randint(1, max_x)
        new_y = random.randint(1, max_y)

        "verify if coords are valid (no object there)"
        "repeat spawn if cords were bad"
        if (self.map.objects.check_coords(new_x, new_y)):
            self.spawn(object_type)
            return

        "create object otherwise"
        self.map.objects.create_object(object_type, new_x, new_y)

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
        target = self.map.objects.get_object(tmp_x, tmp_y)

        "check if map border was hit"
        if (tmp_x == 0 or tmp_x > max_x or tmp_y == 0 or tmp_y > max_y):
            self.msgscr.addstr(max_y + 2, 0, "World's end")
            return 0

        "check if obstacle was hit"
        if (target == None):
            actor.x = tmp_x
            actor.y = tmp_y
            return 0

        message = collision_message.get(target.type_name)
        self.msgscr.addstr(max_y + 2, 0, message)

        result = target.collision_result()
        target.hp -= result.damage_to_self
        if (target.obstacle == False):
            actor.x = tmp_x
            actor.y = tmp_y
        if (target.hp <= 0):
            self.map.objects.remove_object(target)
            return result
        return 0

    def ster(self, key):
        """read control input, return 1 if hit a wall"""
        if key == 65:  # UP
            return self.move(self.map.objects.lists.get('Hero'), 3)
        if key == 66:  # DOWN
            return self.move(self.map.objects.lists.get('Hero'), 1)
        if key == 67:  # RIGHT
            return self.move(self.map.objects.lists.get('Hero'), 2)
        if key == 68:  # LEFT
            return self.move(self.map.objects.lists.get('Hero'), 4)
        else:
            "nothing"

    def look_at(self, direction):
        look_x = self.map.objects.lists.get('Hero').x
        look_y = self.map.objects.lists.get('Hero').y
        if direction == 'w':
            look_y -= 1
        if direction == 's':
            look_y += 1
        if direction == 'a':
            look_x -= 1
        if direction == 'd':
            look_x += 1
        target = self.map.objects.get_object(look_x, look_y)
        if (target == None):
            return 0
        message = look_message.get(target.type_name)
        self.msgscr.addstr(max_y + 2, 0, message)

    def attack(self, direction):
        attack_x = self.map.objects.lists.get('Hero').x
        attack_y = self.map.objects.lists.get('Hero').y
        if direction == 'i':
            attack_y -= 1
        if direction == 'k':
            attack_y += 1
        if direction == 'j':
            attack_x -= 1
        if direction == 'l':
            attack_x += 1
        target = self.map.objects.get_object(attack_x, attack_y)

        if (target == None):
            return 0

        damage = self.map.objects.lists.get('Hero').damage
        result = target.attack_result(damage)
        target.hp -= result.damage_to_self

        if (target.hp <= 0):
            message = defeat_message.get(target.type_name)
            self.msgscr.addstr(max_y + 2, 0, message)

            self.map.objects.remove_object(target)
            return result
        else:
            message = attack_message.get(target.type_name)
            battle_log = "You attacked for " + str(damage) + \
                         " and " + str(target.type_name) + " has " + str(target.hp) + " hp remaining."
            self.msgscr.addstr(max_y + 2, 0, message + battle_log)

            return 0

    ########################### control ############################

    def show_help(self):
        self.map.stdscr.addstr(0, 0, """
        arrows - move
        """ + look_keys + """ - look
        """ + attack_keys + """  - attack
        q - quit
        any button - Start
        """)

    def game_start(self):
        show_animation(self.map.stdscr)
        self.show_help()
        """clean unused keys"""
        while (self.map.stdscr.getch() in ignore_keys):
            self.map.stdscr.getch()
        self.all_erase()
        self.draw()

    def action_spawn(self, key):
        if (chr(key) == 'n' and debug == True):
            self.spawn('Item')
            self.spawn('Gold')
            self.spawn('Monster')
            self.spawn('Wall')
            self.spawn('Food')
            self.errscr.addstr(max_y + 5, 0, "Can't create more objects!")
            return

    def action_move(self, key):
        h = self.map.objects.lists.get('Hero')
        if (key in move_keys):
            result = self.ster(key)
            h.steps += 1
            if (result != 0):
                h.hp -= result.damage_to_actor
                h.experience += result.experience
                h.gold += result.gold

    def action_look(self, key):
        if chr(key) in look_keys:
            self.look_at(chr(key))

    def action_attack(self, key):
        h = self.map.objects.lists.get('Hero')
        if chr(key) in attack_keys:
            result = self.attack(chr(key))
            if (result != 0):
                h.hp -= result.damage_to_actor
                h.experience += result.experience
                h.gold += result.gold

    def check_quit(self, key):
        h = self.map.objects.lists.get('Hero')
        objects_left = self.map.objects.count()
        if (chr(key) == 'q' or h.hp <= 0 or objects_left == 0):
            self.all_erase()
            self.map.stdscr.addstr(0, 0, "final score: " + str(5 * h.experience + 4 * h.gold + 10 * h.hp - h.steps)
                                   + "\n\rTHE END")
            return False
        return True

    def action(self, key):
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
