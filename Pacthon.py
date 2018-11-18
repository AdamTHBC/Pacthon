from unicurses import *

from src.Engine import Engine
from src.Objects import Objects

stdscr = initscr()
noecho()
curs_set(False)

engine = Engine(stdscr, Objects())
engine.game_start()

key = stdscr.getkey()
while engine.action(key):
    """game is running"""
    key = stdscr.getkey()

"""pres any button to quit"""
stdscr.getch()
