import re
from css import CssParser
from js import JavascriptParser
from plate import TemplateParser
from lexical import GrammarParser
from html import HtmlParser

class NodeStack:
    nodes = []
    
    def push(self, node):
        self.nodes.append(node)
        
    def pop(self):
        return self.nodes.pop()

class BaseNode:
    comparator = None
    
    def __init__(self, str):
        if '$' in str:
            self.comparator = RegexComparator(str[1:])
        else:
            self.comparator = StringComparator(str)
    
    def match(self, str):
        return self.comparator.compare(str)
    
    def traverse(self, tokens):
        raise NotImplementedError()

class ParentNode(BaseNode):
    children = []
    
    def add_child(self, node):
        self.children.append(node)
        
    def traverse(self, tokens):
        node = self.find_child(self, tokens.pop(0))
        node.traverse(tokens)
        
    def find_child(self, token):
        for child in self.children:
            if child.match(token):
                return child
                
class MethodLeaf(BaseNode):
    method = None
    
    def __init__(self, method):
        self.method = method
    
    def traverse(self, tokens):
        self.run_method(tokens)
    
    def run_method(self, params):
        self.method(params)
    
class TreeReferenceLeaf(BaseNode):
    tree = None
    
    def __init__(self, pattern, tree):
        super(TreeReferenceLeaf, self).__init__(pattern)
        self.tree = tree
    
    def traverse(self, tokens):
        self.tree.traverse()
        
class StringComparator:
    string = ""
    
    def __init__(self, string):
        self.string = string
        
    def compare(self, string):
        return self.string == string

class RegexComparator:
    pattern = ""
    
    def __init__(self, pattern):
        self.pattern = pattern

    def compare(self, string):
        return bool(re.match(self.pattern, string))

class Tree(ParentNode):
    syntax_forest = None
    
    def __init__(self, syntax_forest):
        self.syntax_forest = syntax_forest 
    
    def build(self, token_list):
        parent_level = 0
        stack = NodeStack()
        parent = self
        son = self._generate_node(token_list.pop(0))
        parent.add_child(son) 
        while token_list:
            token = token_list.pop(0)
            grandson = self._generate_node(token) 
            if token.level() == parent_level + 2:
                stack.push(parent)
                parent = son
                parent_level = parent_level + 1
            elif token.level() <= parent_level:
                while(token.level() <= parent_level):
                    parent = stack.pop()
                    parent_level = parent_level - 1
            parent.add_child(grandson)
    
    def _generate_node(self, token):
        node = None
        if token.has_method_call():
            node = MethodLeaf(self.syntax_forest.get_method(token.method_call()))
        elif token.has_tree_reference():
            tree = self.syntax_forest.tree(token.tree_reference())
            node = TreeReferenceLeaf(token.content, tree)
        else:
            node = ParentNode(token.content)
        return node

class SyntaxForest:
    roots = {}
    css = None
    html = None
    js = None
    plate = None

    def __init__(self, file):
        self.css = CssParser(self)
        self.html = HtmlParser(self)
        self.js = JavascriptParser(self)
        self.plate = TemplateParser(self)
        self.build(file)
    
    def build(self, file):
        dictionary = GrammarParser(file).dictionary()
        for definition in dictionary.definitions:
            self.roots[definition.tree_name] = Tree(self)
        for definition in dictionary.definitions:
            self.roots[definition.tree_name].build(definition.token_list)
  
    def get_method(self, declaration):
        meth = None
        if declaration.cls == 'css':
            meth = getattr(self.css, 'parse_' + declaration.method)
        elif declaration.cls == 'html':
            meth = getattr(self.html, 'parse_' + declaration.method)
        elif declaration.cls == 'js':
            meth = getattr(self.js, 'parse_' + declaration.method)
        elif declaration.cls == 'plate':
            meth = getattr(self.plate, 'parse_' + declaration.method)
        #meth... im so funny i love myself!!!
        return meth
            
    def traverse(self, tokens):
        self.root().traverse(tokens)

    def tree(self, tree):
        return self.roots[tree]

    def main_tree(self):
        return self.roots['']