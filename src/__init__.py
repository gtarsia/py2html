import re
from lines import RawLine, YAUnyfyReader
from reader import UnyfyReader, Writer
from tree import SyntaxForest

class ReaderWriter(UnyfyReader, Writer):
    None
    
class YAUnyfyParser:
    
    def __init__(self):
        None
        
    def parse(self, file):
        for statement in YAUnyfyReader(file):
            self.forest.
            
class UnyfyTree:
    
    def __init__(self):
        
    def build(self, file):

class UnyfyParser:
    level = 0
    reader_writer = None
    tree = None

    syntax_forest = None
    
    def __init__(self, file):
        self.syntax_forest = SyntaxForest('grammar.grm')
        self.reader.open(file)

    def translate(self):
        output = []
        while not self.reader.eof():
            tokens = self.reader.read_tokens_line()
            self.syntax_forest.traverse(tokens)

    def parse(self):
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
 
    def open_block(self):
        self.level = self.level + 1
        
    def close_block(self):
        self.level = self.level - 1
        if self.level < 0:  
            raise IndexError("Level tried to go below 0")
    
    def output(self):
        return self.writer.lines
    
    def unindented_writeline(self, line):
        self.writer.writeline(line)
    
    def writeline(self, line):
        self.writer.writeline(' '*4*self.level + line)

def main():
    file = "in.p2h"
    parser = UnyfyParser(file)
    return parser.translate()

if __name__ == "__main__":
    main()