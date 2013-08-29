'''
Created on 25/08/2013

@author: guidi
'''
from lines import UnyfyLine, GrammarToken
import re

class Reader(object):
    file = None
    lines = []
    
    def __init__(self, file):
        self.open(file)
               
    def open(self, file):
        self.lines = [line.rstrip() for line in open(file)]
    
    def eof(self):
        return (not self.lines)

    def push_line(self, line):
        self.lines.insert(0, line)

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
    
    def read_line(self):
        line = ""
        while not line and not self.eof():
            line = self.lines.pop(0)
        return (line)


class YAUnyfyReader(Reader):
    
    def __iter__(self):
        return self
    
    def next(self):
        line = YAUnyfyLine(self.read_line())
        while not line.empty():
            line = YAUnyfyLine(self.read_line())
        return line
    
    def _read_definition(self):
        None
    
    def _is_block(self, line):
        return line.rstrip()[-1:]


class UnyfyReader(Reader):
    
    def read_tokens_line(self):
        line = super(UnyfyReader, self).read_line()
        tokens = re.findall(r'(?:[(][^)]*[)])|\w+|\S', line)
        return tokens
                    
class Writer(object):
    lines = []
    def writeline(self, line):
        self.lines.append(line)

