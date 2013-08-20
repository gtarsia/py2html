from lexical import Block
from lexical import Statement

class Html(Block):
    manifest = ""
    xmlns = ""
    def open_block(self, params):
        return "<html>"
    def close_block(self):
        return "</html>"

class Head(Block):
    def open_block(self, params):
        return "<head>"
    def close_block(self):
        return "</head>"

class Body(Block):
    def open_block(self, params):
        return "<body>"
    def close_block(self):
        return "</body>"

class Footer(Block):
    def open_block(self, params):
        return "<body>"
    def close_block(self):
        return "</body>"

class Doctype(Statement):
    def state(self, params):
        return "<!DOCTYPE html>"
    
def process_html():
    return ""