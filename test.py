from curses import initscr,endwin,wrapper

def main(stdscr):
    stdscr = initscr()

    for i in range(0,50):
        stdscr.refresh()
        stdscr.addstr(10,i,"Hello!")
        stdscr.getch()


    endwin()

wrapper(main)