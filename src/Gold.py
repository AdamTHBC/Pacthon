from Event_Result import EventResult
from Map_Object import MapObject


class Gold(MapObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mark = 'G'
        self.type_name = 'Gold'

    def collision_result(self):
        print("yum!", end='', flush=True)
        return EventResult(True, 0, 0, 3)

    def defeat_result(self):
        print("Dont attack gold :(")
        return EventResult(True)

    def response(self):
        print("It's a shiny gold! Pick it up")
