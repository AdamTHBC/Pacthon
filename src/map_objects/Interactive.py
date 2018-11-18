from src.Event_Result import EventResult
from src.map_objects.Map_Object import MapObject


class Interactive(MapObject):
    """
    Abstract class for interactive objects on the map.
    These could be beings (monsters, npcs)
    or not moving (items, buildings)
    can(?) be attacked, can be looked at.
    """
    mark = '?'
    type_name = 'default interactive object'
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
