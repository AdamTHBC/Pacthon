from src.Event_Result import EventResult
from src.map_objects.Non_Actor import NonActor


class Sword(NonActor):
    mark = 'S'
    type_name = 'Sword'
    artifact = True

    def __init__(self, x, y):
        super().__init__(x, y)

    def collision_result(self):
        return EventResult(self.hp)

    def attack_result(self, damage):
        return EventResult(damage)

    def artifact_boost(self):
        return ('damage', 1)
