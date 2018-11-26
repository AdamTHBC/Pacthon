from src.res.Important import ignore_keys


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
        self.position = 0
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

    def show_help(self, stdscr):
        stdscr.addstr(0, 0, """
        UP / DOWN - select
        u - use
        v - view
        q - quit
        """)

    def move(self, direction):
        if (direction == 65):
            self.position -= 1
        elif (direction == 66):
            self.position += 1
        if (self.position < 0):
            self.position = self.InventorySize - 1
        elif (self.position >= self.InventorySize):
            self.position = 0

    def use_item(self, actor):
        if self.position < self.ItemList.__len__():
            """use"""
            self.ItemList[self.position].give_bonus(actor)
            self.ItemList.pop(self.position)

    def view_item(self, stream):
        if self.position < self.ItemList.__len__():
            self.ItemList[self.position].view(stream)
        stream.erase()

    def action(self, key, stream, actor):
        stream.erase()
        if (ord(key) in ignore_keys):
            return True
        if (ord(key) in [65, 66]):
            self.move(ord(key))
        if (key == 'u'):
            self.use_item(actor)
        if (key == 'v'):
            self.view_item(stream)
        self.draw(stream)

        if (key == 'q'):
            return False
        return True

    def view(self, stream, actor):
        self.show_help(stream)
        stream.getkey()
        stream.erase()
        self.draw(stream)
        key = stream.getkey()
        while self.action(key, stream, actor):
            key = stream.getkey()

    def draw(self, stream):
        for i in range(1, self.InventorySize + 1):
            if (i - 1 == self.position):
                stream.addstr(i, 1, '*')
            stream.addstr(i, 3, str(i))

        j = 1
        for i in self.ItemList:
            stream.addstr(j, 6, i.name)
            j += 1

        stream.refresh()
