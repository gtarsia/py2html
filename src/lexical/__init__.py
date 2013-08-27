import re
from lines.reader import GrammarReader
from lines import RawLine, MethodCall, GrammarToken


class GrammarTreeDefinition:
    tree_name = ""
    token_list = []
    def __init__(self, id, token_list):
        self.id = id
        self.token_list = token_list

class GrammarTreeDictionary:
    definitions = []
    
    def add_definition(self, tree_name, token_list):
        self.definitions.append(GrammarTreeDefinition(tree_name, token_list))

class NodeStack:
    nodes = []
    
    def push(self, node):
        self.nodes.append(node)
        
    def pop(self):
        return self.nodes.pop()

class GrammarParser():
    tree_dictionary = GrammarTreeDictionary()
    
    def __init__(self, file):
        reader = GrammarReader(file)
        self._parse_definitions(reader)
    
    def dictionary(self):
        return self.tree_dictionary

    def _parse_definitions(self, reader):
        while not reader.eof():
            token = reader.read_token()
            if token.level() > 0:
                raise SyntaxError('Grammar tree has wrong level')
            else:
                tree = token.content
                token_list = self._parse_tree_definiens(reader)
                self.tree_dictionary.add_definition(tree, token_list)
                
    def _parse_tree_definiens(self, reader):
        token_list = []
        while not reader.eof():
            token = reader.read_token()
            if token.level() > 0:
                token_list.append(token)
            else:
                reader.push_token(token)
                break
        return token_list   

    def _read_line(self):
        return (GrammarToken(self.reader.read_line()))

class TreeNode:
    comparator = None
    
    def __init__(self, id):
        if '$' in id:
            id.pop(0)
            self.comparator = RegexComparator(id)
        else:
            self.comparator = StringComparator(id)
    
    def match(self, str):
        return self.comparator.compare(str)
    
    def traverse(self, tokens):
        raise NotImplementedError()

class ParentNode(TreeNode):
    children = {}
    
    def add_child(self, node):
        self.children[node.id] = node
                
class MethodLeaf(TreeNode):
    cls, method = "", ""
    
    def __init__(self, cls, method):
        self.cls = cls
        self.method = method
    
    def traverse(self, tokens):
        self.run_method(tokens)
    
    def run_method(self, params):
        None#Call method
    
class TreeReferenceLeaf(TreeNode):
    tree = None
    
    def traverse(self, ):
        None
        
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
        level = 1
        parent = self.syntax_forest
        node_stack = NodeStack()
        while token_list:
            token = token_list.pop(0)
            node = self._generate_node(token)
            if token.level() > level:
                node_stack.push(parent)
                parent = node
                level = level + 1
            elif token.level() < level:
                node = parent
                parent = node_stack.pop()
                level = level - 1
            else:
                parent.add_child(node)
    
    def _generate_node(self, token):
        node = None
        if token.has_method_call():
            node = MethodLeaf(token.method_call())
        elif token.has_tree_reference():
            node = TreeReferenceLeaf(self.forest.tree(token.tree_name()))
        else:
            node = ParentNode(token.content)
        return node

class SyntaxForest:
    roots = {}
    
    def __init__(self, file):
        self.build(file)

    def build(self, file):
        dictionary = GrammarParser(file).dictionary()
        for definition in dictionary.definitions:
            self.roots[id] = Tree(self)
        for definition in dictionary.definitions:
            self.roots[id].build(definition.token_list)
  
    def traverse(self, tokens):
        self.root().traverse(tokens)

    def tree(self, tree):
        return self.roots[tree]
    
