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
        self.map.draw()
        self.show_stats()

        self.all_refresh()

    def show_stats(self):
        hero = self.map.objects.lists.get('Hero')
        self.sttscr.addstr(1, max_x + 5, "LV " + str(hero.level))
        self.sttscr.addstr(2, max_x + 5, "HP " + str(hero.hp))
        self.sttscr.addstr(3, max_x + 5, "XP " + str(hero.experience))
        self.sttscr.addstr(4, max_x + 5, "G " + str(hero.gold))

    def show_message(self, actor, message):
        if (actor.type_name == 'Hero'):
            self.msgscr.addstr(max_y + 2, 0, message)

    def show_error(self, message):
        self.errscr.addstr(max_y + 5, 0, message)

    def show_help(self):
        self.map.stdscr.addstr(0, 0, """
        arrows - move
        """ + look_keys + """ - look
        """ + attack_keys + """  - attack
        q - quit
        any button - Start
        """)

    ########################### interactions ############################

    def spawn(self, object_type):
        """Generator of new objects of any available type"""

        "verify if object limit not reached"
        if (self.map.objects.check_limit()):
            self.show_error("Can't create more objects!")
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

    def move(self, actor, key):
        """move an actor in specified direction, return collision result or 0"""
        tmp_x = actor.x
        tmp_y = actor.y
        if (key == 65):  # UP
            tmp_y -= 1
        if (key == 66):  # DOWN
            tmp_y += 1
        if (key == 67):  # RIGHT
            tmp_x += 1
        if (key == 68):  # LEFT
            tmp_x -= 1
        target = self.map.objects.get_object(tmp_x, tmp_y)

        "case 1: border"
        if (tmp_x == 0 or tmp_x > max_x or tmp_y == 0 or tmp_y > max_y):
            self.show_message(actor, "World's end")
            return 0

        "case 2: empty field"
        if (target == None):
            actor.x = tmp_x
            actor.y = tmp_y
            return 0

        "case 3: collision - interaction"
        result = target.collision_result()
        target.hp -= result.damage_to_self
        if (target.obstacle == False):
            actor.x = tmp_x
            actor.y = tmp_y

        if (target.artifact):
            self.stat_increase(actor, target.artifact_boost())

        if (target.hp <= 0):
            self.map.objects.remove_object(target)

        message = collision_message.get(target.type_name)
        self.show_message(actor, message)

        return result

    def look_at(self, actor, key):
        """check object near hero, get some information"""
        look_x = actor.x
        look_y = actor.y
        if (key == 'w'):  # UP
            look_y -= 1
        if (key == 's'):  # DOWN
            look_y += 1
        if (key == 'a'):  # RIGHT
            look_x -= 1
        if (key == 'd'):  # LEFT
            look_x += 1
        target = self.map.objects.get_object(look_x, look_y)
        if (target == None):
            return 0
        message = look_message.get(target.type_name)
        self.show_message(actor, message)

    def attack(self, actor, key):
        attack_x = actor.x
        attack_y = actor.y
        if (key == 'i'):  # UP
            attack_y -= 1
        if (key == 'k'):  # DOWN
            attack_y += 1
        if (key == 'j'):  # RIGHT
            attack_x -= 1
        if (key == 'l'):  # LEFT
            attack_x += 1
        target = self.map.objects.get_object(attack_x, attack_y)

        if (target == None):
            return 0

        result = target.attack_result(actor.damage)
        target.hp -= result.damage_to_self

        if (target.hp <= 0):
            message = defeat_message.get(target.type_name)
            self.show_message(actor, message)
            self.map.objects.remove_object(target)
            return result
        else:
            message = attack_message.get(target.type_name)
            battle_log = str(actor.type_name) + " attacked for " + str(actor.damage) + \
                         " and " + str(target.type_name) + " has " + str(target.hp) + " hp remaining."
            self.show_message(actor, message + battle_log)

            return 0

    def stat_increase(self, lucky_guy, artifact_boost):
        stat = artifact_boost[0]
        value = artifact_boost[1]
        if (stat == 'damage'):
            lucky_guy.change_damage(value)
        if (stat == 'max_hp'):
            lucky_guy.change_max_hp(value)

    ########################### control ############################

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
            return

    def action_move(self, actor, key):
        """result of moving but only if arrow button was pressed"""
        if (key in move_keys):
            actor.steps += 1
            actor.apply_result(self.move(actor, key))

    def action_look(self, actor, key):
        """result of looking at objects but only if attack button was pressed"""
        if chr(key) in look_keys:
            self.look_at(actor, chr(key))

    def action_attack(self, actor, key):
        """result of attack but only if attack button was pressed"""
        if chr(key) in attack_keys:
            actor.apply_result(self.attack(actor, chr(key)))

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
        """main function in the game
        given input is put to all main actions and results are redrawn,
        afterwards program is ready for another input.
        Actor hard-coded to be hero, it shoulds change in the future."""
        actor = self.map.objects.lists.get('Hero')
        if (key in ignore_keys):
            return True
        self.all_erase()
        self.action_spawn(key)
        self.action_move(actor, key)
        self.action_look(actor, key)
        self.action_attack(actor, key)
        self.draw()
        is_over = self.check_quit(key)
        "depending on result - continue, game over OR (TBD) next level"
        return is_over