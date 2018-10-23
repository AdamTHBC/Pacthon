import time

from unicurses import initscr,addstr,getch,refresh

from Important import refresh_rate,max_x,max_y
from Hero import Hero
from Item import Item,Objects
from Map import Map    


stdscr = initscr()

h = Hero()
o = Objects()
for x in range(10):
    o.spawn()

m = Map()

licznik = 0
while True:
    
    key = getch()
    h.ster(key)
    m.draw(h,o.l,stdscr)
    m.collision(h, o.l,stdscr)
    #time.sleep(refresh_rate)
    licznik += 1
    if key == ord('q'):
        break


o.hello(stdscr)

stdscr.addstr(max_y+4,0,"Zjadlem " + str(h.score) + " rzeczy.")
stdscr.getch()
