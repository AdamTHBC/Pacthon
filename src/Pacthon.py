from Map import Map
from Objects import Objects
from unicurses import *

stdscr = initscr()
noecho()
curs_set(False)

m = Map(stdscr, Objects())

m.game_start()
while m.action():
    """game is running"""

stdscr.getch()
