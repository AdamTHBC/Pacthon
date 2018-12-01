from src.Event_Result import EventResult
from src.Inventory import Inventory
from src.map_objects.Interactive import Interactive
from src.res.Important import lvl_chart


class Actor(Interactive):
    """
    Abstract class for active object on the map.
    These could be monsters, heroes, companions
    can be damaged, can be looked at.
    May move independently.
    """
    type_name = 'default actor object'

    def __init__(self, x, y):
        super().__init__(x, y)
        self.level = 1
        self.gold = 0
        self.xp = 0
        self.xp_factor = 1
        self.damage = 1
        self.damage_factor = 1
        self.inventory = Inventory()

    def attack_result(self, damage):
        """
        if attacked, will receive damage

        :param damage: amount of damaged received by attacked actor
        :return: Event result - nothing happens, aside from this actor getting damaged
        """
        return EventResult(damage)

    def apply_result(self, result):
        if result != 0:
            self.change_hp(result.damage_to_actor)
            self.change_xp(result.xp)
            self.change_gold(result.gold)

    def change_gold(self, value):
        """modify hero's gold using value"""
        self.gold += value

    def change_max_hp(self, value):
        """modify hero's max_hp using value"""
        self.max_hp += value
        self.hp += value

    def change_hp(self, value):
        """modify hero's health using value. Returns False if dead, but it's not used currently"""
        self.hp += value
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        if self.hp <= 0:
            return False
        return True

    def change_damage(self, value):
        """modify hero's damage using value"""
        self.damage += value

    def change_xp(self, value):
        """modify hero's xp using value. check for level up"""
        self.xp += value * self.xp_factor
        while self.level_up():
            """increase level required number of times"""

    def level_up(self):
        """check level up. Return True if level up happened to trigger another check"""
        if self.xp >= lvl_chart[self.level]:
            self.level += 1
            self.change_max_hp(3)
            self.change_damage(1)
            return True
        return False
