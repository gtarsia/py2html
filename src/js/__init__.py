

class JavascriptParser:
    reader = None
    writer = None
    mainParser = None
    
    def __init__(self, mainParser):
        self.reader = mainParser.reader
        self.writer = mainParser.writer
        self.mainParser = mainParser
        
    def parse_script(self, param_list):
        self.write_tag_block(Function("button", param_list))
    
    def write_tag_block(self, tag):
        self.reader.writeline(tag.opening())
        self.reader.open_block()
        self.reader.parse_current_level()
        self.reader.close_block()
        self.reader.writeline(tag.closing())
        
class Function:
    name = ""
    param_list = []
    def __init__(self, name, param_list):
        self.name = name
        self.param_list = param_list
    def opening(self):
        return ("function " + self.name + ' ('.join(self.param_list) + ') {')
    
    def closing(self):
        return ("}")
    
    