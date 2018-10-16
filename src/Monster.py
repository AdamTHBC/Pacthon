class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mark = 'M'

    def hello(self):
        print("Monster ", self.x, " ", self.y)
