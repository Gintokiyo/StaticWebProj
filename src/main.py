from textnode import TextNode, TextType

def main():
    html_node = TextNode("My text here", TextType.BOLD, "www.google.com")
    print(html_node)

if __name__ == "__main__":
    main()
