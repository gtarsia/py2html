import re
from lines import RawLine, GrammarToken
from reader import Reader

class GrammarReader(Reader):

    def read_token(self):
        line = super(GrammarReader, self).read_line()
        return GrammarToken(line)
    
    def push_token(self, token):
        super(GrammarReader, self).push_line(token.content)
        
class GrammarTreeDefinition:
    tree_name = ""
    token_list = []
    def __init__(self, tree_name, token_list):
        self.tree_name = tree_name
        self.token_list = token_list

class GrammarTreeDictionary:
    definitions = []
    
    def add_definition(self, tree_name, token_list):
        self.definitions.append(GrammarTreeDefinition(tree_name, token_list))

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

