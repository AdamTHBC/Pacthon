from src.Event_Result import EventResult
from src.map_objects.Interactive import Interactive


class Actor(Interactive):
    """
    Abstract class for active on the map.
    These could be monsters, npcs, companions
    can be attacked, can be looked at.
    May move independently.
    """
    type_name = 'default interactive object'

    def __init__(self, x, y):
        super().__init__(x, y)

    def collision_result(self):
        """What a colliding hero will get"""
        return EventResult()

    def attack_result(self, damage):
        """What a colliding hero will get"""
        return EventResult(damage)