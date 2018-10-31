from Event_Result import EventResult
from Important import max_x


class MapObject:
    """Abstract class for objects on the map"""
    mark = '?'
    type_name = 'any object'
    wall = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hello(self, stdscr, y):
        """Say hi, help debug"""
        stdscr.addstr(y, max_x + 5, str(self.type_name) + ' ' + str(self.x) + ' ' + str(self.y))

    def collision_result(self):
        """What a colliding hero will get"""
        return EventResult()

    def defeat_result(self):
        """What a colliding hero will get"""
        return EventResult()

    def response(self):
        """How will it respond to hero's 'talk' action"""
        "will not"
        return ""
