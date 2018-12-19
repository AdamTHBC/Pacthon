import random

from unicurses import *

from src.Inventory_Item import InventoryItem
from src.Map import Map
from src.map_objects.Map_Item import MapItem
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
            monster = random.choice(enemy_keys)
            self.spawn(monster)
        for x in range(amountWall):
            self.spawn('Wall')
        for x in range(amountFood):
            self.spawn('Food')
        for x in range(amountItem):
            self.spawn('Map item')
        self.current_actor = self.map.objects.lists.get('Hero')[0]


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
        for hero_id in range(0, len(self.map.objects.lists.get('Hero'))):
            hero = self.map.objects.lists.get('Hero')[hero_id]
            if hero.status != 'dead':
                if hero == self.current_actor:
                    self.sttscr.addstr(0, max_x + 5 + 10 * hero_id, "=" + str(hero.name) + "=")
                else:
                    self.sttscr.addstr(0, max_x + 5 + 10 * hero_id, " " + str(hero.name))
                self.sttscr.addstr(1, max_x + 5 + 10 * hero_id, "LV " + str(hero.level))
                self.sttscr.addstr(2, max_x + 5 + 10 * hero_id, "HP " + str(hero.hp))
                self.sttscr.addstr(3, max_x + 5 + 10 * hero_id, "XP " + str(hero.xp))
                self.sttscr.addstr(4, max_x + 5 + 10 * hero_id, "G " + str(hero.gold))
            else:
                self.sttscr.addstr(0, max_x + 5 + 10 * hero_id, " ___")
                self.sttscr.addstr(1, max_x + 5 + 10 * hero_id, "/   \\")
                self.sttscr.addstr(2, max_x + 5 + 10 * hero_id, "|o o|")
                self.sttscr.addstr(3, max_x + 5 + 10 * hero_id, "\\ \" /")
                self.sttscr.addstr(4, max_x + 5 + 10 * hero_id, " |m|")

    def show_level_up(self):
        if self.current_actor.type_name == 'Hero':
            self.all_erase()
            self.map.stdscr.addstr(2, 2, "    _     _")
            self.map.stdscr.addstr(3, 2, "|  |_\\  /|_ |")
            self.map.stdscr.addstr(4, 2, "|_ |_ \\/ |_ |_")
            self.map.stdscr.addstr(5, 6, "     _")
            self.map.stdscr.addstr(6, 6, "| | |_) |")
            self.map.stdscr.addstr(7, 6, ":_: |   o")
            self.map.stdscr.addstr(10, 2, "attack up!")
            self.map.stdscr.addstr(11, 2, "defense up!")
            self.map.stdscr.addstr(12, 2, "max hp up!")
            self.map.stdscr.addstr(15, 2, "Press any key to return")
            self.all_refresh()
            self.map.stdscr.getkey()

    def show_stage_clear(self):
        if self.current_actor.type_name == 'Hero':
            self.all_erase()
            self.msgscr.addstr(2, 2, "Congratulations, you have cleared the stage.")
            self.msgscr.addstr(3, 2, "But your quest is not over.")
            self.msgscr.addstr(15, 2, "Press any key to continue to the next stage.")
            self.all_refresh()
            self.msgscr.getkey()

    def show_message(self, message):
        if self.current_actor.type_name == 'Hero':
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

    def show_help(self):
        self.map.stdscr.addstr(0, 0, """
        1-9 - select actor
        arrows - move
        """ + look_keys + """ - look
        """ + attack_keys + """  - attack
        [S]ave [L]oad [I]nventory
        [q]uit
        any button - Start
        """)

    ########################### interactions ############################

    def spawn(self, object_type):
        """Generator of new objects of any available type"""

        # verify if object limit not reached
        if (self.map.objects.check_limit()):
            self.show_error("Can't create more objects!")
            return

        # roll new coords
        new_x = random.randint(1, max_x)
        new_y = random.randint(1, max_y)

        # verify if coords are valid (no object there)
        # repeat spawn if cords were bad
        if (self.map.objects.check_coords(new_x, new_y)):
            self.spawn(object_type)
            return

        # create object otherwise
        self.map.objects.create_object(object_type, new_x, new_y)

    def pick_up(self):
        """
        pick up an object lying by actor's feet
        :return: 0 - ok. 1 - not item. 2 - inventory full.
        """
        target = self.map.objects.get_object(self.current_actor.x, self.current_actor.y, self.current_actor.type_name)

        if not isinstance(target, MapItem):
            return 1

        # Try adding to inventory
        result = self.current_actor.inventory.inventory_add(InventoryItem(target.ItemID))
        if (result == 0):
            # Item added
            self.map.objects.remove_object(target)

        return result

    ########################### control ############################

    def game_start(self):
        # show_animation(self.map.stdscr)
        self.show_help()
        # Clean unused keys
        while (self.map.stdscr.getch() in ignore_keys):
            self.map.stdscr.getch()
        self.all_erase()
        self.draw()

    def action_spawn(self, key):
        if (key == 'n' and debug):
            self.show_error(self.map.objects.spawn('Gold'))
            self.show_error(self.map.objects.spawn('Monster'))
            self.show_error(self.map.objects.spawn('Orc'))
            self.show_error(self.map.objects.spawn('Troll'))
            self.show_error(self.map.objects.spawn('Wall'))
            self.show_error(self.map.objects.spawn('Food'))
            self.show_error(self.map.objects.spawn('Map item'))
            return

    def action_pick_up(self, key):
        """result of looking at objects but only if attack button was pressed"""
        if (key == ' '):
            self.pick_up()

    def action_look(self, key):
        """result of looking at objects but only if attack button was pressed"""
        if (key in look_keys):
            self.show_message(self.map.objects.look_at(key, self.current_actor))

    def action_attack(self, key):
        """result of attack but only if attack button was pressed"""
        if (key in attack_keys):
            self.show_message(self.map.objects.attack(key, self.current_actor))

    def action_move(self, key):
        """result of moving but only if arrow button was pressed"""
        if (key in move_keys):
            self.show_message(self.map.objects.move(key, self.current_actor))

    def action_inventory(self, key):
        if (key == 'I'):
            self.all_erase()
            dropped_items = self.current_actor.inventory.view(self.invscr, self.current_actor)
            if dropped_items is not None:
                for item in dropped_items:
                    self.map.objects.lists.get('Map item').append(
                        MapItem(item, self.current_actor.x, self.current_actor.y))
            self.draw()

    def action_saveload(self, key):
        """
        TODO, nothing is completed here
        :param key: pressed key
        :return: nothing yer
        """
        if (key == 'S'):
            prompt = "Save Game menu. Give savefile name."
            savename = self.prompt_input(prompt)
            result = self.show_input(savename)
            self.inpscr.erase()
            if (result == 0):
                # Return to map
                "?"
            if (result == 1):
                # Check if exists, ask to confirm overwrite
                message = "Game saved!"
                self.show_message(message)
            if (result == 2):
                self.action_saveload(key)

        if (key == 'L'):
            prompt = "Load Game menu. Give savefile name."
            savename = self.prompt_input(prompt)
            result = self.show_input(savename)
            self.inpscr.erase()
            if (result == 0):
                # Return to map
                "?"
            if (result == 1):
                # Check if file exists, raise error otherwise
                message = "Game Loaded!"
                self.show_message(message)
            if (result == 2):
                self.action_saveload(key)

    def check_quit(self, key):
        score = 0
        for hero_id in range(0, len(self.map.objects.lists.get('Hero'))):
            hero = self.map.objects.lists.get('Hero')[hero_id]
            if hero.hp <= 0:
                self.map.objects.remove_object(hero)
            if hero.status != 'dead':
                score += 5 * hero.xp + 4 * hero.gold + 10 * hero.hp - hero.steps

        if score == 0:
            self.all_erase()
            self.show_stats()
            self.map.stdscr.addstr(0, 0, "Try again!")
            self.map.stdscr.addstr(1, 1, "THE END")
            self.all_refresh()
            return False

        enemies_left = self.map.objects.count_enemies()
        if key == 'q':
            self.all_erase()
            self.show_stats()
            self.map.stdscr.addstr(0, 0, "final score: " + str(score))
            self.map.stdscr.addstr(1, 1, "THE END")
            return False
        # level clear and standing on the stairs
        if enemies_left == 0 and self.current_actor.x == max_x and self.current_actor.y == max_y:
            self.show_stage_clear()
            return False
        return True

    def action(self, key):
        """main function in the game
        given input is put to all main actions and results are redrawn,
        afterwards program is ready for another input.
        """

        if (ord(key) in ignore_keys):
            return True

        # force hero switch if current is dead
        if self.current_actor.status == 'dead':
            for hero_id in range(0, len(self.map.objects.lists.get('Hero'))):
                selected_hero = self.map.objects.lists.get('Hero')[hero_id]
                if selected_hero.status != 'dead':
                    self.current_actor = selected_hero
        if self.current_actor.status == 'dead':
            return False

        # user-requested hero switch (only to living one)
        if key in "123456789" and int(key) in range(0, len(self.map.objects.lists.get('Hero')) + 1):
            selected_hero = self.map.objects.lists.get('Hero')[int(key) - 1]
            if selected_hero.status != 'dead':
                self.current_actor = selected_hero
        bad_tmp = self.current_actor.level

        # check key in every action
        self.all_erase()
        self.action_spawn(key)
        self.action_pick_up(key)
        self.action_look(key)
        self.action_attack(key)
        self.action_move(ord(key))
        self.action_inventory(key)
        self.action_saveload(key)

        # Monster action
        self.map.objects.enemy_action(1)

        if self.current_actor.level > bad_tmp:
            self.show_level_up()
            self.all_erase()

        self.draw()
        self.current_actor.steps += 1

        # Depending on result - continue, game over OR (TODO) next level
        return self.check_quit(key)
