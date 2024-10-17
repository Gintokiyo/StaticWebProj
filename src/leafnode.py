from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None) -> None:
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("Value not found")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        props = self.props_to_html()
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"
    
    def props_to_html(self):
        return super().props_to_html()
    