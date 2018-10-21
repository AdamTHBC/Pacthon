class EventResult:
    """On defeating an enemy or collision, multiple things may happen. This class returns them."""

    def __init__(self, remove=True, damage=0, experience=0, gold=0):
        self.remove = remove
        self.damage = damage
        self.experience = experience
        self.gold = gold
