import unittest

from leafnode import LeafNode
from htmlnode import HTMLNode

class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode("This is a value", None, None)
        # print(node)
    
    def test_props(self):
        node = LeafNode("Text inside the tag", "a", {"href": "\"someLink.www\"", "important": True})
        result = node.to_html()
        # print(result)
        
    def test_only_value(self):
        node = LeafNode("Only value present")
        result = node.to_html()
        # print(result)
    
    def test_tag(self):
        node = LeafNode("This is the text", "p")
        result = node.to_html()
        # print(result)
    
if __name__ == "__main__":
    unittest.main()