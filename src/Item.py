from Event_Result import EventResult
from Important import max_y
from Map_Object import MapObject


class Item(MapObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mark = 'O'
        self.type_name = 'Item'

    def collision_result(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "Munch!")
        return EventResult(True, 0, 1, 1)

    def defeat_result(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "Dont attack items :(")
        return EventResult(True)

    def response(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "It's a nice item! Pick it up")
