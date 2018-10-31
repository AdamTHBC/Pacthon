from Event_Result import EventResult
from Important import max_y
from Map_Object import MapObject


class Monster(MapObject):
    mark = 'M'
    type_name = 'Monster'

    def collision_result(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "Ouch")
        return EventResult(False, 1)

    def defeat_result(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "Grr!")
        return EventResult(True, 0, 3, 1)

    def response(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "It's a scary monster! Attack with [i j k l]")
