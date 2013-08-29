from tree import SyntaxForest
from lines import RawLine

class UnyfyNode():
    raw_line = None
    children = None
    
    def __init__(self, raw_line):
        self.children = []
        self.raw_line = raw_line

    def adopt(self, node):
        self.children.append(node)    

    def has_children(self):
        return bool(self.children)

class Stack:
    stack = None
    
    def __init__(self, node):
        self.stack = []
        self.stack.append(node)
        
    def pop(self):
        return self.stack.pop()
    
    def push(self, node):
        return self.stack.append(node)
    
    def last(self):
        return self.stack[-1]
    
    def level(self):
        return len(self.stack) - 1

class UnyfyTree(UnyfyNode):
    def __init__(self, file):
        super(UnyfyTree, self).__init__(RawLine(""))
        self.parse_file(file)
        
    def parse_file(self, file):
        stack = Stack(self)
        for line in YAReader(file):
            if line.level() < stack.level():
                if not stack.last().has_children(): 
                    raise SyntaxError('unyfy file wrong syntax')
                while line.level() < stack.level():
                    stack.pop()
            block = UnyfyNode(line)
            stack.last().adopt(block)
            if line.is_block():
                stack.push(block)
        
class YAReader(object):
    file = None
    lines = []
    
    def __init__(self, file):
        self.open(file)
               
    def open(self, file):
        self.lines = [line.rstrip() for line in open(file)]
    
    def eof(self):
        return (not self.lines)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.eof():         # threshhold terminator
            raise StopIteration 
        else:
            line = RawLine("")
            while line.empty() and not self.eof():
                if self.eof():
                    raise StopIteration
                line = RawLine(self.lines.pop(0))
            return line

class YAUnyfyParser:
    syntax_forest = SyntaxForest('grammar.grm')
    unyfy_tree = None
    
    def __init__(self, file):
        self.unyfy_tree = UnyfyTree(file)
        
    def translate(self):
        
'''class UnyfyParser:
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
        self.writer.writeline(' '*4*self.level + line)'''

def main():
    file = "in.p2h"
    parser = YAUnyfyParser(file)
    return parser.translate()

if __name__ == "__main__":
    main()