from Engine import Engine
from Objects import Objects
from unicurses import *

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
