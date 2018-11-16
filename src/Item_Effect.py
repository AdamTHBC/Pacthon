class ItemEffect():
    """ Effect of using an item (or equpiment.
    Not every item has one.
    Effect must contain affected area (e.g. health)
    value, power of the effect
    duration of the effect"""

    def __init__(self, area, value, duration=0):
        self.area = area
        self.value = value
        self.duration = duration
