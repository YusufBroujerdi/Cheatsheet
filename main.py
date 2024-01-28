from enum import Enum
import itertools
import json



Content = Enum('Content', ['Section', 'Text'])



class SheetItem:


    title : str
    owner: SheetItem
    content


    def __init__(title, owner, content):

        self.title = title
        self.owner = owner
        self.content = content


    def content_type(self):

        if isinstance(self.content, str):
            return Content.Text
        else:
            return Content.Section



class CheatSheet:

    sheet_tree : dict
    current_node : dict

    def __init__(cheatsheet_src : str):

        self.sheet_tree = SheetItem('Root', None, [])

        with open('src.txt', 'r') as file:
            src = file.read()

        if src == '':
            return

        tips = src.split('\n\n\nnEWy\n\n')
        current_ancestors : list = [self.sheet_tree]

        for i in range(0, len(tips), 2):

            new_title = tips[i].split('\n')[0]
            new_owner_title = tips[i].split('\n')[1]
            new_type = tips[i].split('\n')[2]
            new_content = tips[i + 1]

            for i, ancestor in enumerate(current_ancestors):
                if ancestor.title == new_owner_title:
                    new_owner = ancestor
                    current_ancestors = current_ancestors[: i + 1]
                    break

            if new_type == Content.Text.value:
                new_item = SheetItem(new_title, new_owner, new_content)
                current_ancestors[-1].content.append(new_item)
            else:
                new_item = SheetItem(new_title, new_owner, [])
                current_ancestors[-1].content.append(new_item)
                current_ancestors.append(new_item)

          

    def __del__():

        





if __name__ == '__main__':


