from src.Event_Result import EventResult
from src.map_objects.Map_Object import MapObject


class Item(MapObject):
    """ Item that can be picked up.
    sometimes can be used or selled.
    Can be viewed by hero, accessed from inventory.
    Only non-equippable items can be objects of this class

    Class for both items that can be picked up and those that are already in the directory. Probably a bad idea
    TODO: parameters read from res/Items.yml, using ItemID
    TODO: graphics, path in res/Items.py
    """

    mark = 'I'
    type_name = 'Item'

    def __init__(self, ItemID, x, y):
        super().__init__(x, y)
        self.name = "Healing Potion"
        self.graphics = "( H )"
        self.description = "A red, glowing healing potion. Drinking it restores 2 HP."
        self.price = 2
        self.effect_type = "boost"
        self.effect = ("hp", 2, 0)

    def collision_result(self):
        return EventResult(self.hp, 0, 1, 1)

    def attack_result(self, damage):
        return EventResult(damage)

    def view(self, item_screen):
        item_screen.erase()
        item_screen.addstr(0, 0, self.name)
        item_screen.addstr(1, 0, self.graphics)
        item_screen.addstr(2, 0, self.description)
        item_screen.refresh()
        # view item or use item or return?
        item_screen.getkey()
