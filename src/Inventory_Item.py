class InventoryItem():
    """Item in inventory of an actor
    sometimes can be used or sold.
    Can be viewed by hero, accessed from inventory -> needs a screen.
    Only non-equippable items can be objects of this class, Equipment expands this class

    TODO: parameters read from res/Items.yml, using ItemID
    TODO: graphics, path in res/Items.py
    """

    def __init__(self, ItemID):
        self.name = "Healing Potion"
        self.graphics = "( H )"
        self.description = "A red, glowing healing potion. Drinking it restores 2 HP."
        self.price = 2
        self.effect_type = "boost"
        self.effect = ("hp", 2, 0)

    def give_bonus(self, actor):
        if (self.effect_type == "boost"):
            if (self.effect[0] == "gold"):
                actor.change_gold(self.effect[1])
            if (self.effect[0] == "max_hp"):
                actor.change_max_hp(self.effect[1])
            if (self.effect[0] == "hp"):
                actor.change_hp(self.effect[1])
            if (self.effect[0] == "damage"):
                actor.change_damage(self.effect[1])

    def view(self, item_screen):
        item_screen.erase()
        item_screen.addstr(0, 0, self.name)
        item_screen.addstr(1, 0, self.graphics)
        item_screen.addstr(2, 0, self.description)
        item_screen.refresh()
        # view item or use item or return?
        item_screen.getkey()
