from lexical.structure import Block
from lexical.structure import Statement

class HtmlParser():
    reader = None
    writer = None
    mainParser = None
    
    def __init__(self, mainParser):
        self.reader = mainParser.reader
        self.writer = mainParser.writer
        self.mainParser = mainParser
    
    def parse_html(self, param_list):
        self.write_tag_block(Tag("html", param_list))
        
    def parse_body(self, param_list):
        self.write_tag_block(Tag("body", param_list))
        
    def parse_head(self, param_list):
        self.write_tag_block(Tag("head", param_list))
        
    def parse_doctype(self, param_list):
        self.write_tag_statement(Tag("!DOCTYPE", param_list))
        
    def parse_footer(self, param_list):
        self.write_tag_block(Tag("footer", param_list))
    
    def parse_paragraph(self, param_list):
        self.write_tag_block(Tag("p", param_list))
    
    def parse_button(self, param_list):
        self.write_tag_block(Tag("button", param_list))

    def write_tag_block(self, tag):
        self.writer.writeline(tag.opening())
        self.mainParser.open_block()
        self.mainParser.parse()
        self.mainParser.close_block()
        self.writer.writeline(tag.closing())
        
    def write_tag_statement(self, tag, params):
        self.writer.writeline(tag)

class Tag:
    tagId = ""
    param_list = []
    def __init__(self, tagId, param_list):
        self.tagId = tagId
        self.param_list = param_list
    def opening(self):
        return ("<" + self.tagId + ' '.join(self.param_list) + ">")
    
    def closing(self):
        return ("</" + self.tagId + ">")    