import re
from css import CssDictionary
from lexical import Line


def get_instance_of(cls):
    parts = cls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m()

class Reader:
    level = 0
    file = None
    lines = []
    output = []
    cssDictionary = CssDictionary()
    def __init__(self, file):
        self.lines = [line.rstrip() for line in open(file)]
        self.level = 0
    
    def is_indent_correct(self, indent):
        return (indent == ' '*self.level*4)
    
    def writeline(self, line):
        self.output.append(' '*self.level*4 + line)
        
    def eof(self):
        return (not self.lines)
    
    def open_block(self):
        self.level = self.level + 1
        
    def close_block(self):
        self.level = self.level - 1
        if self.level < 0:  
            raise IndexError("Level tried to go below 0")
    
    def parse_nextline(self):
        line = Line(self.lines.pop(0))
        if line.empty():
            self.writeline('')
        elif re.search(r'\s+\"', line.line):
            self.writeline(line.line)
        else:
            declaration = Declaration(line.line)
            declaration.parse(self)
    
    def read_current_level(self):
        block = []
        current_level = self.level
        line = Line(self.lines.pop(0))
        while line.indent_level() >= current_level:
            block.append(line.line)
            line = Line(self.lines.pop(0))
        self.lines.insert(0, line.line)
        return block
    
    def parse_current_level(self):
        current_level = self.level
        while not self.eof() and current_level == self.level:
            self.parse_nextline()
            
    def parse(self):
        while not self.eof():
            self.parse_nextline()

class Declaration:
    group = ""
    element = ""
    params = ""
    def __init__(self, line):
        print(line)
        list = re.search('(\w+)\.(\w+)\(?([^)]*)\)?', line).groups()
        self.group = list[0]
        self.element = list[1]
        self.params = list[2]
        
    def parse(self, reader):
        instance = get_instance_of(self.group + '.' + self.element.title())
        instance.parse(reader, self.params)

def call_method(module, cls, method):

def main():
    file = "in.p2h"
    reader = Reader(file)
    reader.parse()
    print(reader.output)
    return reader.output

if __name__ == "__main__":
    main()