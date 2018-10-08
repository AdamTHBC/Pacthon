import time

from getkey import getkey

from Important import refresh_rate
from Hero import Hero
from Item import Item,Objects
from Map import Map    


h = Hero()
o = Objects()
for x in range(10):
    o.spawn()

o.hello()

m = Map()

licznik = 0
while True:
    
    key = getkey()
    if key is not None:
        h.ster(key)
        m.draw(h,o.l)
        m.collision(h, o.l)
        time.sleep(refresh_rate)
        licznik += 1
    if key == 'q':
        break


o.hello()

print("Zjadlem ", h.score, " rzeczy.")
