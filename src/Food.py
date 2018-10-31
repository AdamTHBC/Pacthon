from Event_Result import EventResult
from Important import max_y
from Map_Object import MapObject


class Food(MapObject):
    mark = 'F'
    type_name = 'Food'

    def collision_result(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "Delicious")
        return EventResult(True, -1, 0, 0)

    def defeat_result(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "Worst idea ever")
        return EventResult(True)

    def response(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "Warm and healthy food")
