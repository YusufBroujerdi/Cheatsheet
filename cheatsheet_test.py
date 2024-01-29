import unittest
from src import cheatsheet as cs
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

js_1 = [cs.SheetItem("Section 1",
        "Herro, my name is YouSniffYourTurdy"),
    cs.SheetItem("Section 2",
        "Some more content for ya"),
    cs.SheetItem("Yet Another Subsection",
        [cs.SheetItem("Subsection 1",
                "I'm in Subsection 1!"),
            cs.SheetItem("Subsection 2",
                "I'm in Subsection 2!")
        ]),
    cs.SheetItem("Last Subsection",
        [cs.SheetItem("Last Subsubsection",
                [cs.SheetItem("Last Subsubsubsection",
                        "Holy moly.....")
                ])
        ])
]



class TestLoader(unittest.TestCase):


    def test_json_parsing(self):

        def json_load(file_text: str) -> dict:
            return json.loads(file_text, object_hook=cs.parse_sheet_item)

        my_json = json_load(cs_1)

        assert(my_json[0].title == "Section 1")
        assert(my_json[0].content == "Herro, my name is YouSniffYourTurdy")
        assert(my_json[1].owner == None)
        assert(my_json[2].title == "Yet Another Subsection")
        assert(js_1[2].title == "Yet Another Subsection")
        assert(my_json[2].content[0].title == "Subsection 1")
        #assert(my_json == js_1)

        

if __name__ == "__main__":

    unittest.main()
