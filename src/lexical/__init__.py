import re
from lines.reader import GrammarReader



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

class TreeNode:
    id = ""
    
    def __init__(self, id):
        self.id = id
    
    def traverse(self, tokens):
        raise NotImplementedError()

class SyntaxTreeRoot(TreeNode):
    children = []
    forest = None
    
    def build(self, reader):
        while not reader.eof():
            grammar_line = reader.read_line()
            if grammar_line.indent_level() < 1:
                reader.push_line(grammar_line)
                break
            else:
                node = self.generate_node(grammar_line)
                self.children[node.id] = node
        return self
    
    def generate_node(self, grammar_line):
        if grammar_line.has_method_call():
            grammar_line.content.pop(0)
            return MethodLeaf(grammar_line.content)
        elif grammar_line.has_tree_reference():
            grammar_line.content.pop(0)
            return SyntaxTreeRoot(grammar_line.content)
    
class ForestRoot(SyntaxTreeRoot):
    
    def __init__(self, reader):
        self.id = 'Main'
        self.build(reader)

class SyntaxForest:
    trees = {}
    
    def __init__(self, file):
        self.build(file)

    def build(self, file):
        reader = GrammarReader(file)
        line = reader.read_line()
        if line.content != 'Main':
            raise SyntaxError('Wrong Grammar: Root should be called Main')
        self.trees['Main'] = ForestRoot(reader)
        while not reader.eof():
            grammar_line = reader.read_line()
            self.tree_root(grammar_line.content).build(reader)
    
    def traverse(self, tokens):
        self.root().traverse(tokens)
        
    def tree_root(self, tree):
        return self.trees[tree]
    
    def forest_root(self):
        return self.trees['Main']
    
class MethodLeaf(TreeNode):
    instance = None
    method= ''
    
    def __init__(self, instance, method):
        self.instance = instance
        self.method = method
    
    def traverse(self, tokens):
        self.run_method(tokens)
    
    def run_method(self, params):
        None#Call method

class SyntaxBranch(TreeNode):
    children = []
    def compare(self):
        raise NotImplementedError() 
    
    def traverse(self, tokens):
        self.children[tokens.pop(0)].traverse(tokens)
    
class RegexBranch(SyntaxBranch):
    regex = ''
    def __init__(self, regex):
        self.regex = regex
        
    def compare(self, string):
        return re.match(self.regex, string)

class StringBranch(SyntaxBranch):
    string = ''
    def __init__(self, string):
        self.string = string
        
    def compare(self, string):
        return self.string == string

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
        
      