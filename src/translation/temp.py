from syntax import TreeTraverser
from syntax import SyntaxForest, Stack
from reader import UnyfyReader

class TranslationBlock:
    
    def opening(self):
        raise NotImplementedError()
    
    def closing(self):
        raise NotImplementedError()

class TranslationStatement:
    
    def statement(self):
        raise NotImplementedError()

class TranslationParent():
    trans_block = None
    children = []
    
    def __init__(self, trans_block):
        self.trans_block
    
    def adopt(self, child):
        self.children.append(child)
        
    def translate(self):
        lines = []
        lines += self.translation.opening()
        lines += self.translate_children()
        lines += self.translation.closing()
        return lines
    
    def translate_children(self):
        lines = []
        for child in self.children:
            lines += child.translate()
        return lines
    
class TranslationLeaf():
    trans_statement = None
    def __init__(self, trans_statement):
        self.trans_statement = trans_statement
    
    def translate(self):
        return [self.trans_statement.statement()]


class TranslationTree:
    children = []
    
    def translate(self):
        for child in self.children:
            child.translate()
            
    def add_root(self, root):
        self.children.append(root)

class TranslationTreeBuilder:
    stack = Stack()
    tree = TranslationTree()
    last_line = None
    
    def __init__(self, file):
        self.build(file)
    
    def build(self, file):
        traverser = TreeTraverser(SyntaxForest('grammar.grm'))
        for line in UnyfyReader(file):
            self.validate(line)
            translation = traverser.get_translation(line)
            if line.is_block():
                self.adopt_as_father(TranslationParent(translation))
            else:
                self.adopt_as_child(TranslationLeaf(translation))
            while self.level() > line.level():
                self.up()

    def adopt_as_child(self, node):
        if self.last():
            self.last().adopt(node)
        else:
            self.tree.add_root(node)
    
    def adopt_as_parent(self, node):
        self.adopt_child(node)
        self.stack.push(node)
    
    def up(self):
        self.stack.pop()
    
    def validate(self, line):
        if not self.last_line:
            if line.level() != 0:
                raise SyntaxError('The first line should be of level 0')
        else:
            if self.last_line.is_block():
                if self.last_line.level() != line.level() + 1:
                    raise SyntaxError('If a block was opened, there should be at least one child statement')
            else:
                if self.last_line.level() != line.level():
                    raise SyntaxError("Last line wasn't a block, this line shouldn't be a child")
    
    def level(self):
        return self.stack.level()
    
    def last(self):
        return self.stack.last()
    
    def tree(self):
        return self.tree

