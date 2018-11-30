from src.res.Important import max_x


class MapObject:
    """
    Abstract class for objects on the map
    children classes:
    interactive
    non-interactive
    """
    mark = '?'
    type_name = 'default object'
    max_hp = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = self.max_hp

    def hello(self, stdscr, y):
        """Say hi, help debug"""
        stdscr.addstr(y, max_x + 5, str(self.type_name) + ' ' + str(self.x) + ' ' + str(self.y))
