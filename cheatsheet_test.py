import unittest
from src.cheatsheet import SheetItem
import json



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



class TestLoader(unittest.TestCase):

    parsed_json = None

    def setUp(self):

        def json_load(file_text: str) -> dict:
            return json.loads(file_text,
                object_hook= SheetItem.parse_sheet_item)

        self.parsed_json = json_load(cs_1)


    def test_json_parsing(self):

        assert(self.parsed_json[0].title == "Section 1")
        assert(self.parsed_json[0].content == "Herro, my name is YouSniffYourTurdy")
        assert(self.parsed_json[1].owner == None)
        assert(self.parsed_json[2].title == "Yet Another Subsection")
        assert(self.parsed_json[2].content[0].title == "Subsection 1")
        #assert(self.parsed_json == js_1)

    def test_adding_owners(self):

        pass

        

if __name__ == "__main__":

    unittest.main()
