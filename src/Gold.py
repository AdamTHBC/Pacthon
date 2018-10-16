class Gold:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mark = 'G'

    def hello(self):
        print("Gold ", self.x, " ", self.y)

    def collision_deadly(self):
        print("yum!", end='', flush=True)
        return False
