import re
from css import CssParser
from html import HtmlParser
from js import JavascriptParser
from plate import TemplateParser
from lexical import SyntaxForest
from lines.reader import Reader
from lines import RawLine

class Translator:
    level = 0
    reader = None
    writer = None
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

    def translate(self):
        while not self.reader.eof():
            tokens = self.reader.next_token_line()
            self.forest.traverse(tokens)
            

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
        #tokenize de lineas, entonces, cada linea se va a tokenizar...
        
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
        line = RawLine(self.lines.pop(0))
        while line.indent_level() >= current_level:
            block.append(line.line)
            line = RawLine(self.lines.pop(0))
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



def main():
    file = "in.p2h"
    translator = Translator(file)
    translator.translate()
    return translator.translate()
    '''parser = MainParser(file)
    parser.parse()
    return parser.output'''

if __name__ == "__main__":
    main()