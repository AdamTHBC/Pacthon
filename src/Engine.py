import random

from unicurses import *

from src.Map import Map
from src.res import *


class Engine:
    def __init__(self, stdscr, objects):
        self.map = Map(stdscr, objects)
        self.msgscr = stdscr  # main messages
        self.sttscr = stdscr  # show status
        self.errscr = stdscr  # show errors
        self.inpscr = stdscr  # get inputs
        self.invscr = stdscr  # inventory overview
        self.itmscr = stdscr  # item description
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
        self.inpscr.refresh()
        self.invscr.refresh()
        self.itmscr.refresh()

    def all_erase(self):
        self.map.stdscr.erase()
        self.msgscr.erase()
        self.sttscr.erase()
        self.errscr.erase()
        self.inpscr.erase()
        self.invscr.erase()
        self.itmscr.erase()

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

    def show_input(self, message):
        self.inpscr.addstr(2, 0, "You've entered: ")
        self.inpscr.addstr(3, 0, message)
        self.inpscr.addstr(4, 0, "Accept? [y/n]")
        key = self.inpscr.getkey()
        if (key == "y"):
            return 1
        if (key == "n"):
            return 0
        return 2

    def prompt_input(self, message):
        self.inpscr.addstr(0, 0, message)
        return self.inpscr.getstr()

    def show_inventory(self, actor):
        """"""
        "TODO - inventory - list of items held by actor"
        self.invscr.erase()
        self.invscr.addstr(0, 0, "| # |    Item name   ")
        self.invscr.addstr(1, 0, "| 1 | Healing Potion ")
        self.invscr.refresh()

        # view item or use item or return?

    def show_item(self, item):
        """
        if inventory open
        if item found
        """
        item.view()

    def show_help(self):
        self.map.stdscr.addstr(0, 0, """
        arrows - move
        """ + look_keys + """ - look
        """ + attack_keys + """  - attack
        [S]ave [L]oad [q]uit
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

        # TODO remake for new Item mechanism
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

        result = target.attack_result(actor.damage * actor.damage_factor)
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
        if (stat == 'hp'):
            lucky_guy.change_hp(value)

    def use_item(self, actor, item):
        if (item.effect_type == None):
            "nothing happened"
        elif (item.effect_type == 'boost'):
            self.stat_increase(actor, (item.area, item.value))
            # remove item
        elif (item.effect_type == 'action'):
            "this I don't know"

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
        if (key == 'n' and debug == True):
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
        if (key in look_keys):
            self.look_at(actor, key)

    def action_attack(self, actor, key):
        """result of attack but only if attack button was pressed"""
        if (key in attack_keys):
            actor.apply_result(self.attack(actor, key))

    def action_saveload(self, actor, key):
        if (key == 'S'):
            prompt = "Save Game menu. Give savefile name."
            savename = self.prompt_input(prompt)
            result = self.show_input(savename)
            self.inpscr.erase()
            if (result == 0):
                "return to map"
            if (result == 1):
                # sprawdz czy taki plik istnieje a jak tak to zapytaj czy nadpisac
                message = "Game saved!"
                self.show_message(actor, message)
            if (result == 2):
                self.action_saveload(actor, key)

        if (key == 'L'):
            prompt = "Load Game menu. Give savefile name."
            savename = self.prompt_input(prompt)
            result = self.show_input(savename)
            self.inpscr.erase()
            if (result == 0):
                "return to map"
            if (result == 1):
                # sprawdz czy taki plik istnieje a jak nie to error
                message = "Game Loaded!"
                self.show_message(actor, message)
            if (result == 2):
                self.action_saveload(actor, key)

    def check_quit(self, key):
        h = self.map.objects.lists.get('Hero')
        objects_left = self.map.objects.count()
        if (key == 'q' or h.hp <= 0 or objects_left == 0):
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
        if (ord(key) in ignore_keys):
            return True
        self.all_erase()
        self.action_spawn(key)
        self.action_move(actor, ord(key))
        self.action_look(actor, key)
        self.action_attack(actor, key)
        self.action_saveload(actor, key)
        self.draw()
        is_over = self.check_quit(key)
        "depending on result - continue, game over OR (TBD) next level"
        return is_over