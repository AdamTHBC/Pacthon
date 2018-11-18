from src.Item import Item

class Equipment(Item):
    """Item that can be equipped
    has additional field - EqSlot - dedicated slot it will occupy.
    Has additional effect when equipped
    Other than this, regular item.
    """

    def __init__(self, ItemID, slot, x, y):
        super().__init__(ItemID, x, y)
        self.hp = self.max_hp
        self.name = "Legendary sword"
        self.graphics = "-(==-"
        self.description = "Sword from times long forgotten. Still sharper than anything else."
        self.price = 0
        self.effect_type = None
        self.effect = ("hp", 0, 0)
        self.slot = slot
        self.attribute = ("damage", 1)

    def apply_attribute(self, actor):
        if (self.attribute[0] == 'damage'):
            actor.change_damage(self.attribute[1])
        if (self.attribute[0] == 'max_hp'):
            actor.change_max_hp(self.attribute[1])
        if (self.attribute[0] == 'hp'):
            actor.change_hp(self.attribute[1])

    def remove_attribute(self, actor):
        if (self.attribute[0] == 'damage'):
            actor.change_damage(-1 * self.attribute[1])
        if (self.attribute[0] == 'max_hp'):
            actor.change_max_hp(-1 * self.attribute[1])
        if (self.attribute[0] == 'hp'):
            actor.change_hp(-1 * self.attribute[1])
