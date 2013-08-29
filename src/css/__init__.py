import re

class CssDictionary:
    styles = {}
    def define(self, id, definition):
        self.styles[id] = definition
        #print("WE HAVE DEFINED: '" + id + "' as: \n" + definition + "\n Glory to Rome!!!!!")
    
    def definition_exists(self, style):
        return style in self.styles
    
    def get_definition(self, id):
        return self.styles[id]

class CssParser:
    dictionary = CssDictionary()
    reader = None
    writer = None
    mainParser = None
    
    def __init__(self, mainParser):
        None
        #self.writer = mainParser.writer
        #self.mainParser = mainParser
    
    def parse_define(self, param_list):
        None
        '''self.mainParser.open_block()
        block_list = self.mainParser.read_current_level()
        self.mainParser.close_block()
        block = "\n".join(line for line in block_list)
        self.dictionary.define(param_list[0], block)'''

    def parse_apply(self, params):
        None
        '''apply_params = CssApplyStyleParams(params)
        styleDef = self.dictionary.get_definition(apply_params.style)
        selectors = apply_params.selectors
        while selectors:
            self.writer.writeline(CssStyleBlock(styleDef, selectors.pop(0)).block())'''

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
    selectors = []
    def __init__(self, param_list):
        self.style = param_list.pop(0)
        while param_list:
            type, id = re.match(r'(\w+)\=(\w+)', param_list.pop(0)).groups()
            self.selectors.append(CssSelector(type, id).selector)
        
