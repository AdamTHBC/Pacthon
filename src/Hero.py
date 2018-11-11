from Important import max_x, max_y
from Map_Object import MapObject


class Hero(MapObject):
    """Main hero, only one"""
    mark = 'H'
    type_name = 'Hero'
    obstacle = False
    max_hp = 3

    def __init__(self):
        self.steps = 0
        self.x = int(max_x / 2)
        self.y = int(max_y / 2)
        self.gold = 0
        self.experience = 0
        self.hp = self.max_hp
        self.damage = 1

    def collision_result(self):
        """not really possible"""

    def attack_result(self, damage):
        """game over"""
