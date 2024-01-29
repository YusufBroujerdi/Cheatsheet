from enum import Enum
from typing import Self
from typing import List
import itertools
import json



Content = Enum('Content', ['Section', 'Text'])



class SheetItem:


    title : str
    owner : Self
    content : str | List[Self]


    def __init__(self,
        title : str,
        content : str | List[Self],
        owner : Self = None):

        self.title = title
        self.owner = owner
        self.content = content


    def content_type(self) -> Content:

        if isinstance(self.content, str):
            return Content.Text
        else:
            return Content.Section


    def parse_sheet_item(node : dict):
        return SheetItem(node['title'], node['content'])



class CheatSheet:

    sheet_tree : SheetItem
    current_node : SheetItem

    def __init__(self, cheatsheet_src : str):

        self.sheet_tree = SheetItem('Root', [])

        with open('../data/cheatsheet.txt', 'r') as file:
            src : str = file.read()

        src_parsed = json.loads(src,
            object_hook = SheetItem.parse_sheet_item)

        CheatSheet.add_owners(src_parsed)
        self.sheet_tree.content = src_parsed
       

    def add_owners(src_json : List[SheetItem],
                   current_owner : SheetItem = None) -> List[SheetItem]:

        for item in src_json:

            item.owner = current_owner

            if item.content_type() == Content.Section:
                CheatSheet.add_owners(item.content, item)
       

    def __del__():
        pass

        


if __name__ == '__main__':
    pass


