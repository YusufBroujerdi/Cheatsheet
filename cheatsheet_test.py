import unittest
from src import cheatsheet as cs
import json



cs_1 = '''
[{"title" : "Section 1",
    "content" : "Herro, my name is YouSniffYourTurdy"},
    {"title" : "Section 2",
    "content" : "Some more content for ya"},
    {"title" : "Yet Another Subsection",
    "__SheetItem__" : true,
    "content" : [{"title" : "Subsection 1",
        "content" : "I'm in Subsection 1!"},
        {"title" : "Subsection 2",
        "content" : "I'm in Subsection 2!"}
    ]},
    {"title" : "Last Subsection",
    "__SheetItem__" : true,
    "content" : [{"title" : "Last Subsubsection",
        "__SheetItem__" : true,
        "content" : [{"title" : "Last Subsubsubsection",
            "content" : "Holy moly....."}
        ]}
    ]}
]
'''

js_1 = [{"title" : "Section 1",
    "content" : "Herro, my name is YouSniffYourTurdy"},
    {"title" : "Section 2",
    "content" : "Some more content for ya"},
    cs.SheetItem("Yet Another Subsection",
    None,
    [{"title" : "Subsection 1",
        "content" : "I'm in Subsection 1!"},
        {"title" : "Subsection 2",
        "content" : "I'm in Subsection 2!"}
    ]),
    cs.SheetItem("Last Subsection",
    None,
    [cs.SheetItem("Last Subsubsection",
        None,
        [{"title" : "Last Subsubsubsection",
            "content" : "Holy moly....."}
        ])
    ])
]



class TestLoader(unittest.TestCase):


    def test_json_parsing(self):

        def json_load(file_text: str) -> dict:
            return json.loads(file_text, object_hook=cs.parse_sheet_item)

        my_json = json_load(cs_1)
        #assert(my_json == js_1)

        assert(my_json[0]["title"] == "Section 1")
        assert(my_json[2].title == "Yet Another Subsection")
        assert(js_1[2].title == "Yet Another Subsection")

        

if __name__ == "__main__":

    unittest.main()
