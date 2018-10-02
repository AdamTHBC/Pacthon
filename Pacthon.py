import time
import random

max_x = 20
max_y = 10
refresh_rate = 0.1

class Hero:
    def __init__(self):
        self.x = max_x / 2
        self.y = max_y / 2
        self.score = 0

    def ruch(self, kierunek):
        if (kierunek == 1 and self.y + 1 < max_y):
            self.y = self.y + 1
        if (kierunek == 2 and self.x + 1 < max_x):
            self.x = self.x + 1
        if (kierunek == 3 and self.y > 0):
            self.y = self.y - 1
        if (kierunek == 4 and self.x > 0):
            self.x = self.x - 1

    def eat(self):
        self.score = self.score + 1

class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hello(self):
        print("Item ", self.x, " ", self.y)

class Objects:
    def __init__(self):
        self.l = []

    def spawn(self):
        new_x = random.randint(0, max_x - 1)
        new_y = random.randint(0, max_y - 1)
        for i in self.l:
            if (new_x == i.x and new_y == i.y):
                self.spawn()
                return
        self.l.append(Item(new_x, new_y))

    def hello(self):
        for i in self.l:
            i.hello()


class Map:
    def __init__(self):
        "nothing"

    def draw(self, hero, objects):
        y = 0
        print("/--------------------\\")
        while (y < max_y):
            x = 0
            print("|", end='', flush=True)
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

    def collision(self, hero, objects):
        for i in objects:
            if (hero.x == i.x and hero.y == i.y):
                print("munch!")
                objects.remove(i)
                hero.eat()


h = Hero()
o = Objects()
o.spawn()
o.spawn()
o.spawn()
o.spawn()
o.spawn()
o.spawn()
o.spawn()
o.spawn()
o.spawn()
o.spawn()
o.spawn()
o.spawn()
o.spawn()
o.spawn()
o.spawn()
o.spawn()
o.hello()

m = Map()

h.ruch(1)
m.draw(h, o.l)
m.collision(h, o.l)
time.sleep(refresh_rate)

h.ruch(1)
m.draw(h, o.l)
m.collision(h, o.l)
time.sleep(refresh_rate)

h.ruch(1)
m.draw(h, o.l)
m.collision(h, o.l)
time.sleep(refresh_rate)

h.ruch(2)
m.draw(h, o.l)
m.collision(h, o.l)
time.sleep(refresh_rate)

h.ruch(2)
m.draw(h, o.l)
m.collision(h, o.l)
time.sleep(refresh_rate)

h.ruch(2)
m.draw(h, o.l)
m.collision(h, o.l)
time.sleep(refresh_rate)

h.ruch(3)
m.draw(h, o.l)
m.collision(h, o.l)
time.sleep(refresh_rate)

h.ruch(3)
m.draw(h, o.l)
m.collision(h, o.l)
time.sleep(refresh_rate)

h.ruch(3)
m.draw(h, o.l)
m.collision(h, o.l)
time.sleep(refresh_rate)

h.ruch(4)
m.draw(h, o.l)
m.collision(h, o.l)
time.sleep(refresh_rate)

h.ruch(4)
m.draw(h, o.l)
m.collision(h, o.l)
time.sleep(refresh_rate)

h.ruch(4)
m.draw(h, o.l)
m.collision(h, o.l)
time.sleep(refresh_rate)

o.hello()

print("Zjadlem ", h.score, " rzeczy.")
