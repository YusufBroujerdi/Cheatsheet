from enum import Enum
import itertools
import json



Content = Enum('Content', ['Section', 'Text'])



class SheetItem:


    title : str
    owner = None
    content = None


    def __init__(self, title, owner, content):

        self.title = title
        self.owner = owner
        self.content = content


    def content_type(self):

        if isinstance(self.content, str):
            return Content.Text
        else:
            return Content.Section



def parse_sheet_item(node : dict) -> SheetItem:
    return SheetItem(node['title'], None, node['content'])


class CheatSheet:

    sheet_tree : dict
    current_node : dict

    def __init__(cheatsheet_src : str):

        self.sheet_tree = SheetItem('Root', None, [])

        with open('src.txt', 'r') as file:
            src : str = file.read()

        src_json = json.loads(src, object_hook = parse_sheet_item)



    def parse_json(src_json) -> dict:

        cheatsheet : dict = dict()

        
          

    def __del__():
        pass

        





if __name__ == '__main__':
    pass


