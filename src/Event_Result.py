class EventResult:
    """On defeating an enemy or collision, multiple things may happen. This class returns them."""

    def __init__(self, damage_to_self=0, damage_to_actor=0, xp=0, gold=0):
        self.damage_to_self = damage_to_self
        self.damage_to_actor = damage_to_actor
        self.xp = xp
        self.gold = gold
