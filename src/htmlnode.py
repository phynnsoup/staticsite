class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        props_string = ""
        if self.props == None:
            return props_string
        for prop, value in self.props.items():
            props_string += f" {prop}=\"{value}\""
        return props_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None or self.value == "":
                raise ValueError("no value given")
        elif self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag given")
        if self.children == None or type(self.children) != list:
            raise ValueError("no or incorrect type given for child")
        content = list(map(lambda node: node.to_html(), self.children))
        return f"<{self.tag}{self.props_to_html()}>{"".join(content)}</{self.tag}>"