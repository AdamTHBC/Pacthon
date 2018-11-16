from Item import Item


class Equipment(Item):
    """Item that can be equipped
    has additional field - EqSlot - dedicated slot it will occupy.
    Has additional effect when equipped
    Other than this, regular item.
    """

    def __init__(self, slot, ):
        ""
