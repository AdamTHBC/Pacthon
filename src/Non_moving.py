from Event_Result import EventResult
from Interactive import Interactive


class NonMoving(Interactive):
    """
    Abstract class for living beings on the map.
    These could be items, buildings, structures
    can not(?) attacked, can be looked at.
    May not move.
    """
    type_name = 'default interactive object'

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
