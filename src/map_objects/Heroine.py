from src.map_objects.Actor import Actor


class Heroine(Actor):
    """Main heroine, only one"""
    mark = 'h'
    type_name = 'Heroine'
    obstacle = False

    def __init__(self, x, y):
        self.max_hp = 3
        super().__init__(x, y)
        self.steps = 0
