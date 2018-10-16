import time

from Important import refresh_rate
from Map import Map
from Objects import Objects
from getkey import getkey

o = Objects()
h = o.lists.get('hero')
for x in range(10):
    o.spawn('item')
    o.spawn('monster')

m = Map()
m.draw(o)

licznik = 0

while True:
    
    key = getkey()
    if key is not None:
        h.ster(key)
        m.draw(o)
        eaten = m.collision(o)
        time.sleep(refresh_rate)
        licznik += 1
    if (key == 'q' or eaten):
        break

print("Zjadlem ", h.score, " rzeczy.")
o.hello()
