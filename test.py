from unicurses import *

def main():
    stdscr = initscr()

    start_color()
    noecho()
    curs_set(False)
    keypad(stdscr,True)

    window = newwin(10,25,3,3)
    box(window)
    
    wmove(window,1,1)
    waddstr(window,"Hello!")
    

    running = True
    while (running):
        key = wgetch(window)
        if (key == 27):
            running = False
            break


    endwin()

if (__name__ == "__main__"):
    main()