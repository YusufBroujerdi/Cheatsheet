import curses

def initialize_stdscr(main_func):

    def new_main():

        stdscr = curses.initscr()

        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        try:
            main_func(stdscr)

        except Exception as error:
       
            curses.echo()
            curses.nocbreak()
            stdscr.keypad(False)
            curses.endwin()
            raise error

        curses.echo()
        curses.nocbreak()
        stdscr.keypad(False)
        curses.endwin()

    return new_main



@initialize_stdscr
def main(stdscr):

    stdscr.clear()

    chosen_key = None

    for i in range(10, 0, -1):

        y = 2 * (10 - i)
        x = 0

        stdscr.addstr(y, x, f'10 divided by {i} is {10 / i}')    

        if chosen_key == None:
            stdscr.addstr(y + 1, x, 'Choose a key.')
        else:
            stdscr.addstr(y + 1, x, f'Key chosen is {chosen_key}')

        chosen_key = stdscr.getkey()

    stdscr.clear()
    stdscr.addstr(0, 0, 'End of application...')
    stdscr.getkey()





if __name__ == '__main__':

    main()



