from src.Event_Result import EventResult
from src.map_objects.Non_Actor import NonActor


class Food(NonActor):
    """
    Nice items that heal you if you step on them.
    """
    mark = 'F'
    type_name = 'Food'

    def collision_result(self):
        """
        Restore health of colliding actor and disappear.
        """
        return EventResult(self.hp, 1)
