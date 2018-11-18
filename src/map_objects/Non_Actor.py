from src.Event_Result import EventResult
from src.map_objects.Interactive import Interactive


class NonActor(Interactive):
    """
    Abstract class for passive objects on the map.
    These could be items, buildings, structures
    can not(?) attacked, can be looked at.
    May not move.
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
