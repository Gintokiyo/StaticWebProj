import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a test node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_wrong_eq(self):
        node = TextNode("This is unique", TextType.ITALIC)
        node2 = TextNode("This is something else", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        
    def test_url_not_eq(self):
        node = TextNode("This is a test node", TextType.BOLD, "google.com")
        node2 = TextNode("This is a test node", TextType.BOLD)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()