from unicurses import *

def main():
    stdscr = initscr()

    start_color()
    noecho()
    curs_set(False)
    keypad(stdscr,True)

    window = newwin(3,20,5,5)
    box(window)
    wmove(window,1,1)
    waddstr(window, "Hey you!")

    window2 = newwin(3,20,4,4)
    box(window2)
    wmove(window2,1,1)
    waddstr(window2, "Hey you second!")
    

    panel = new_panel(window)
    panel2 = new_panel(window2)

    #move_panel(panel,10,30)
    top_panel(panel)
    panel

    


    running = True
    while (running):
        key = getch()
        if (key == 27):
            running = False
            break
        update_panels()
        doupdate()


    endwin()

if (__name__ == "__main__"):
    main()
