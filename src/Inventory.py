class Inventory():
    """
    class for inventory.
    Used for item management, so has a list of those.
    Must have it's own window to show the contents.

    Every actor has one, enables equipping actor
    """

    def __init__(self):
        #   self.inventory_screen
        self.InventorySize = 8
        self.ItemList = []
        self.EqSlots = {
            'head': None,
            'right': None,
            'left': None,
            'torso': None
        }

    def InventoryAdd(self, item):
        """
        Add item to inventory

        :param item: item to add
        :return: 0 - ok. 1 - not item. 2 - inventory full.
        """
        if (self.ItemList.__len__() >= self.InventorySize):
            "inventory full"
            return 2
        self.ItemList.append(item)
        return 0

    def InventoryRemove(self, item):
        """
        Remove item from inventory.
        Can be used for unequipped items only

        :param item: item to remove
        :return: 0 - ok. 1 - item not found.
        """
        if (item in self.ItemList):
            self.ItemList.remove(item)
            return 0
        "item not found"
        return 1

    def equip(self, item, slot):
        """
        Equip item to slot
        change in bonuses applied by actor in major function

        :param item: item to equip. Success only with Equipment type
        :param slot: slot to wear the item. If not empty, put item to inventory
        :return: 0 - ok. 1 - not equipment. 2 - wrong slot.
        """
        if (item.slot == None):
            "not an equipment"
            return 1
        if (item.slot != slot):
            "wrong slot"
            return 2
        if (self.EqSlots.get(slot) != None):
            "wasn't empty"
            self.InventoryAdd(self.EqSlots.get(slot))
        "ok, equip and remove from list"
        self.EqSlots[slot] = item
        self.InventoryRemove(item)
        return 0

    def view(self, stream):
        j = 15
        for i in self.ItemList:
            stream.addstr(j, 0, i.name)
            j += 1
