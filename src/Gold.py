from Event_Result import EventResult
from Important import max_y
from Map_Object import MapObject


class Gold(MapObject):
    mark = 'G'
    type_name = 'Gold'


    def collision_result(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "yum!")
        return EventResult(True, 0, 0, 3)

    def defeat_result(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "Dont attack gold :(")
        return EventResult(True)

    def response(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "It's a shiny gold! Pick it up")
