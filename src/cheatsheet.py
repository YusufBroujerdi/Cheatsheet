from enum import Enum
from typing import Self
from typing import List
from collections.abc import Iterable
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

        if title != '..':
            self.title = title
        else:
            raise ValueError('title cannot equal ".."')

        self.owner = owner
        self.content = content


    @property
    def content_type(self) -> Content:

        if isinstance(self.content, str):
            return Content.Text
        else:
            return Content.Section


    def parse_sheet_item(node : dict):
        return SheetItem(node['title'], node['content'])



class SheetItemEncoder(json.JSONEncoder):

    def default(self, obj):

        if isinstance(obj, SheetItem):
            return {'title' : obj.title,
                'content' : obj.content}
        else:
            return json.JSONEncoder.default(self, obj)



class CheatSheet:

    sheet_tree : SheetItem
    current_node : SheetItem
    cheat_sheet_path : str

    def __init__(self, cheat_sheet_path : str):

        self.sheet_tree = SheetItem('Root', [])
        self.cheat_sheet_path = cheat_sheet_path

        with open(self.cheat_sheet_path, 'r') as file:
            src : str = file.read()

        src_parsed = json.loads(src,
            object_hook = SheetItem.parse_sheet_item)

        CheatSheet.add_owners(src_parsed, self.sheet_tree)
        self.sheet_tree.content = src_parsed
        self.current_node = self.sheet_tree
       

    def add_owners(src_json : List[SheetItem],
                   current_owner : SheetItem = None) -> List[SheetItem]:

        for item in src_json:

            item.owner = current_owner

            if item.content_type == Content.Section:
                CheatSheet.add_owners(item.content, item)
       

    def __del__(self):

        json_text = json.dumps(self.sheet_tree.content,
            cls = SheetItemEncoder)

        with open(self.cheat_sheet_path, 'w') as file:
            file.write(json_text)


    @property
    def ct_type(self):
        return self.current_node.content_type

    @ct_type.setter
    def ct_type(self, value):
        self.current_node.content_type = value
    

    @property
    def ct_content(self):
        return self.current_node.content

    @ct_content.setter
    def ct_content(self, value):

        if self.ct_type == Content.Text\
            and isinstance(value, str):

            self.current_node.content = value

        else:
            raise TypeError('Can only alter text content directly.') 


    @property
    def ct_title(self):
        return self.current_node.title

    @ct_title.setter
    def ct_title(self, value):
    
        owner_content = self.current_node.owner.content
        if any([i.title == value for i in owner_content]):
            raise ValueError('Title name already in use.')

        self.current_node.title == value


    def navigate(self, *titles : str):

        for title in titles:

            # print(f'{self.ct_title} vs. {title}')

            if title == '..':
                self.current_node = self.current_node.owner
                continue

            for item in self.ct_content:
                if item.title == title:
                    self.current_node = item
                    break

            if self.ct_title != title:
                raise ValueError('Title name not found.')


    def filter_titles(self, title : str):
        return [i for i in self.ct_content if title in i.title]


    def get_idx(title : str, l : List[SheetItem]):
        l = [n for n, i in enumerate(l) if i.title == title]
        return l[0]
    

    def add_item(self, item : SheetItem):

        orig_title = self.ct_title
        if orig_title == 'Root':
            raise ValueError('Cannot add a section after Root.')

        self.navigate('..')
        its = self.ct_content
        item.owner = self.current_node

        if any([i.title == item.title for i in its]):
            self.navigate(orig_title)
            raise ValueError('Title name already in use.')

        its.insert(CheatSheet.get_idx(orig_title, its) + 1, item)
        self.navigate(item.title)


    def del_item(self, title : str):

        its = self.ct_content
        if any([i.title == title for i in its]):
            del its[CheatSheet.get_idx(title, its)]
        else:
            raise ValueError('Title name not in use.')
                    


class CheatSheetReader:

    cheatsheet : CheatSheet

    def __init__(self, cheatsheet : CheatSheet):

        self.cheatsheet = cheatsheet


    @property
    def current_node(self):
        return current_node
  
    

if __name__ == '__main__':

    pass

