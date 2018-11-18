from src.res.Important import max_x, max_y


class Map:
    def __init__(self, stdscr, objects):
        self.objects = objects
        self.stdscr = stdscr  # map

    def draw_spot(self, x, y):
        """Decide what should be drawn on a given spot"""

        "verify singular objects"
        for i in self.objects.non_lists:
            j = self.objects.lists.get(i)
            if (x == j.x and y == j.y):
                return j.mark

        "verify lists"
        for i in self.objects.list_keys:
            for j in self.objects.lists.get(i):
                if (x == j.x and y == j.y):
                    return j.mark

        return ' '

    def draw(self):
        y = 1

        self.stdscr.addch(0, 0, "/")
        x = 1
        while (x <= max_x):
            self.stdscr.addch(0, x, "-")
            x += 1
            self.stdscr.addch(0, max_x + 1, "\\")

        while (y <= max_y):
            x = 1
            self.stdscr.addch(y, 0, "|")
            while (x <= max_x):
                char_to_draw = self.draw_spot(x, y)
                self.stdscr.addch(y, x, char_to_draw)
                x += 1

                self.stdscr.addch(y, x, "|")
            y += 1

            self.stdscr.addch(max_y + 1, 0, "\\")
        x = 1
        while (x <= max_x):
            self.stdscr.addch(max_y + 1, x, "-")
            x += 1
            self.stdscr.addch(max_y + 1, max_x + 1, "/")
