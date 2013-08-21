from lexical import Statement

class Load(Statement):
    def state(self, params):
        return ""
'''class Inherit(Statement):
    def state(self, params):
        return "Inherited"
#        
class Override(Block):
    def open_block(self, params):
        Block.open_block(self, params)
    def close_block(self, params):
        Block.close_block(self, params)

class Symbol(): 
    content = ""
    def __init__(self, content):
        self.content = content

#class Tree():
#class TreeNode():
#    content = ""
#    sons 

#def process_templates(lines):
 #   for line in lines:
'''