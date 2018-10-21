from Event_Result import EventResult
from Map_Object import MapObject


class Monster(MapObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mark = 'M'
        self.type_name = 'Monster'

    def collision_result(self):
        print("Ouch! ", end='', flush=True)
        return EventResult(False, 1)

    def defeat_result(self):
        print("Grr! ", end='', flush=True)
        return EventResult(True, 0, 3, 1)

    def response(self):
        print("It's a scary monster! Attack with [i j k l]")
