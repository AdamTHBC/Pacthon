from Event_Result import EventResult
from Important import max_x
from Map_Object import MapObject


class Sword(MapObject):
    mark = 'S'
    type_name = 'Sword'
    artifact = True

    def __init__(self):
        self.x = max_x
        self.y = 1
        self.hp = self.max_hp

    def collision_result(self):
        return EventResult(self.hp)

    def attack_result(self, damage):
        return EventResult(damage)

    def artifact_boost(self):
        return ('damage', 1)
