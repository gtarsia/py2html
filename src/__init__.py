import re

def get_declaration(line):

def get_instance_of(cls):
    parts = cls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)            
    return m

class Reader:
    level = 0
    file = None
    lines = []
    output = []
    def __init__(self, file):
        self.f = open(file)
        self.level = 0
        
    def readline(self):
        return self.lines.pop(0)
        
    def writeline(self, line):
        self.output.append(line)
        
    def eof(self):
        return self.lines.count() > 0
    
    def open_block(self, params):
        self.level = self.level + 1
        
    def close_block(self, params):
        self.level = self.level - 1
        if self.level < 0:
            raise IndexError("Level tried to go below 0")
    
    def parse_nextline(self):
        line = self.readline()
        declaration = parse_declaration()
        run_declaration(declaration, self)
            
    def parse_current_level(self):
        current_level = self.level()
        while not self.eof() and current_level == self.level:
            self.parse_nextline()
            
    def parse(self):
        while not self.eof():
            self.parse_nextline()

def run_declaration(declaration, reader):
    instance = get_instance_of(declaration.group + '.' + declaration.action)
    instance.parse(reader, declaration.params)

def parse_declaration(line):
    declaration = Declaration
    list = re.search('(\w+)\.(\w+)\(?([^)]*)\)?', line).groups()
    declaration.group = list[0]
    declaration.action = list[1]
    declaration.params = list[2]
    return 
    
class Parser:
    def process_py2html(self, file):
        reader = Reader(file)
        reader.parse
        return reader.output
                        

class Declaration:
    group = ""
    element = ""
    params = ""
    def __init__(self, list):
        self.group = list[0]
        self.element = list[1]
        self.params = list[2]

def load_template(file):
    f = open(file)
    for line in f:
        re.findall('load.define()', line)
        #define
        #redefine
        #



            
def main():
    parser = Parser
    html = parser.process_py2html("in.p2h")
    return html

if __name__ == "__main__":
    main()