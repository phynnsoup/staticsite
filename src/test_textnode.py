import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        node4 = TextNode("This is a text node", TextType.ITALIC, "www.google.com")
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node3, node4)
    
    def test_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.ITALIC, "www.google.com")
        self.assertIsNone(node.url)
        self.assertIsNotNone(node4.url)

if __name__ == "__main__":
    unittest.main()