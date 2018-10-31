from Event_Result import EventResult
from Important import max_y
from Map_Object import MapObject


class Wall(MapObject):
    mark = 'W'
    type_name = 'Wall'
    obstacle = True

    def collision_result(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "Bump")
        return EventResult(True, 0, 1, 1)

    def defeat_result(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "It hurt!")
        return EventResult(True, 1, 1, 1)

    def response(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "It's a wall! Maybe it can break..?")
