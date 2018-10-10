from curses import initscr,endwin,wrapper,A_REVERSE,A_BOLD

def main(stdscr):
    stdscr = initscr()

    max_y,max_x = stdscr.getmaxyx()

    stdscr.attron(A_REVERSE)
    stdscr.addstr(int(max_y/2)-1,int(max_x/2),'Hello!',A_BOLD)
    stdscr.addstr(int(max_y/2),int(max_x/2),'Hello!',)
    stdscr.attroff(A_REVERSE)
    stdscr.addstr(int(max_y/2)+1,int(max_x/2),'Hello!')

    stdscr.getch()


    endwin()

wrapper(main)