
import re

global_reader = None
global_writer = None

class RawLine(object):
    indent, content = None, ""
    def __init__(self, line):
        indent_string, self.content = re.match(r'(\s*)(.*)', line).groups()
        self.indent = Indent(indent_string, self.indent_size())
        
    def level(self):
        return self.indent.level()
        
    def _validate_indent(self):
        if not self.indent.is_valid():
            raise SyntaxError('Bad indentation')
        
    def is_block(self):
        return self.content[-1:] == ':'
    
    def empty(self):
        return not self.content
    
    def indent_size(self):
        return 4


class GrammarLine(RawLine):
    def indent_size(self):
        return 2

    
class Indent:
    indent = ""
    indent_size = 4
    
    def __init__(self, indent, indent_size):
        self.indent = indent
        self.indent_size = indent_size
    
    def level(self):
        return self.indent.__len__()/self.indent_size
        
    def is_valid(self):
        return not (self.indent.__len__()/self.indent_size) % 1
    
    
class Reader(object):
    def __init__(self, file):
        self.open(file)
               
    def open(self, file):
        self.lines = [line.rstrip() for line in open(file)]
    
    def eof(self):
        return (not self.lines)

    def __iter__(self):
        return self
    
    def next(self):
        if self.eof():
            raise StopIteration
        else:
            return self.readline()

    def push(self, line):
        self.lines.insert(0, line)

    def readline(self):
        line = ""
        while not line and not self.eof():
            line = self.lines.pop(0)
        return (line)


class Writer(object):
    lines = []
    def writeline(self, line):
        self.lines.append(line)


class RawGrammarReader(Reader):
    def readline(self):
        return GrammarLine(super(RawGrammarReader, self).readline())













