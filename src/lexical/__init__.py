import re
from __init__ import RawLine

class LexicalRule:
    def parse(self, group, action, reader):
        raise NotImplementedError("Should have implemented this")

class Block(LexicalRule):
    def opening_tag(self, params):
        raise NotImplementedError("Should have implemented this")
    def closing_tag(self):
        raise NotImplementedError("Should have implemented this")
    def parse(self, reader, params):
        reader.writeline(self.opening_tag(params))
        reader.open_block()
        reader.parse_current_level()
        reader.close_block()
        reader.writeline(self.closing_tag())

class Statement(LexicalRule):
    def tag(self, params):
        raise NotImplementedError("Should have implemented this")
    def parse(self, reader, params):
        reader.writeline(self.tag(params))

class GrammarLine(RawLine):
    def 

class GrammarReader:
    lines = []
    
    def __init__(self, file):
        self.lines = [line.rstrip() for line in open(file)]
        
    def read_grammar_line(self):
        return (GrammarLine(self.lines.pop(0)))

class SyntaxForest:
    
    trees = []
    grammar_reader = None
    
    def __init__(self, file):
        self.grammar_reader = GrammarReader(file)
        while not self.grammar_reader.eof():
            line = self.grammar_reader.read_grammar_line()
            line.
            

class SyntaxTree:
    grammar_reader = None
    def __init__(self):
    
    
    
class SyntaxNode:
    token = ""
    children = []

class Line():
    line = ""
    def __init__(self, line):
        self.line = line
    
    def indent_level(self):
        match = re.match(r'(\s+)', self.line)
        if not match:
            return 0
        else:
            indent = match.groups()[0]
            level = indent.__len__()
            if not isinstance(level, int):
                raise SyntaxError("Wrong indentation")
            return level
    
    def empty(self):
        return self.line.__len__() == 0
        
        