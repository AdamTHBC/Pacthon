from src.map_objects.Non_Actor import NonActor


class StairsUp(NonActor):
    """
    Allows going to the previous level, closer to the exit, less dangerous.

    """
    mark = 'O'
    type_name = 'StairsUp'
    obstacle = True

    def return_level(self):
        """
        Loads previous level, refilling it with monsters and treasures at random.
        """


class StairsDown(NonActor):
    """
    Allows going to the next level, farther from the exit, more dangerous.
    """
    mark = 'X'
    type_name = 'StairsDown'
    obstacle = True

    def progress_level(self):
        """
        Creates next level, filling it with monsters and treasures at random.
        """
