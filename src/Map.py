
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
        for i in objects.list_keys:
            for j in objects.lists.get(i):
                if (objects.lists.get('hero').x == j.x and objects.lists.get('hero').y == j.y):
                    if (j.collision_deadly()):
                        return True
                    objects.lists.get(i).remove(j)
                    objects.lists.get('hero').eat()
        return False
