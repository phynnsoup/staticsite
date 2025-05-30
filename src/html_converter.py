from textnode import *
from htmlnode import *


def text_node_to_html_node(text_node):
    match (text_node):
         case TextType.TEXT:
              return LeafNode(None, text_node.value)
         case TextType.BOLD:
              return LeafNode("b", text_node.value)
         case TextType.ITALIC:
              return LeafNode("i", text_node.value)
         case TextType.CODE:
              return LeafNode("code", text_node.value)
         case TextType.LINK:
              return LeafNode("a", text_node.value, {"href": text_node.url})
         case TextType.IMAGE:
              return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
         case _:
              raise ValueError(f"Invalid text type: {text_node.text_type}")