import unittest
from src.cheatsheet import SheetItem
from src.cheatsheet import CheatSheet
from src.cheatsheet import Content
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
    assert(loaded_json[2].title == "Yet Another Subsection")
    assert(loaded_json[2].content[0].title == "Subsection 1")
    #assert(loaded_json == js_1)
    

def check_owners(loaded_json):
    assert(loaded_json[0].owner.title == 'Root')
    assert(loaded_json[2].content[0].owner.title == "Yet Another Subsection")
    assert(loaded_json[2].content[1].owner.title == "Yet Another Subsection")
    assert(loaded_json[3].owner.title == 'Root')
    assert(loaded_json[3].content[0].owner.title == "Last Subsection")
    assert(loaded_json[3].content[0].content[0].owner.title == "Last Subsubsection")


def test_error(error : BaseException, callable):

    try:
        callable()
        assert(False)
    except error:
        assert(True)
    except Exception:
        assert(False)


class TestSheetItem(unittest.TestCase):

    parsed_json = None

    def setUp(self):

        def json_load(file_text: str) -> dict:
            return json.loads(file_text,
                object_hook= SheetItem.parse_sheet_item)

        self.parsed_json = json_load(cs_1)


    def test_json_parsing(self):

        check_sections(self.parsed_json)


    def test_adding_owners(self):

        CheatSheet.add_owners(self.parsed_json, SheetItem('Root', []))
        check_owners(self.parsed_json)



class TestLoader(unittest.TestCase):

    text_file_path = None
    
    def setUp(self):

        self.text_file_path = 'test.txt'
        with open(self.text_file_path, 'w') as file:
            file.write(cs_1)
        
      
    def test_use_cheatsheet(self):

        test_sheet = CheatSheet(self.text_file_path)
        check_sections(test_sheet.current_node.content)
        check_owners(test_sheet.current_node.content)
        del test_sheet

        test_sheet_2 = CheatSheet(self.text_file_path)
        check_sections(test_sheet_2.sheet_tree.content)
        check_owners(test_sheet_2.sheet_tree.content)
        del test_sheet_2


    def tearDown(self):
        os.remove(self.text_file_path)

def ugh(ug):
    print(ug[1].owner.title == 'Root')


class TestCheatSheet(unittest.TestCase):

    text_file_path = None
    cs = None

    def setUp(self):

        self.text_file_path = 'tst.txt'
        with open(self.text_file_path, 'w') as file:
            file.write(cs_1)

        self.cs = CheatSheet(self.text_file_path)
        # print(self.cs.ct_content[0].owner)


    def test_edit_methods(self):

        self.cs.navigate('Section 1')
        assert(self.cs.ct_type == Content.Text)
        assert(self.cs.ct_content == 'Herro, my name is YouSniffYourTurdy')

        self.cs.navigate('..', 'Section 2')
        assert(self.cs.ct_title == 'Section 2')

        self.cs.add_item(SheetItem('Section 3', 'Random text.'))
        assert(self.cs.ct_content == 'Random text.')

        self.cs.ct_content = 'Random teext'
        assert(self.cs.ct_content == 'Random teext')

        self.cs.navigate('..')
        assert([i.title for i in self.cs.filter_titles('Section')]\
            == ['Section 1', 'Section 2', 'Section 3'])

        self.cs.del_item('Section 3')
        assert('Section 3' not in [i.title for i in self.cs.ct_content])


    def test_error_handling(self):

        test_error(ValueError, lambda: self.cs.add_item(SheetItem('Section 5', 'some text')))
        test_error(ValueError, lambda: self.cs.navigate('Section 7'))
        test_error(ValueError, lambda: self.cs.del_item('Section 5'))

        self.cs.navigate('Section 2')
        test_error(ValueError, lambda: self.cs.add_item(SheetItem('Section 1', 'some text')))

        def set_content_type():
            self.cs.ct_type = Content.Section
        test_error(TypeError, set_content_type)

        def set_content():
            self.cs.ct_content = SheetItem('Subsection', [])
        test_error(TypeError, set_content)

        def set_title():
            self.cs.ct_title = 'Section 1'
        test_error(ValueError, set_title)

    def tearDown(self):
        os.remove(self.text_file_path)
        
    
       
if __name__ == "__main__":

    unittest.main()
