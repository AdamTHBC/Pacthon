from Event_Result import EventResult
from Map_Object import MapObject


class Gold(MapObject):
    mark = 'G'
    type_name = 'Gold'

    def collision_result(self):
        return EventResult(self.hp, 0, 0, 3)

    def attack_result(self, damage):
        return EventResult(damage)
