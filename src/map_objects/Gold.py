from src.Event_Result import EventResult
from src.map_objects.Non_Actor import NonActor


class Gold(NonActor):
    mark = 'G'
    type_name = 'Gold'

    def collision_result(self):
        """
        Give colliding actor some gold and disappear
        """
        return EventResult(self.hp, 0, 0, 3)
