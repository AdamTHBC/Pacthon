from Important import max_x, max_y
from Map_Object import MapObject


class Hero(MapObject):
    """Main hero, only one"""
    mark = 'H'
    type_name = 'Hero'
    obstacle = False

    def __init__(self):
        self.steps = 0
        self.x = int(max_x / 2)
        self.y = int(max_y / 2)
        self.gold = 0
        self.experience = 0
        self.hp = 3

    def collision_result(self):
        """not really possible"""

    def defeat_result(self):
        """game over"""
