from curses import *

def main(stdscr):
    stdscr = initscr()

    start_color()
    use_default_colors()
    init_pair(1,COLOR_RED,-1)

    
    stdscr.addstr('Hello!\n',color_pair(1) + A_BOLD)
    stdscr.addstr('Hello!\n',color_pair(1))


    stdscr.getch()


    endwin()

wrapper(main)