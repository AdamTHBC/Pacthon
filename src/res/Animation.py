from time import sleep

frames = [
    """
         /       \\
         \\ \\\\v// /
         <"  ^  ">
        <(O) ^ (O)>
         <  \\ /  >
          <     >
           < v >
            \\=/
    """,
    """
         /       \\
         \\ \\\\v// /
         <"  ^  ">
        <(o) ^ (o)>
         <  | |  >
          <  _  >
           </'\\>
            \\_/
    """,

    """
         /       \\
         \\ \\\\v// /
         <"  ^  ">
        <(|) ^ (|)>
         <  /"\\  >
          </' '\\>
           <. .>
            \\_/
    """,

    """
         /       \\
         \\ \\\\v// /
         <"  ^  ">
        <(\\)/W\\(/)>
         < /v v\\ >
          <^   ^>
           <^ ^>
            \\M/
    """,

    """
         /       \\
         \\ \\\\v// /
         <\\  ^  />
        <(\\\\/|\\//)>
         <\\\\\\|///>
          ===O===
           //|\\\\
            /|\\
    """,

    """
         /       \\
      \\ \\ \\\\   // / /
      \\_     v     _/
        \\ \\ \\|/ / /
       \\ \\\\\\ | /// /
       --====O====--
         _// | \\\\_ \\
        // _/|\\_ \\\\
        /  / | \\  \\
    """,

    """
     \\ \\ /       \\ / /
     \\ \\\\ \\ \\ / / // /
       \\_ \\  v  / _/
       \\  \\ \\|/ /  /
        \\\\\\\\ | ////
       --====O====--
        _/ / | \\ \\_\\
         //_/|\\_\\\\
       /   / | \\   \\
    """,

    """
         /       \\
      \\   \\     /   /
      \\_     v     _/
        \\ \\ \\|/ / /
       \\  \\     /  /
       ----  *  ----
         _ /   \\ _ \\
        /  _/|\\_  \\
        /  / | \\  \\
    """
]

frametimes = [3, 1, 1, 2, 2, 4, 2]


def show_frame(stdscr, f, t=1):
    framerate = 0.200

    stdscr.erase()
    stdscr.addstr(0, 0, frames[f])
    stdscr.refresh()
    sleep(t * framerate)


def show_animation(stdscr):
    show_frame(stdscr, 0, 3)
    show_frame(stdscr, 1)
    show_frame(stdscr, 2)
    show_frame(stdscr, 3, 3)
    show_frame(stdscr, 4)
    show_frame(stdscr, 5, 3)
    show_frame(stdscr, 6)
    show_frame(stdscr, 5)
    show_frame(stdscr, 6)
    show_frame(stdscr, 7)
    stdscr.erase()
