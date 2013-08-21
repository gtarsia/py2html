import re

class Css:
    reader = None 
    def __init__(self, reader):
        self.reader = reader

class CssParser:
    CssDictionary dictionary

class Define:
    def parse(self, reader, params):
        reader.open_block()
        block = reader.read_current_level()
        print("hola")
        reader.cssDictionary.define(params[0], block)

class ApplyBlock:
    block = ''
    
    def __init__(self, style, type, id):
        selector = ''
        if type == 'tag':
            selector = id
        elif type == 'class':
            selector = '.' + id
        elif type == 'id':
            selector = '#' + id
        block = selector + ' \n'
        block = block + get_definition(style)

class Apply:
    def apply(self, style, id):
    
    def parse(self, reader, params):
        param_list = self.parse_params(params)
        reader.cssDictionary.get_definition(param_list.pop(0))
        while param_list:
            selectorParser = CssSelectorParser(param_list.pop(0))
            reader.writeline("hola")
        
    def parse_params(self, params):
        [x.strip() for x in params.split(',')]

class CssDictionary:
    styles = {}
    def define(self, id, definition):
        self.styles = {id: definition}
    
    def definition_exists(self, style):
        return style in self.styles
    
    def get_definition(self, id):
        return self.styles['id']
        
class CssDefinition:
    id = ""
    definition = ''
    
class CssSelectorParser:
    selector = ''
    def __init__(self, param):
        type, identifier = re.match(r'(\w+)\=(\w+)', param).groups()
        if type == 'tag':
            selector = identifier
        elif type == 'class':
            selector = '.' + identifier
        elif type == 'id':
            selector = '#' + identifier
    def selector(self):
        return self.selector
    
    