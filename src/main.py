from textnode import TextNode
def main(text, text_type, url):
    dummy_text = TextNode(text, text_type, url)
    print(dummy_text)
if __name__ == "__main__":
    main("This is some anchor text", "link", "https://www.boot.dev")