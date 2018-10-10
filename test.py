from curses import *

def main(stdscr):
    stdscr = initscr()

    start_color()
    echo()
    #noecho()
    curs_set(False)
    stdscr.keypad(True)
    
    running = True
    while (running):
        key = stdscr.getch()
        if (key == 27):
            running = False
            break


    endwin()

wrapper(main)