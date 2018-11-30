from src.Event_Result import EventResult
from src.map_objects.Interactive import Interactive


class NonActor(Interactive):
    """
    Abstract class for passive objects on the map.
    These could be items, buildings, structures
    can not be damaged, can be looked at.
    May not move.
    """
    type_name = 'default non-actor object'

    def attack_result(self, damage):
        """
        if attacked, will NOT receive damage

        :param damage: for compatibility
        :return: Event result - nothing happens
        """
        return EventResult()
