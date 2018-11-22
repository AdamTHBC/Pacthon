from src.Event_Result import EventResult
from src.map_objects.Non_Actor import NonActor


class MapItem(NonActor):
    """ Item that can be picked up.
    sometimes can be used or selled.
    Can be viewed by hero, accessed from inventory.
    Only non-equippable items can be objects of this class
    """

    mark = 'I'
    type_name = 'Map item'

    def __init__(self, ItemID, x, y):
        super().__init__(x, y)
        self.ItemID = ItemID

    def collision_result(self):
        return EventResult(0)
        # but also spawn item in hero inventory

    def attack_result(self, damage):
        return EventResult(damage)
