from typing import List
from logger import log


class Option:

    def __init__(title : str, keys : set, command : any):

        self.title = title
        self.keys = keys
        self.command = command



class Buffer:

    _text : list

    def __init__(self):

        self._text = []

    
    def add(self, new_char : str):

        if new_char == curses.KEY_BACKSPACE:
            if self._text != []:
                self._text.pop()
            return

        self._text.append(new_char)


    def empty(self):

        self._text = []


    @property
    def text(self):

        return ''.join(self._text)


    @text.setter
    def text(self, value):

        self._text = list(value)

    

class Cache:

    search : Buffer
    rename : Buffer

    def __init__(self):
        
        self.search = Buffer()
        self.rename = Buffer()

