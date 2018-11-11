from Event_Result import EventResult
from Map_Object import MapObject


class Item(MapObject):
    mark = 'I'
    type_name = 'Item'

    def collision_result(self):
        return EventResult(self.hp, 0, 1, 1)

    def attack_result(self, damage):
        return EventResult(damage)
