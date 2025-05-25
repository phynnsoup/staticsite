class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplemented
    def props_to_html(self):
        props_string = "" 
        for prop, value in self.props.items():
            props_string += f" {prop}=\"{value}\""
        return props_string
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"