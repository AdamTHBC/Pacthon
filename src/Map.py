
from Important import max_x,max_y


class Map:
    def __init__(self):
        "nothing"

    def draw_spot(self, x, y, objects):
        """Decide what should be drawn on a given spot"""

        "verify singular objects"
        for i in objects.non_lists:
            j = objects.lists.get(i)
            if (x == j.x and y == j.y):
                return j.mark

        "verify lists"
        for i in objects.list_keys:
            for j in objects.lists.get(i):
                if (x == j.x and y == j.y):
                    return j.mark

        return ' '

    def draw(self, objects):
        y = 0
        print("")
        print("/--------------------\\")
        while (y < max_y):
            x = 0
            print("|",end='', flush=True)
            while (x < max_x):
                print(self.draw_spot(x, y, objects), end='', flush=True)
                x = x + 1
            print("|")
            y = y + 1

        print("\\--------------------/")
        print(">", end='', flush=True)

    def collision(self, objects):
        for i in objects.get('monsters'):
            if (objects.get('hero').x == i.x and objects.get('hero').y == i.y):
                print("Ouch! ", end='', flush=True)
                return True
        for i in objects.get('items'):
            if (objects.get('hero').x == i.x and objects.get('hero').y == i.y):
                print("munch!", end='', flush=True)
                objects.get('items').remove(i)
                objects.get('hero').eat()
                return False
