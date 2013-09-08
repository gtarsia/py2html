import re

class UnyfyStatement:
    
    def __init__(self, content):
        self.content = content
        list = re.match('(\w*)\.(\w*)\(?([^)]*)\)?', content)
        if list:
            list = list.groups()
            self.cls = list[0]
            self.method = list[1]
            self._validate_declaration(self.cls, self.method)
            self.params = list[2].split(', ')
        self._is_valid = True
    
    def _validate_declaration(self, cls, method):
        if not cls or not method:
            self.is_valid = False

    def has_definition(self):
        None
        
    def is_valid(self):
        return self.is_valid

class LineType:
    Statement, Comment, ContentOnly, Empty = range(4)


class UnyfyLine(RawLine):
    line_type = LineType.Comment
    _indent_size = 4
    statement = None
    
    def __init__(self, line):
        #print("Line read is: " + line)
        super(UnyfyLine, self).__init__(line)
        self._validate_line_type()
        
    def validate(self):
        super(UnyfyLine, self).validate()
    
    def _validate_line_type(self):
        if self.empty():
            self.line_type = LineType.Empty
        elif self.content[0] == '#':
            self.line_type = LineType.Comment
        elif self._validate_indent() and self.content[0] == '"':
            self.line_type = LineType.ContentOnly
        elif self._validate_statement():
            self.line_type = LineType.Statement
    
    def _validate_statement(self):
        statement = UnyfyStatement(self.content)
        if not statement.is_valid():
            raise SyntaxError('Wrong declaration')
        else:
            self.statement = statement
            return True
    
    def is_statement(self):
        return self.line_type == LineType.Statement
    def is_comment(self):
        return self.line_type == LineType.Comment
    def is_content_only(self):
        return self.line_type == LineType.ContentOnly
    def is_empty(self):
        return self.line_type == LineType.Empty

