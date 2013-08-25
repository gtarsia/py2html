import re
from css import CssParser
from html import HtmlParser
from js import JavascriptParser
from plate import TemplateParser
from lexical import SyntaxTree
from lexical import Line 

class MainParser:
    level = 0
    reader = None
    writer = None
    tree = None
    css = None
    html = None
    js = None
    plate = None
    syntax_forest = None
    
    def __init__(self, file):
        self.syntax_forest = SyntaxForest('grammar.grm')
        self.reader = Reader(file)
        self.writer = Writer()
        self.css = CssParser(self)
        self.html = HtmlParser(self)
        self.js = JavascriptParser(self)
        self.plate = TemplateParser(self)

    def parse(self):
        #tokenize de lineas, entonces, cada línea se va a tokenizar...
        
        while not self.reader.eof():
            line = self.reader.next_unyfy_line()
            if line.is_empty():
                self.writeline("")
            elif line.indent_size() != self.level:
                raise SyntaxError('Indent is incorrect')
            elif line.is_content_only():
                self.writeline(line.content())
            elif not line.is_comment():
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
    
    def next_line_tokens(self):
        return self.tokenize(self.lines.pop(0))
    
    def tokenize(self):
        tokens = []
        
    
    
    
    
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
            if line.indent_size() >= level:
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
class Indent:
    indent = ""
    
    def __init__(self, indent):
        self.indent = indent
        
    def size(self):
        return self.indent.__len__()/4
        
    def is_valid(self):
        return not (self.indent.__len__()/4) % 1
    
class LineType:
    Declaration, Comment, ContentOnly, Empty = range(4)
            
class RawLine:
    indent_size = None
    indent, content = None, ""
    def __init__(self, line):
        indent_string, self.content = re.match(r'(\s*)(.*)', line).groups()
        self.indent = Indent(indent_string)
        
    def validate(self):
        self.indent.validate()

class UnyfyLine(RawLine):
    line_type = LineType.Comment
    _indent_size = None
    declaration = None
    
    def __init__(self, line):
        print("Line read is: " + line)
        super(RawLine, UnyfyLine).__init__(line)
        self._validate_line_type()
        
    def validate(self):
        super(UnyfyLine, self).validate()
    
    def _validate_line_type(self):
        if not self.content:
            self.line_type = LineType.Empty
        elif self.content[0] == '#':
            self.line_type = LineType.Comment
        elif self._validate_indent() and self.content[0] == '"':
            self.line_type = LineType.ContentOnly
        elif self._validate_declaration():
            self.line_type = LineType.Declaration
    
    def _validate_declaration(self, raw_line):
        declaration = Declaration(raw_line.content)
        if not declaration.is_valid():
            raise SyntaxError('Wrong declaration')
        else:
            self.declaration = declaration
            return True
    
    def is_declaration(self):
        return self.line_type == LineType.Declaration
    def is_comment(self):
        return self.line_type == LineType.Comment
    def is_content_only(self):
        return self.line_type == LineType.ContentOnly
    def is_empty(self):
        return self.line_type == LineType.Empty


        

class Declaration:
    cls = ""
    method = ""
    param_list = []
    _is_valid = True
    def __init__(self, content):
        self.content = content
        list = re.match('(\w*)\.(\w*)\(?([^)]*)\)?', content)
        if list:
            list = list.groups()
            self.cls = list[0]
            self.method = list[1]
            self._validate_declaration(self.cls, self.method)
            param_list = list[2].split(', ')
     
    def _validate_declaration(self, cls, method):
        if not cls or not method:
            self.is_valid = False

    def is_valid(self):
        return self.is_valid

def main():
    file = "in.p2h"
    parser = MainParser(file)
    parser.parse()
    return parser.output

if __name__ == "__main__":
    main()