
from Important import max_x,max_y


class Map:
    def __init__(self):
        "nothing"

    def draw(self, hero, objects):
        y = 0
        print("")
        print("/--------------------\\")
        while (y < max_y):
            x = 0
            print("|",end='', flush=True)
            while (x < max_x):
                if (x == hero.x and y == hero.y):
                    print("H", end='', flush=True)
                else:
                    flag = True
                    for i in objects:
                        if (x == i.x and y == i.y):
                            print("O", end='', flush=True)
                            flag = False
                    if (flag):
                        print(" ", end='', flush=True)
                    # print("(", x, ", ", y, ") ", end='', flush=True)
                x = x + 1
            print("|")
            y = y + 1

        print("\\--------------------/")
        print(">", end='', flush=True)

    def collision(self, hero, objects):
        for i in objects:
            if (hero.x == i.x and hero.y == i.y):
                print("munch!", end='', flush=True)
                objects.remove(i)
                hero.eat()