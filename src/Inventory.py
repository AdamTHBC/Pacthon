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

    def equip(self, item, actor):
        """
        Equip item to slot
        change in bonuses applied by actor in major function

        :param item: item to equip. Success only with Equipment type
        :param actor: actpr equipping. Will be solved better
        :return: 0 - ok. 1 - not equipment.
        """
        if (item.slot not in self.EqSlots.keys()):
            "not an equipment"
            return 1

        old_item = self.EqSlots.get(item.slot)

        "ok, equip and remove from list"
        self.EqSlots[item.slot] = item
        self.InventoryRemove(item)
        item.give_bonus(actor)

        if (old_item != None):
            "wasn't empty"
            # remove (any) old equipment bonus
            old_item.remove_bonus(actor)
            self.InventoryAdd(old_item)
        return 0

    def show_help(self, stdscr):
        stdscr.addstr(0, 0, """
        UP / DOWN - select
        u - use
        v - view
        d - destroy
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
        if (self.ItemList[self.position].effect_type == "boost"):
            self.ItemList[self.position].give_bonus(actor)
            self.ItemList.pop(self.position)

    def destroy(self):
        self.ItemList.remove(self.ItemList[self.position])

    def view_item(self, stream):
        self.ItemList[self.position].view(stream)
        stream.erase()

    def action(self, key, stream, actor):
        stream.erase()
        if (ord(key) in ignore_keys):
            return True
        if (ord(key) in [65, 66]):
            self.move(ord(key))
        if (self.position < self.ItemList.__len__() and key == 'u'):
            self.use_item(actor)
        if (self.position < self.ItemList.__len__() and key == 'v'):
            self.view_item(stream)
        if (self.position < self.ItemList.__len__() and key == 'e'):
            self.equip(self.ItemList[self.position], actor)
        if (self.position < self.ItemList.__len__() and key == 'd'):
            self.destroy()
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
        stream.erase()

    def draw(self, stream):
        for i in range(1, self.InventorySize + 1):
            if (i - 1 == self.position):
                stream.addstr(i, 1, '*')
            stream.addstr(i, 3, str(i))

        j = 1
        for i in self.ItemList:
            stream.addstr(j, 6, i.name)
            j += 1
        for dict_key in self.EqSlots.keys():
            self.draw_slot(stream, dict_key)

        stream.refresh()

    def draw_slot(self, stream, slot):
        """

        :param stream:
        :param slot:
        :return:
        """
        # get parameters for given slot
        if (slot == "head"):
            row = 0
            column = 1
        elif (slot == "right"):
            row = 1
            column = 0
        elif (slot == "left"):
            row = 1
            column = 2
        elif (slot == "torso"):
            row = 2
            column = 1
        else:
            row = 0
            column = 0

        x = 8 * column + 30
        y = 5 * row + 1
        stream.addstr(y, x + 1, slot)
        stream.addstr(y + 1, x, " _____ ")
        stream.addstr(y + 2, x, "|     |")
        stream.addstr(y + 3, x, "|     |")
        stream.addstr(y + 4, x, "|_____|")
        if (self.EqSlots.get(slot) != None):
            stream.addstr(y + 3, x + 1, self.EqSlots.get(slot).graphics)
