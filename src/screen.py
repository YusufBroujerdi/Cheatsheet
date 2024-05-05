import curses
from cheatsheet import CheatSheet
from cheatsheet import SheetItem
from typing import List
from logger import log

def initialize_resources(main_func):

    def new_main():

        stdscr = curses.initscr()
        cs = CheatSheet('test.txt')

        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        curses.curs_set(False)

        try:
            main_func(stdscr, cs)

        except Exception as error:
       
            curses.echo()
            curses.nocbreak()
            stdscr.keypad(False)
            curses.curs_set(True)
            curses.endwin()
            del cs
            log('made it here.')
            raise error

        curses.echo()
        curses.nocbreak()
        stdscr.keypad(False)
        curses.curs_set(True)
        curses.endwin()
        del cs

    return new_main


class Screen:

    selection : List[SheetItem]

    def __init__(self, stdscr):

        self.stdscr = stdscr

        width = curses.COLS - 1
        height = curses.LINES - 2

        self.node_display = curses.newwin(height, width, 0, 0)

        y = curses.LINES - 1

        self.prompt_display = curses.newwin(1, width, y, 0)


    def display_nodes(self, title_list, title):

        self.node_display.clear()
        log("in display_nodes")
        log(title)
        self.node_display.addstr(0, 0, f'Current node: {title}')

        for n, i in enumerate(title_list, start = 1):
            self.node_display.addstr(n, 0, f'{i.title}')

        self.node_display.refresh()

        
    def update_prompt(self, buffer):

        self.prompt_display.addstr(0, 0, buffer)
        self.prompt_display.refresh()


if __name__ == '__main__':

    main()




