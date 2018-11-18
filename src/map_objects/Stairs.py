from src.Event_Result import EventResult
from src.map_objects.Map_Object import MapObject


class StairsUp(MapObject):
    mark = 'O'
    type_name = 'StairsUp'
    obstacle = True

    def __init__(self, x, y):
        super().__init__(x, y)

    def collision_result(self):
        return EventResult()

    def attack_result(self, damage):
        return EventResult()


class StairsDown(MapObject):
    mark = 'X'
    type_name = 'StairsDown'
    obstacle = True

    def __init__(self, x, y):
        super().__init__(x, y)

    def collision_result(self):
        return EventResult()

    def attack_result(self, damage):
        return EventResult()
