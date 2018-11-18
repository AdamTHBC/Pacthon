from src.Event_Result import EventResult
from src.map_objects.Map_Object import MapObject


class Monster(MapObject):
    mark = 'M'
    type_name = 'Monster'
    max_hp = 5

    def collision_result(self):
        return EventResult(0, -1)

    def attack_result(self, damage):
        return EventResult(damage, 0, 3, 1)
