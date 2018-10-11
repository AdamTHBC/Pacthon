from unicurses import *

def main():
    stdscr = initscr()

    start_color()
    noecho()
    curs_set(False)
    keypad(stdscr,True)

    window = newwin(10,25,3,10)
    waddstr(window,"Hello!")
    
    window2 = newwin(2,25,3,80)
    waddstr(window2,"Hello again!")

    running = True
    while (running):
        key = wgetch(window2)
        if (key == 27):
            running = False
            break


    endwin()

if (__name__ == "__main__"):
    main()