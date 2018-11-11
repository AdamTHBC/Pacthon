from Event_Result import EventResult
from Important import max_x


class MapObject:
    """Abstract class for objects on the map"""
    mark = '?'
    type_name = 'default object'
    obstacle = False
    max_hp = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = self.max_hp

    def hello(self, stdscr, y):
        """Say hi, help debug"""
        stdscr.addstr(y, max_x + 5, str(self.type_name) + ' ' + str(self.x) + ' ' + str(self.y))

    def collision_result(self):
        """What a colliding hero will get"""
        return EventResult()

    def attack_result(self, damage):
        """What a colliding hero will get"""
        return EventResult(damage)
