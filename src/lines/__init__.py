import re

class RawLine(object):
    indent, content = None, ""
    def __init__(self, line):
        indent_string, self.content = re.match(r'(\s*)(.*)', line).groups()
        self.indent = Indent(indent_string, 4)

    def indent_level(self):
        self.indent.level()
        
    def validate(self):
        self.indent.validate()
         
class GrammarLine(RawLine):
    
    def __init__(self, line):
        super(GrammarLine, self).__init__(line)
        self.indent.indent_size = 2
        
    def has_method_call(self):
        return '>' == self.content[0]

    def has_tree_reference(self):
        return '!' == self.content[0]
            
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
    declaration = None
    
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
    
    def _validate_declaration(self, raw_line):
        declaration = Declaration(raw_line.content)
        if not declaration.is_valid():
            raise SyntaxError('Wrong declaration')
        else:
            self.declaration = declaration
            return True
    
    def is_declaration(self):
        return self.line_type == LineType.Declaration
    def is_comment(self):
        return self.line_type == LineType.Comment
    def is_content_only(self):
        return self.line_type == LineType.ContentOnly
    def is_empty(self):
        return self.line_type == LineType.Empty

class Declaration:
    cls = ""
    method = ""
    param_list = []
    _is_valid = True
    def __init__(self, content):
        self.content = content
        list = re.match('(\w*)\.(\w*)\(?([^)]*)\)?', content)
        if list:
            list = list.groups()
            self.cls = list[0]
            self.method = list[1]
            self._validate_declaration(self.cls, self.method)
            param_list = list[2].split(', ')
    
    def _validate_declaration(self, cls, method):
        if not cls or not method:
            self.is_valid = False

    def is_valid(self):
        return self.is_valid
