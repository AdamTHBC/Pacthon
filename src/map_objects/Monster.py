from src.Event_Result import EventResult
from src.map_objects.Actor import Actor


class Monster(Actor):
    mark = 'M'
    type_name = 'Monster'
    max_hp = 5

    def collision_result(self):
        """
        Nothing happens to monster. Colliding actor gets hit.

        :return:
        """
        return EventResult(0, -1)

    def attack_result(self, damage):
        """
        damages monster some, and gives some gold and XP upon defeat.

        :param damage: amount of damage dealt
        :return:
        """
        return EventResult(damage, 0, 3, 1)
