import unittest
from src.cheatsheet import SheetItem
from src.cheatsheet import CheatSheet
import json
import os



cs_1 = '''
[{"title" : "Section 1",
        "content" : "Herro, my name is YouSniffYourTurdy"},
    {"title" : "Section 2",
        "content" : "Some more content for ya"},
    {"title" : "Yet Another Subsection",
        "content" : [{"title" : "Subsection 1",
                "content" : "I'm in Subsection 1!"},
            {"title" : "Subsection 2",
                "content" : "I'm in Subsection 2!"}
    ]},
    {"title" : "Last Subsection",
        "content" : [{"title" : "Last Subsubsection",
            "content" : [{"title" : "Last Subsubsubsection",
                "content" : "Holy moly....."}
        ]}
    ]}
]
'''

js_1 = [SheetItem("Section 1",
        "Herro, my name is YouSniffYourTurdy"),
    SheetItem("Section 2",
        "Some more content for ya"),
    SheetItem("Yet Another Subsection",
        [SheetItem("Subsection 1",
                "I'm in Subsection 1!"),
            SheetItem("Subsection 2",
                "I'm in Subsection 2!")
        ]),
    SheetItem("Last Subsection",
        [SheetItem("Last Subsubsection",
                [SheetItem("Last Subsubsubsection",
                        "Holy moly.....")
                ])
        ])
]


def check_sections(loaded_json):

    assert(loaded_json[0].title == "Section 1")
    assert(loaded_json[0].content == "Herro, my name is YouSniffYourTurdy")
    assert(loaded_json[1].owner == None)
    assert(loaded_json[2].title == "Yet Another Subsection")
    assert(loaded_json[2].content[0].title == "Subsection 1")
    #assert(loaded_json == js_1)
    

def check_owners(loaded_json):
    assert(loaded_json[0].owner == None)
    assert(loaded_json[2].content[0].owner.title == "Yet Another Subsection")
    assert(loaded_json[2].content[1].owner.title == "Yet Another Subsection")
    assert(loaded_json[3].owner == None)
    assert(loaded_json[3].content[0].owner.title == "Last Subsection")
    assert(loaded_json[3].content[0].content[0].owner.title == "Last Subsubsection")


class TestLoader(unittest.TestCase):

    parsed_json = None
    text_file_path = None

    def setUp(self):

        def json_load(file_text: str) -> dict:
            return json.loads(file_text,
                object_hook= SheetItem.parse_sheet_item)

        self.parsed_json = json_load(cs_1)
        self.text_file_path = 'test.txt'

        with open(self.text_file_path, 'w') as file:
            file.write(cs_1)


    def test_json_parsing(self):

        check_sections(self.parsed_json)


    def test_adding_owners(self):

        CheatSheet.add_owners(self.parsed_json)
        check_owners(self.parsed_json)


    def test_use_cheatsheet(self):


        test_sheet = CheatSheet(self.text_file_path)
        check_sections(test_sheet.sheet_tree.content)
        check_owners(test_sheet.sheet_tree.content)
        del test_sheet

        test_sheet_2 = CheatSheet(self.text_file_path)
        check_sections(test_sheet_2.sheet_tree.content)
        check_owners(test_sheet_2.sheet_tree.content)
        del test_sheet_2


    def tearDown(self):
        os.remove(self.text_file_path)
      

       
if __name__ == "__main__":

    unittest.main()
