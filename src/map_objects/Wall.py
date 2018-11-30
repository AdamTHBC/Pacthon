from src.Event_Result import EventResult
from src.map_objects.Non_Actor import NonActor


class Wall(NonActor):
    """
    Designed to be impassable obstacle, at least as,long as actor can not break it.

    """
    mark = 'W'
    type_name = 'Wall'
    obstacle = True
    max_hp = 5

    def attack_result(self, damage):
        """
        Wall receives normal damage, but hurts attacking actor.

        :param damage: received damage
        :return: deals some damage if destroyed, gives 1 gold and 1 XP
        """
        return EventResult(damage, -1, 1, 1)
