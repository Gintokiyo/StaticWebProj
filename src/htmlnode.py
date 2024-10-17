

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("Not implemented in HTMLNode")
    
    def props_to_html(self):
        props_result = ""
        for prop in self.props:
            props_result += f" {prop}={self.props[prop]}"
        return props_result
    
    def __repr__(self) -> str:
        return f"{type(self)}:\nTag: {self.tag}\nValue:{self.value}\nChildren:{self.children}\nProps:{self.props}"
