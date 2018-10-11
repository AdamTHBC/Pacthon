import time

from getkey import getkey
from curses import initscr

from Important import refresh_rate
from Hero import Hero
from Item import Item,Objects
from Map import Map    


stdscr = initscr()

h = Hero()
o = Objects()
for x in range(10):
    o.spawn()

#o.hello(stdscr)

m = Map()

licznik = 0
while True:
    
    key = getkey()
    if key is not None:
        h.ster(key)
        m.draw(h,o.l,stdscr)
        m.collision(h, o.l)
        time.sleep(refresh_rate)
        licznik += 1
        stdscr.getch()
    if key == 'q':
        break


#o.hello(stdscr)

print("Zjadlem ", h.score, " rzeczy.")
