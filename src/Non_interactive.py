from Event_Result import EventResult
from Map_Object import MapObject


class NonInteractive(MapObject):
    """
    Abstract class for non-interactive objects on the map.
    These could be obstacles (rocks, trees, map borders)
    or just some moving graphics (cloud. animals)
    Have no properties, may take space.
    """
    mark = '?'
    type_name = 'default non-interactive object'
    obstacle = False
    artifact = False
    max_hp = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = self.max_hp

    def collision_result(self):
        """What a colliding hero will get"""
        return EventResult()

    def attack_result(self, damage):
        """What a colliding hero will get"""
        return EventResult(damage)
