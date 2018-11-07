from Event_Result import EventResult
from Map_Object import MapObject


class Monster(MapObject):
    mark = 'M'
    type_name = 'Monster'

    def collision_result(self):
        return EventResult(False, 1)

    def defeat_result(self):
        return EventResult(True, 0, 3, 1)

