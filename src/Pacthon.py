from Animation import *
from Important import debug
from Map import Map
from Objects import Objects
from unicurses import *

frate = .200

def show_help():
    stdscr.addstr(0, 0, """
    arrows - move
    wsad - look
    ijkl - attack
    q - quit
    any button - Start
    """)

o = Objects()
h = o.lists.get('hero')

move_keys = [65, 66, 67, 68]
look_keys = "wasd"
attack_keys = "ijkl"
ignore_keys = [27, 91]

stdscr = initscr()
noecho()
curs_set(False)

show_animation(stdscr)
show_help()

while (stdscr.getch() in ignore_keys):
    stdscr.getch()
m = Map()
stdscr.erase()
m.draw(stdscr, o)

licznik = 0

while True:
    key = stdscr.getch()
    if (key in ignore_keys):
        continue

    stdscr.erase()
    if (chr(key) == 'n' and debug == True):
        o.spawn('item')
        o.spawn('gold')
        o.spawn('monster')

    if (key in move_keys):
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
        stdscr.erase()
        stdscr.addstr(0, 1, "final score:" + str(5 * h.experience + 4 * h.gold + 10 * h.hp - licznik))
        stdscr.addstr(1, 5, "THE END")
        break

    licznik += 1
    m.draw(stdscr, o)

stdscr.getch()
