from unicurses import *

from Important import refresh_rate,max_x,max_y,amountItem
from Hero import Hero
from Item import Item,Objects
from Map import Map    


stdscr = initscr()
noecho()
curs_set(False)
stdscr.addstr(0,0, "Nacisnij dowolny przycisk, aby rozpoczac GRE")

h = Hero()
o = Objects()
for x in range(amountItem):
    o.spawn()

m = Map()

licznik = 0
while True:
    
    key = getch()
    h.ster(key)
    m.draw(stdscr,h,o.l)
    m.collision(stdscr,h, o.l)
    licznik += 1
    stdscr.addstr(max_y+5,0, "Aby zakonczyc GRE nacisnij q...")
    if key == ord('q'):
        break
    


o.hello(stdscr)

stdscr.addstr(max_y+2,0,"Zjadlem " + str(h.score) + " rzeczy.")
stdscr.getch()
