from src.Event_Result import EventResult
from src.map_objects.Map_Object import MapObject


class Interactive(MapObject):
    """
    Abstract class for interactive objects on the map.
    These could be beings (monsters, npcs)
    or not moving (items, buildings)
    can be attacked, can be looked at.
    """
    mark = '~'
    type_name = 'default interactive object'
    obstacle = False

    def collision_result(self):
        """
        Default collision without any effect
        :return:
        """
        return EventResult()
