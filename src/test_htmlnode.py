import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_is_none(self):
        node = HTMLNode("<p>", "you are sexy baby", None, None)
        node2 = HTMLNode()
        self.assertIsNone(node.props)
        self.assertIsNone(node2.tag)
        self.assertIsNotNone(node.tag)

if __name__ == "__main__":
    unittest.main()