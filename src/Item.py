class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mark = 'O'

    def hello(self):
        print("Item ", self.x, " ", self.y)

    def collision_result(self):
        print("munch!", end='', flush=True)
        return 1
