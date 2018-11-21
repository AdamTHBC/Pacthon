from src.Event_Result import EventResult
from src.map_objects.Map_Object import MapObject


class Food(MapObject):
    mark = 'F'
    type_name = 'Food'

    def collision_result(self):
        return EventResult(self.hp, 1)

    def attack_result(self, damage):
        return EventResult(damage)