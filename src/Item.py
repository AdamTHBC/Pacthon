from Event_Result import EventResult
from Map_Object import MapObject


class Item(MapObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mark = 'O'
        self.type_name = 'Item'

    def collision_result(self):
        print("munch!", end='', flush=True)
        return EventResult(True, 0, 1, 1)

    def defeat_result(self):
        print("Dont attack items :(")
        return EventResult(True)

    def response(self):
        print("It's a nice item! Pick it up")
