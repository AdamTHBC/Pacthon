from Dictionary_Items import *
from Event_Result import EventResult
from Map_Object import MapObject


class Item(MapObject):
    """ Item that can be picked up.
    sometimes can be used or selled.
    Can be viewed by hero, accessed from inventory.
    Only non-equippable items can be objects of this class

    Class for both ittems that can be picked up and those tyhat are already in the directory. Probably a bad idea"""

    mark = 'I'
    type_name = 'Item'

    def __init__(self, ItemID):
        self.hp = self.max_hp
        self.name = ItemName.get(ItemID)
        self.graphics = ItemGrpahics.get(ItemID)
        self.description = ItemDescription.get(ItemID)
        self.price = ItemPrice.get(ItemID)
        self.effect_type = ItemEffectType.get(ItemID)
        self.effect = ItemEffect.get(ItemID)

    def collision_result(self):
        return EventResult(self.hp, 0, 1, 1)

    def attack_result(self, damage):
        return EventResult(damage)
