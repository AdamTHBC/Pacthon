from Important import max_x,max_y


class Hero:
    def __init__(self):
        self.x = max_x / 2
        self.y = max_y / 2
        self.score = 0

    def ruch(self, kierunek):
        if (kierunek == 1 and self.y < max_y):
            self.y += 1
        if (kierunek == 2 and self.x < max_x):
            self.x += 1
        if (kierunek == 3 and self.y > 1):
            self.y -= 1
        if (kierunek == 4 and self.x > 1):
            self.x -= 1

    def ster(self,key):
        if key == 65:   #UP
            self.ruch(3)
        if key == 66:   #DOWN
            self.ruch(1)
        if key == 67:    #RIGHT
            self.ruch(2)
        if key == 68:     #LEFT
            self.ruch(4)
        else:
            "nothing"


    def eat(self):
        self.score += 1
