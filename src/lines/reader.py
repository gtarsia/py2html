'''
Created on 25/08/2013

@author: guidi
'''
from lines import GrammarLine
from lines import UnyfyLine

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
    '''def read_current_level(self):
        block = []
        current_level = self.level
        line = Line(self.lines.pop(0))
        while line.indent_level() > current_level:
            block.append(line.line)
            line = Line(self.lines.pop(0))
        self.lines.insert(0, line.line)
        return block''' 


class GrammarReader(Reader):
    lines = []
    
    def __init__(self, file):
        self.lines = [line.rstrip() for line in open(file)]

    def push_line(self, line):
        self.lines.insert(0, line.content)

    def read_line(self):
        print(self.lines[0])
        return (GrammarLine(self.lines.pop(0)))

class UnyfyReader(Reader):
    
    def read_line(self):
        return UnyfyLine(self.lines.pop(0))