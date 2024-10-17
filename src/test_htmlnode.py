import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "this is a value", None, {"href": "'this is a href'", "important": True})
        # print(node)
    
    def test_props(self):
        node = HTMLNode(None, None, None, {"href": "\"https://www.google.com\"", "important": True, "Optional": False})
        # print(node.props_to_html())
        
    def test_empty(self):
        node = HTMLNode()
        # print(node)
    
if __name__ == "__main__":
    unittest.main()