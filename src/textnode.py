from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "links"
    IMAGE = "images"

class TextNode():
    def __init__(self, text, text_type: TextType, url = None) -> None:
        self.text = text
        self.text_type = text_type.value
        self.url = url
        
    def __eq__(self, value: object) -> bool:
        return value.text == self.text and value.text_type == self.text_type and value.url == self.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


