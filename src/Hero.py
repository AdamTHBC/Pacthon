from Important import max_x, max_y
from Map_Object import MapObject


class Hero(MapObject):
    def __init__(self):
        self.x = int(max_x / 2)
        self.y = int(max_y / 2)
        self.gold = 0
        self.experience = 0
        self.hp = 3
        self.mark = 'H'
        self.type_name = 'Hero'


    def ruch(self, kierunek):
        if (kierunek == 1 and self.y < max_y):
            self.y += 1
        if (kierunek == 2 and self.x < max_x):
            self.x += 1
        if (kierunek == 3 and self.y > 1):
            self.y -= 1
        if (kierunek == 4 and self.x > 1):
            self.x -= 1

    def ster(self, key):
        if key == 65:  # UP
            self.ruch(3)
        if key == 66:  # DOWN
            self.ruch(1)
        if key == 67:  #RIGHT
            self.ruch(2)
        if key == 68:  #LEFT
            self.ruch(4)
        else:
            "nothing"

    def eat(self, x):
        self.gold += x

    def collision_result(self):
        """not really possible"""

    def defeat_result(self):
        """game over"""

    def response(self, stdscr):
        stdscr.addstr(max_y + 2, 0, "You can't talk to yourself")

    def hello(self, stdscr, y):
        """Say hi, help debug"""
        stdscr.addstr(y, max_x + 5, str(self.type_name) + " " + str(self.x) + " " + str(self.y))
