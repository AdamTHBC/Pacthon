import time

from Hero import Hero
from Important import refresh_rate
from Item import Objects
from Map import Map
from getkey import getkey

h = Hero()
o = Objects()
for x in range(10):
    o.spawn()

m = Map()
m.draw(h, o.l)

licznik = 0

while True:
    
    key = getkey()
    if key is not None:
        h.ster(key)
        m.draw(h, o.l)
        m.collision(h, o.l)
        time.sleep(refresh_rate)
        licznik += 1
    if key == 'q':
        break

print("Zjadlem ", h.score, " rzeczy.")
