from cheatsheet import CheatSheet
import screen
from screen import Screen
from cache import Cache
from command import Command
import curses
import string
from logger import log


digits = tuple(string.digits)

alphanum = tuple(string.ascii_lowercase
                   + string.ascii_uppercase
                   + string.digits)

chars = alphanum + (curses.KEY_BACKSPACE,)

inputs = chars + (curses.KEY_ENTER,)


class Running:

    def __init__(self):
        self.verification = True

    def __bool__(self):
        return self.verification

running = Running()

def activate_exit():
    running.verification = False


com = Command()

options = {"main" : {
    ('r',) : lambda key: com.start_op("rename"),
    ('d',) : lambda key: com.start_op("delete"),
    ('n',) : lambda key: com.start_op("navigate"),
    ('.',) : lambda key: com.navigate_up(),
    ('i',) : lambda key: com.enter_search(),
    ('q',) : lambda key: activate_exit()
    },
"mod_search" : {
    inputs : lambda key: com.mod_search(key),
    },
"rename" : {
    digits : lambda key: com.rename(key)
    },
"navigate" : {
    digits : lambda key: com.navigate(key)
    },
"delete" : {
    digits : lambda key: com.delete(key)
    }
}
    
       

@screen.initialize_resources
def main_func(stdscr, cs):

    com.initialize(cs, Cache(), Screen(stdscr))


    ct_option = "main"

    while running:

        key = stdscr.getkey()

        for key_set, ct_command in options[ct_option].items():
            if key in key_set:
                ct_option = ct_command(key)

        
if __name__ == '__main__':

    main_func()
