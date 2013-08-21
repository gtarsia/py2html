import re

class CssDictionary:
    styles = {}
    def define(self, id, definition):
        self.styles = {id: definition}
    
    def definition_exists(self, style):
        return style in self.styles
    
    def get_definition(self, id):
        return self.styles['id']

class CssStyleBlockGenerator:
    dictionary = CssDictionary()
    def block(self, style, selector):
        styleDef = self.dictionary.get_definition(style)
        return CssStyleBlock(styleDef).block()
    
class CssParser:
    styleGenerator = CssStyleBlockGenerator()
    
    def parse_define(self, reader, params):
        reader.open_block()
        block = reader.read_current_level()
        reader.cssDictionary.define(params[0], block)
        
    def parse_apply(self, reader, params):
        apply_params = CssApplyStyleParams(params) 
        reader.writeline(styleGenerator(apply_params.style, apply_params.selectors))
        
    def split(self, params):
        return [x.strip() for x in params.split(',')]


class CssStyleBlock:
    styleDef = ""
    selector = ""
    def __init__(self, styleDef, selector):
        self.styleDef = styleDef
        self.selector = selector
    def opening(self):
        return self.selector + '{'
    
    def closing(self):
        return '}'
    
    def block(self):
        block = self.opening() + "\n"
        block = block + self.styleDef + "\n"
        block = block + self.closing() + "\n"
        return block

class CssSelector:
    selector = ""
    def __init__(self, type, id):
        if type == 'tag':
            selector = id
        elif type == 'class':
            selector = '.' + id
        elif type == 'id':
            selector = '#' + id

class CssApplyStyleParams:
    style = ""
    selectors = ""
    def __init__(self, params):
        list = [x.strip() for x in params.split(',')]
        self.style = list.pop(0)
        self.selectors = list
        
