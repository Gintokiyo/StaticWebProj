from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("No parent tag found!")
        if self.children == None:
            raise ValueError("No children found!")
        
        if type(self.children) == type(self):
            return f"<{self.tag}>{self.children.to_html()}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.compose_html(self.children)}</{self.tag}>"
        
    def compose_html(self, children):
        if len(children) == 0:
            return ""
        return "" + children[0].to_html() + self.compose_html(children[1:])
        
        
    def props_to_html(self):
        return super().props_to_html()
