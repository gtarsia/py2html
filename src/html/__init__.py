from comparators import RegexComparator

class GrammarNode(object):
    comparator = None
    
    @classmethod
    def try_create(cls, str):
        cls.comparator.match(str)

class HtmlParagraph(GrammarNode):
    comparator = RegexComparator('paragraph(.*)')
    def __init__(self):
        

class HtmlParser():
    
    def parse_html(self, param_list):
        None
        #return Tag("html", param_list)
        
    def parse_body(self, param_list):
        None
        #self.write_tag_block(Tag("body", param_list))
        
    def parse_head(self, param_list):
        None
        #self.write_tag_block(Tag("head", param_list))
        
    def parse_doctype(self, param_list):
        None
        #self.write_tag_statement(Tag("!DOCTYPE", param_list))
        
    def parse_footer(self, param_list):
        None
        #self.write_tag_block(Tag("footer", param_list))
    
    def parse_paragraph(self, param_list):
        None
        #self.write_tag_block(Tag("p", param_list))
    
    def parse_button(self, param_list):
        None
        #self.write_tag_block(Tag("button", param_list))

    def write_tag_block(self, tag):
        None
        #self.writer.writeline(tag.opening())
        #self.mainParser.open_block()
        #self.mainParser.parse()
        #meelf.mainParser.close_block()
        #self.writer.writeline(tag.closing())
        
    def write_tag_statement(self, tag, params):
        None
        #self.writer.writeline(tag)'''

class Tag(Translation):
    def __init__(self, tagId, param_list):
        self.tagId = tagId
        self.param_list = []
        self.param_list = param_list
        
    def opening(self):
        return ("<" + self.tagId + ' '.join(self.param_list) + ">")
    
    def closing(self):
        return ("</" + self.tagId + ">")    