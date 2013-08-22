import re
from css import CssParser
from html import HtmlParser
from js import JavascriptParser
from plate import TemplateParser
from lexical import Line 

class MainParser:
    level = 0
    reader = None
    writer = None
    css = None
    html = None
    js = None
    plate = None
    
    def __init__(self, file):
        self.reader = Reader(file)
        self.writer = Writer()
        self.css = CssParser(self)
        self.html = HtmlParser(self)
        self.js = JavascriptParser(self)
        self.plate = TemplateParser(self)

    def parse(self):
        while not self.reader.eof():
            line = self.reader.next_unyfy_line()
            if line.is_empty:
                self.writeline("")
            elif line.indent_size != self.level:
                raise SyntaxError('Indent is incorrect')
            elif line.is_content_only():
                self.writeline(line.content())
            elif not line.is_comment:
                self.call_method(line.declaration)
        
    def call_method(self, declaration):
        if declaration.cls == 'css':
            getattr(self.css, 'parse_' + declaration.method)(declaration.param_list)
        elif declaration.cls == 'html':
            getattr(self.html, 'parse_' + declaration.method)(declaration.param_list)
        elif declaration.cls == 'js':
            getattr(self.js, 'parse_' + declaration.method)(declaration.param_list)
        elif declaration.cls == 'plate':
            getattr(self.plate, 'parse_' + declaration.method)(declaration.param_list)
    
    def open_block(self):
        self.level = self.level + 1
        
    def close_block(self):
        self.level = self.level - 1
        if self.level < 0:  
            raise IndexError("Level tried to go below 0")
    
    def read_current_level(self):
        self.reader.read_entire_level(self.level)
        block = []
        current_level = self.level
        line = Line(self.lines.pop(0))
        while line.indent_level() >= current_level:
            block.append(line.line)
            line = Line(self.lines.pop(0))
        self.lines.insert(0, line.line)
        return block
    
    def output(self):
        return self.writer.lines
    
    def unindented_writeline(self, line):
        self.writer.writeline(line)
    
    def writeline(self, line):
        self.writer.writeline(' '*4*self.level + line)
            
class Writer:
    lines = []
    def writeline(self, line):
        self.lines.append(line)
    
'''def get_instance_of(cls):
    parts = cls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m()'''

class Reader:
    file = None
    lines = []
    
    def __init__(self, file):
        self.lines = [line.rstrip() for line in open(file)]
    
    ''' def open_block(self):
        self.level = self.level + 1
        
    def close_block(self):
        self.level = self.level - 1
        if self.level < 0:  
            raise IndexError("Level tried to go below 0")'''
    
    def next_unyfy_line(self):
        return UnyfyLine(self.lines.pop(0))
    
    def is_indent_correct(self, indent):
        return (indent == ' '*self.level*4)

    def eof(self):
        return (not self.lines)

    def read_entire_level(self, level):
        block = []
        while not self.eof():
            line = self.next_unyfy_line()
            if line.indent_size >= level:
                block.append(line.content())
            else:
                break
        self.lines.insert(0, line.content()) 
        return block
    '''def read_current_level(self):
        block = []
        current_level = self.level
        line = Line(self.lines.pop(0))
        while line.indent_level() > current_level:
            block.append(line.line)
            line = Line(self.lines.pop(0))
        self.lines.insert(0, line.line)
        return block'''
    
class UnyfyLine:
    is_empty = False
    is_comment = False
    indent_size = None
    declaration = None
    
    def __init__(self, line):
        print("Line read is: " + line)
        indent, content = "", ""
        indent, content = re.search(r'(\s*)(.*)', line).groups()
        if not content:
            self.is_empty = True
        else:
            self.validate_indent(indent)
            self.declaration = Declaration(content)

    def validate_indent(self, indent):
        self.indent_size = indent.__len__()/4
        if isinstance(self.indent_size, int):
            raise IndentationError('Indent should be a 4 multiple')
        
    def is_content_only(self):
        return (self.declaration.is_content_only)
    
    def content(self):
        return (self.declaration.content)

class Declaration:
    cls = ""
    method = ""
    param_list = []
    is_content_only = False
    content = ""
    def __init__(self, content):
        self.content = content
        list = re.match('(\w+)\.(\w+)\(?([^)]*)\)?', content)
        if list:
            list = list.groups()
            self.validate_declaration(list[0], list[1])
            param_string = list[2]
            self.param_list = param_string.split(', ')
        elif '"' in content:
            self.is_content_only = True
    
    def validate_declaration(self, cls, method):
        self.cls = cls
        self.method = method
        if (self.cls and not self.method) or (not self.cls and self.method):
            raise SyntaxError('Invalid declaration')

def main():
    file = "in.p2h"
    parser = MainParser(file)
    parser.parse()
    return parser.output

if __name__ == "__main__":
    main()