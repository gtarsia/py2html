class LexicalRule:
    def parse(self, group, action, reader):
        raise NotImplementedError("Should have implemented this")

class Block(LexicalRule):
    def opening_tag(self, params):
        raise NotImplementedError("Should have implemented this")
    def closing_tag(self):
        raise NotImplementedError("Should have implemented this")
    def parse(self, reader, params):
        reader.writeline(self.opening_tag(params))
        reader.open_block()
        reader.parse_current_level()
        reader.close_block()
        reader.writeline(self.closing_tag)

class Statement(LexicalRule):
    def tag(self):
        raise NotImplementedError("Should have implemented this")
    def parse(self, reader, params):
        reader.writeline(self.tag(params))
