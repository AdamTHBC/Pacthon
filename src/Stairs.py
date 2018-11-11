from Event_Result import EventResult
from Important import max_x, max_y
from Map_Object import MapObject


class StairsUp(MapObject):
    mark = 'O'
    type_name = 'StairsUp'
    obstacle = True

    def __init__(self):
        self.x = 1
        self.y = 1
        self.hp = self.max_hp

    def collision_result(self):
        return EventResult()

    def attack_result(self, damage):
        return EventResult()


class StairsDown(MapObject):
    mark = 'X'
    type_name = 'StairsDown'
    obstacle = True

    def __init__(self):
        self.x = max_x
        self.y = max_y
        self.hp = self.max_hp

    def collision_result(self):
        return EventResult()

    def attack_result(self, damage):
        return EventResult()
