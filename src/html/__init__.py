from lexical import Block
from lexical import Statement

class HtmlParser():
    def parse_html(self, params):
        self.write_block(Tag("html", params))
        
    def parse_body(self, params):
        self.write_tag_block(Tag("body", params))
        
    def parse_head(self, params):
        self.write_tag_block(Tag("head", params))
        
    def parse_doctype(self, params):
        self.write_tag_statement(Tag("!DOCTYPE", params))
        
    def parse_footer(self, params):
        self.write_tag_block(Tag("footer", params))
    
    def write_tag_block(self, tag):
        self.reader.writeline(tag.opening())
        self.reader.open_block()
        self.reader.parse_current_level()
        self.reader.close_block()
        self.reader.writeline(tag.closing())
        
    def write_tag_statement(self, tag, params):
        self.reader.writeline(tag)

class Tag:
    tagId = ""
    params = ""
    def __init__(self, tagId, params):
        self.tagId = tagId
        self.params = params
    def opening(self):
        return ("<" + self.tagId + self.params + ">")
    
    def closing(self):
        return ("</" + self.tagId + ">")    