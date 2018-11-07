from Event_Result import EventResult
from Map_Object import MapObject


class Food(MapObject):
    mark = 'F'
    type_name = 'Food'

    def collision_result(self):
        return EventResult(True, -1, 0, 0)

    def defeat_result(self):
        return EventResult(True)
