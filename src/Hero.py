from getkey import keys

from Important import max_x,max_y


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

    def ster(self,key):
        if key == keys.UP:
            self.ruch(3)
        if key == keys.DOWN:
            self.ruch(1)
        if key == keys.RIGHT:
            self.ruch(2)
        if key == keys.LEFT:
            self.ruch(4)
        else:
            "nothing"


    def eat(self):
        self.score = self.score + 1