import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        children_nodes = [
            LeafNode("Bold text from the first leaf node", "b"),
            LeafNode("Just text in second leafnode", None),
            LeafNode("Italic text in the third leaf", "i"),
            LeafNode("Simple text in the fourth leaf")
        ]
        node = ParentNode("p", children_nodes)
        result = node.to_html()
        print(result)
    
    def test_no_children(self):
        node = ParentNode("a", [])
        result = node.to_html()
        print(result)
        
    def test_multiple_parentnodes(self):
        children_nodes = [
            LeafNode("Bold text from the first leaf node", "b"),
            LeafNode("Just text in second leafnode", None),
            LeafNode("Italic text in the third leaf", "i"),
            LeafNode("Simple text in the fourth leaf")
        ]
        node = ParentNode("a", ParentNode("p", ParentNode("c", children_nodes)))
        result = node.to_html()
        print(result)
    
if __name__ == "__main__":
    unittest.main()