from lexical import Block
from lexical import Statement

class Html(Block):
    #manifest = ""
    #xmlns = ""
    def opening_tag(self, params):
        return "<html>"
    def closing_tag(self):
        return "</html>"

class Head(Block):
    def opening_tag(self, params):
        return "<head>"
    def closing_tag(self):
        return "</head>"

class Body(Block):
    def opening_tag(self, params):
        return "<body>"
    def closing_tag(self):
        return "</body>"

class Footer(Block):
    def opening_tag(self, params):
        return "<body>"
    def closing_tag(self):
        return "</body>"

class Doctype(Statement):
    def tag(self, params):
        return "<!DOCTYPE html>"
    
def process_html():
    return ""