from cheatsheet import CheatSheet
from screen import Screen
from cache import Cache
from cache import Option
from logger import log

class Command:

    def __init__(self):
        return


    def initialize(self, cs, cache, screen):

        self.cs = cs
        self.cache = cache
        self.screen = screen

        log(self.cs.ct_title)
        log(self.cs.ct_content)
        self.screen.display_nodes(self.cs.ct_content, self.cs.ct_title)
        

    def navigate_up(self):

        try:
            self.cs.navigate('..')
        except:
            return "main" #Add error message

        self.cache.search.text = ''

        self.screen.display_nodes(filtered_list, self.cs.ct_title)
        self.screen.update_prompt('')

        return "main"


    def navigate(self, key):

        key = int(key)
        filtered_list = self.cs.filter_titles(self.cache.search.text)

        if key >= len(filtered_list):
            return "main"#screen should show error later.

        title = filtered_list[key].title
        self.cs.navigate(title)

        self.cache.search.text = ''

        log('content:')
        log(self.cs.ct_content)
        for i in self.cs.ct_content:
            log(i.title)
        self.screen.display_nodes(self.cs.ct_content, self.cs.ct_title)
        self.screen.update_prompt('')

        return "main"


    def delete(self, key):

        filtered_list = self.cs.filter_titles(self.cache.search.text)
        if key >= len(filtered_list):
            return "main"#screen should show error later.

        title = self.cs.filter_titles(filtered_list)[key]
        self.cs.del_item
        filtered_list.pop(key)

        self.screen.display_nodes(filtered_list, self.cs.ct_title)

        return "main"


    def enter_search(self):

        self.screen.update_prompt(self.cache.search.text)
        curses.curs_set(True)
        return "mod_search"


    def mod_search(self, char):

        if char == curses.KEY_ENTER:
            curses.curs_set(False)
            return "main"

        self.cache.search.add(char)
        filtered_list = self.cs.filter_titles(self.cache.search.text)
        self.screen.display_nodes(filtered_list, self.cs.ct_title)
        self.screen.update_prompt(self.cache.search.text)
        return "mod_search"


    def rename(self, key):

        filtered_list = self.cs.filter_titles(self.cache.search.text)
        if key >= len(filtered_list):
            return "rename"#Screen should show error later.

        title = self.cs.filtered_titles(filtered_list)[key]
        self.cache.rename = title


    def start_op(self, op : str):

        self.screen.update_prompt(f'Enter a digit to {op}')
        return op



