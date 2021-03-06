from src.map_objects.Actor import Actor


class Hero(Actor):
    """Main hero, only one"""
    mark = 'H'
    type_name = 'Hero'
    obstacle = False

    def __init__(self, x, y, name, mark):
        self.max_hp = 3
        super().__init__(x, y)
        self.name = name
        self.mark = mark
        self.status = 'good'
