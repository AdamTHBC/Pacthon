import os.path

import yaml

absolute_path = os.path.abspath(os.path.dirname(__file__))
items_path = os.path.join(absolute_path, 'res/Items.yml')

with open(items_path, 'r') as file:
    item_list = yaml.load(file)


class InventoryItem():
    """Item in inventory of an actor
    sometimes can be used or sold.
    Can be viewed by hero, accessed from inventory -> needs a screen.
    Only non-equippable items can be objects of this class, Equipment expands this class

    TODO: parameters read from res/Items.yml, using ItemID
    TODO: graphics, path in res/Items.py
    """

    def __init__(self, ItemID):
        self.name = item_list.get(ItemID).get('name')
        self.graphics = item_list.get(ItemID).get('graphics')
        self.description = item_list.get(ItemID).get('description')
        self.price = item_list.get(ItemID).get('price')
        self.effect_type = item_list.get(ItemID).get('effect_type')
        self.effect = item_list.get(ItemID).get('effect_params')
        self.slot = item_list.get(ItemID).get('slot')

    def give_bonus(self, actor):
        if (self.effect.get('area') == 'gold'):
            actor.change_gold(self.effect.get('value'))
        if (self.effect.get('area') == 'max_hp'):
            actor.change_max_hp(self.effect.get('value'))
        if (self.effect.get('area') == 'hp'):
            actor.change_hp(self.effect.get('value'))
        if (self.effect.get('area') == 'damage'):
            actor.change_damage(self.effect.get('value'))

    def remove_bonus(self, actor):
        if (self.effect.get('area') == 'gold'):
            actor.change_gold(-1 * self.effect.get('value'))
        if (self.effect.get('area') == 'max_hp'):
            actor.change_max_hp(-1 * self.effect.get('value'))
        if (self.effect.get('area') == 'hp'):
            actor.change_hp(-1 * self.effect.get('value'))
        if (self.effect.get('area') == 'damage'):
            actor.change_damage(-1 * self.effect.get('value'))

    def view(self, item_screen):
        item_screen.erase()
        item_screen.addstr(0, 0, self.name)
        item_screen.addstr(1, 0, self.graphics)
        item_screen.addstr(2, 0, self.description)
        item_screen.refresh()
        # view item or use item or return?
        item_screen.getkey()
