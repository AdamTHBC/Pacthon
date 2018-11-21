from src.Inventory_Item import InventoryItem


class Equipment(InventoryItem):
    """Item that can be equipped
    has additional field - slot - dedicated slot it will occupy.
    Has additional effect when equipped
    Other than this, regular item.
    """

    def __init__(self, ItemID):
        super().__init__(ItemID)
        self.name = "Legendary sword"
        self.graphics = "-(==-"
        self.description = "Sword from times long forgotten. Still sharper than anything else."
        self.price = 0
        self.effect_type = None
        self.effect = ("hp", 0, 0)
        self.slot = 'right'
        self.attribute = ("damage", 1)

    def ApplyAttribute(self, actor):
        if (self.attribute[0] == 'damage'):
            actor.change_damage(self.attribute[1])
        if (self.attribute[0] == 'max_hp'):
            actor.change_max_hp(self.attribute[1])
        if (self.attribute[0] == 'hp'):
            actor.change_hp(self.attribute[1])

    def RemoveAttribute(self, actor):
        if (self.attribute[0] == 'damage'):
            actor.change_damage(-1 * self.attribute[1])
        if (self.attribute[0] == 'max_hp'):
            actor.change_max_hp(-1 * self.attribute[1])
        if (self.attribute[0] == 'hp'):
            actor.change_hp(-1 * self.attribute[1])
