
from Important import max_x,max_y


class Map:
    def __init__(self):
        "nothing"

    def draw(self, objects):
        y = 0
        print("")
        print("/--------------------\\")
        while (y < max_y):
            x = 0
            print("|",end='', flush=True)
            while (x < max_x):
                if (x == objects.get('hero').x and y == objects.get('hero').y):
                    print("H", end='', flush=True)
                else:
                    spot_free = True
                    for i in objects.get('items'):
                        if (x == i.x and y == i.y):
                            print("O", end='', flush=True)
                            spot_free = False
                    if (spot_free):
                        for i in objects.get('monsters'):
                            if (x == i.x and y == i.y):
                                print("M", end='', flush=True)
                                spot_free = False
                    if (spot_free):
                        print(" ", end='', flush=True)
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
