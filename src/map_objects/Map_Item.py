from src.Event_Result import EventResult
from src.map_objects.Non_Actor import NonActor


class Item(NonActor):
    """ Item that can be picked up.
    sometimes can be used or selled.
    Can be viewed by hero, accessed from inventory.
    Only non-equippable items can be objects of this class
    """

    mark = 'I'
    type_name = 'Item'

    def __init__(self, ItemID, x, y):
        super().__init__(x, y)

    def collision_result(self):
        return EventResult(self.hp, 0, 1, 1)
        # but also spawn item in hero inventory

    def attack_result(self, damage):
        return EventResult(damage)
