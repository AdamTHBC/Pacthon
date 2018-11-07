from Event_Result import EventResult
from Map_Object import MapObject


class Item(MapObject):
    mark = 'O'
    type_name = 'Item'

    def collision_result(self):
        return EventResult(True, 0, 1, 1)

    def defeat_result(self):
        return EventResult(True)
