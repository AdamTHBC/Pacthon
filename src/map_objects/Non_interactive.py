from src.map_objects.Map_Object import MapObject


class NonInteractive(MapObject):
    """
    Abstract class for non-interactive objects on the map.
    These could be obstacles (rocks, trees, map borders)
    or just some moving graphics (cloud. animals)
    Have no properties, may take space.
    """
    mark = '*'
    type_name = 'default non-interactive object'

    def __init__(self, x, y):
        super().__init__(x, y)
