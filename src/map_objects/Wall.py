from src.Event_Result import EventResult
from src.map_objects.Non_Actor import NonActor


class Wall(NonActor):
    mark = 'W'
    type_name = 'Wall'
    obstacle = True
    max_hp = 5

    def collision_result(self):
        return EventResult()

    def attack_result(self, damage):
        return EventResult(damage, -1, 1, 1)