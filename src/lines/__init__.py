import re

class UnyfyStatement:
    cls, method, params = "", "", ""
    _is_valid = True
    
    def __init__(self, content):
        self.content = content
        list = re.match('(\w*)\.(\w*)\(?([^)]*)\)?', content)
        if list:
            list = list.groups()
            self.cls = list[0]
            self.method = list[1]
            self._validate_declaration(self.cls, self.method)
            self.params = list[2].split(', ')
    
    def _validate_declaration(self, cls, method):
        if not cls or not method:
            self.is_valid = False

    def has_definition(self):
        None
        
    def is_valid(self):
        return self.is_valid
    
class UnyfyDefinition():
    statement, block = None, []
    
    def __init__(self, statement, block):
        self.statement = statement
        self.block = block
        
class RawLine(object):
    indent, content = None, ""
    def __init__(self, line):
        indent_string, self.content = re.match(r'(\s*)(.*)', line).groups()
        self.indent = Indent(indent_string, 4)

    def level(self):
        return self.indent.level()
        
    def validate(self):
        self.indent.validate()
        
    def is_block(self):
        return self.content[-1:] == ':'
    
    def empty(self):
        return not self.content

class GrammarToken(RawLine):
    def __init__(self, line):
        super(GrammarToken, self).__init__(line)
        self.indent.indent_size = 2
        
    def has_method_call(self):
        return '>' in self.content

    def has_tree_reference(self):
        return '!' in self.content
    
    def tree_reference(self):
        if not '!' in self.content:
            raise BaseException("Don't create this node if the token doesnt reference a tree")
        else:
            return self.content.split('!', 1)[1]
        
    def method_call(self):
        return UnyfyStatement(self.content.split('>', 1)[1])

    def pattern(self):
        return re.split('!|>', self.content)[0]
    
class Indent:
    indent = ""
    indent_size = 4
    
    def __init__(self, indent, indent_size):
        self.indent = indent
    
    def level(self):
        return self.indent.__len__()/self.indent_size
        
    def is_valid(self):
        return not (self.indent.__len__()/self.indent_size) % 1
    
class LineType:
    Declaration, Comment, ContentOnly, Empty = range(4)


class UnyfyLine(RawLine):
    line_type = LineType.Comment
    _indent_size = None
    statement = None
    
    def __init__(self, line):
        print("Line read is: " + line)
        super(RawLine, UnyfyLine).__init__(line)
        self._validate_line_type()
        
    def validate(self):
        super(UnyfyLine, self).validate()
    
    def _validate_line_type(self):
        if not self.content:
            self.line_type = LineType.Empty
        elif self.content[0] == '#':
            self.line_type = LineType.Comment
        elif self._validate_indent() and self.content[0] == '"':
            self.line_type = LineType.ContentOnly
        elif self._validate_declaration():
            self.line_type = LineType.Declaration
    
    def _validate_statement(self, raw_line):
        statement = UnyfyStatement(raw_line.content)
        if not statement.is_valid():
            raise SyntaxError('Wrong declaration')
        else:
            self.statement = statement
            return True
    
    def is_statement(self):
        return self.line_type == LineType.Declaration
    def is_comment(self):
        return self.line_type == LineType.Comment
    def is_content_only(self):
        return self.line_type == LineType.ContentOnly
    def is_empty(self):
        return self.line_type == LineType.Empty

