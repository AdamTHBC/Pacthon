import time

from Important import refresh_rate, ArrowKeyList
from Map import Map
from Objects import Objects
from getkey import getkey

o = Objects()
h = o.lists.get('hero')
for x in range(10):
    o.spawn('item')
    o.spawn('gold')
    o.spawn('monster')

print("""
arrows - move
wsad - look
ijkl - attack
q - quit
any button - Start
""")
getkey()

m = Map()
m.draw(o)

licznik = 0

while True:
    
    key = getkey()
    if key in ArrowKeyList:
        h.ster(key)
        result = m.collision(o)
        if (result != 0):
            h.hp -= result.damage
            h.experience += result.experience
            h.gold += result.gold
        m.draw(o)
        time.sleep(refresh_rate)
        licznik += 1
    elif key in "wsad":
        m.look_at(o, key)
        time.sleep(refresh_rate)
        licznik += 1
    elif key in "ijkl":
        result = m.attack(o, key)
        if (result != 0):
            h.hp -= result.damage
            h.experience += result.experience
            h.gold += result.gold
        m.draw(o)
        time.sleep(refresh_rate)
        licznik += 1
    objects_left = o.count()
    if (key == 'q' or h.hp <= 0 or objects_left == 0):
        m.draw(o)
        print("final score:", 5 * h.experience + 4 * h.gold + 10 * h.hp - licznik)
        print("THE END")
        break
