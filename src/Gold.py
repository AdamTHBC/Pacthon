from Event_Result import EventResult
from Map_Object import MapObject


class Gold(MapObject):
    mark = 'G'
    type_name = 'Gold'

    def collision_result(self):
        return EventResult(True, 0, 0, 3)

    def defeat_result(self):
        return EventResult(True)

