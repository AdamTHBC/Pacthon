from Event_Result import EventResult
from Map_Object import MapObject


class Wall(MapObject):
    mark = 'W'
    type_name = 'Wall'
    obstacle = True

    def collision_result(self):
        return EventResult(False, 0, 0, 0)

    def defeat_result(self):
        return EventResult(True, 1, 1, 1)

