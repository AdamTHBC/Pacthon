from Event_Result import EventResult
from Interactive import Interactive


class Being(Interactive):
    """
    Abstract class for living beings on the map.
    These could be monsters, npcs, companions
    can be attacked, can be looked at.
    May move independently.
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
