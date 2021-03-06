import os.path
import random

import yaml

from src.map_objects import *
from src.res.Dictionary_Text import *
from src.res.Important import max_x, max_y, enemy_keys, attack_keys, move_keys


class Objects:
    def __init__(self):
        self.lists = {'Monster': [], 'Orc': [], 'Troll': [],
                      'Gold': [], 'Wall': [], 'Food': [], 'Map item': [],
                      'StairsUp': [], 'StairsDown': [],
                      'Hero': []
                      }
        # Define create and add mandatory objects.
        self.lists.get('StairsUp').append(StairsUp(1, 1))
        self.lists.get('StairsDown').append(StairsDown(max_x, max_y))
        self.lists.get('Hero').append(Hero(int(max_x / 2), int(max_y / 2), 'Ja', '1'))
        self.lists.get('Hero').append(Hero(int(max_x / 2) + 1, int(max_y / 2), 'Ty', '2'))
        self.lists.get('Hero').append(Hero(int(max_x / 2), int(max_y / 2) + 1, 'On', '3'))

        absolute_path = os.path.abspath(os.path.dirname(__file__))
        items_path = os.path.join(absolute_path, 'res/Items.yml')
        with open(items_path, 'r') as file:
            self.item_keys = list(yaml.load(file).keys())

    ######################## object control #########################

    def check_limit(self):
        object_count = 0
        for i in self.lists.keys():
            object_count = object_count + len(self.lists.get(i))

        object_limit = max_x * max_y

        if (object_count >= object_limit):
            return True
        return False

    def check_coords(self, new_x, new_y):
        """verify if coords of object to be created are not in use"""

        for i in self.lists.keys():
            for j in self.lists.get(i):
                if (new_x == j.x and new_y == j.y):
                    return True

        return False

    def get_object(self, x, y, blacklist=None):
        """
        returns object at given coords or None if empty
        blacklist allows ignoring some objects (type_name)
        """
        for i in self.lists.keys():
            for j in self.lists.get(i):
                if (j.x == x and j.y == y and j.type_name != blacklist):
                    return j
        return None

    def create_object(self, object_type, x, y):
        """
        Objects that are created multiple times at random.
        If object_type does not match any of expected types, no object is created
        More strictly defined objects are mostly generated by direct sppending

        :param object_type: type of added object
        :param x: horizontal map coordinate
        :param y: vertical map coordinate
        :return: returns nothing
        """
        if (object_type == 'Monster'):
            self.lists.get(object_type).append(Monster(x, y))
        if (object_type == 'Orc'):
            self.lists.get(object_type).append(Orc(x, y))
        if (object_type == 'Troll'):
            self.lists.get(object_type).append(Troll(x, y))
        elif (object_type == 'Gold'):
            self.lists.get(object_type).append(Gold(x, y))
        elif (object_type == 'Wall'):
            self.lists.get(object_type).append(Wall(x, y))
        elif (object_type == 'Food'):
            self.lists.get(object_type).append(Food(x, y))
        elif object_type == 'Map item':
            new_id = self.item_keys[random.randint(0, len(self.item_keys) - 1)]
            self.lists.get(object_type).append(MapItem(new_id, x, y))

    def remove_object(self, removed_object):
        """removes given object"""
        x = removed_object.x
        y = removed_object.y
        for i in self.lists.keys():
            for j in self.lists.get(i):
                if (j.x == x and j.y == y):
                    if j.type_name == 'Hero':
                        j.status = 'dead'
                        j.mark = '+'
                        return 0
                    self.lists.get(i).remove(j)
                    return 0
        return 1

    def spawn(self, object_type):
        """Generator of new objects of any available type"""

        # verify if object limit not reached
        if (self.check_limit()):
            return "Can't create more objects!"

        # roll new coords
        new_x = random.randint(1, max_x)
        new_y = random.randint(1, max_y)

        # verify if coords are valid (no object there)
        # repeat spawn if cords were bad
        if (self.check_coords(new_x, new_y)):
            self.spawn(object_type)
            return ""

        # create object otherwise
        self.create_object(object_type, new_x, new_y)
        return ""

    def count(self):
        result = 0
        for i in self.lists.keys():
            for j in self.lists.get(i):
                result += 1
        return result

    def count_enemies(self):
        result = 0
        for i in enemy_keys:
            for j in self.lists.get(i):
                result += 1
        return result

    def hello(self, stdscr):
        y = 5
        for i in self.lists.keys():
            for j in self.lists.get(i):
                j.hello(stdscr, y)
                y += 1

    def hello2(self, stdscr):
        y = 5
        for i in range(max_x):
            for j in range(max_y):
                k = self.get_object(i, j)
                if (k is not None):
                    k.hello(stdscr, y)
                    y += 1
                j += 1
            i += 1

    ######################### iteractions ##########################

    def attack(self, key, actor):
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
        target = self.get_object(attack_x, attack_y)

        if (target is None):
            return ""

        result = target.attack_result(actor.damage * actor.damage_factor)
        target.hp -= result.damage_to_self

        if (target.hp <= 0):
            actor.apply_result(result)
            message = defeat_message.get(target.type_name)
            self.remove_object(target)
        else:
            message = attack_message.get(target.type_name)
            message += str(actor.type_name) + " attacked for " + str(actor.damage) + \
                       " and " + str(target.type_name) + " has " + str(target.hp) + " hp remaining."
        return message

    def move(self, key, actor):
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
        target = self.get_object(tmp_x, tmp_y)

        # case 1: border
        if (tmp_x == 0 or tmp_x > max_x or tmp_y == 0 or tmp_y > max_y):
            return "World's end"

        # case 2: empty field
        if (target is None):
            actor.x = tmp_x
            actor.y = tmp_y
            return ""

        # case 3: collision - interaction
        result = target.collision_result()
        target.hp -= result.damage_to_self
        if (not target.obstacle):
            actor.x = tmp_x
            actor.y = tmp_y
        actor.apply_result(result)

        if (target.hp <= 0):
            self.remove_object(target)

        return collision_message.get(target.type_name)

    def look_at(self, key, actor):
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
        target = self.get_object(look_x, look_y)
        if (target is None):
            return ""
        return look_message.get(target.type_name)

    def enemy_action(self, difficulty=1):
        # select enemies
        # get number of enemies
        enemy_count = self.count_enemies()
        number_of_moving_enemies = min(enemy_count, difficulty)
        if number_of_moving_enemies == 0:
            return

        # select different enemies
        all_enemies = []
        for i in enemy_keys:
            for j in self.lists.get(i):
                all_enemies.append(j)
        moving_enemies = random.sample(all_enemies, number_of_moving_enemies)
        for i in moving_enemies:
            move_dir = random.choice(move_keys)
            self.move(move_dir, i)
            attack_dir = random.choice(attack_keys)
            self.attack(attack_dir, i)
        return
