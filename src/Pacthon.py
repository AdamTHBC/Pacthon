from unicurses import *

from Hero import Hero
from Map import Map
from Objects import Objects

o = Objects()
h = o.lists.get('hero')
for x in range(10):
    o.spawn('item')
    o.spawn('gold')
    o.spawn('monster')

move_keys = [65, 66, 67, 68]
look_keys = "wasd"
attack_keys = "ijkl"

stdscr = initscr()
noecho()
curs_set(False)
stdscr.addstr(0, 0, """"
arrows - move\n
wsad - look\n
ijkl - attack\n
q - quit\n
any button - Start\n
""")


m = Map()
m.draw(stdscr, o)

licznik = 0

while True:
    """bug do naprawienia - nie pokazuje wiadomosci z obiektow, printuja sie poza loopem rysowania mapy"""
    key = getch()
    stdscr.erase()
    if key in [65, 66, 67, 68]:
        h.ster(key)
        result = m.collision(stdscr, o)
        if (result != 0):
            h.hp -= result.damage
            h.experience += result.experience
            h.gold += result.gold
    elif chr(key) in look_keys:
        m.look_at(stdscr, o, chr(key))
    elif chr(key) in attack_keys:
        result = m.attack(stdscr, o, chr(key))
        if (result != 0):
            h.hp -= result.damage
            h.experience += result.experience
            h.gold += result.gold

    objects_left = o.count()
    if (chr(key) == 'q' or h.hp <= 0 or objects_left == 0):
        stdscr.addstr(0, 1, "final score:" + str(5 * h.experience + 4 * h.gold + 10 * h.hp - licznik))
        stdscr.addstr(1, 5, "THE END")
        break

    #    stdscr.addstr(max_y+5,0, "Aby zakonczyc GRE nacisnij q...")
    licznik += 1
    m.draw(stdscr, o)

# o.hello(stdscr)
stdscr.getch()
