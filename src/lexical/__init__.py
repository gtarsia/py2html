
class Block:
    def open_block(self, params):
        raise NotImplementedError("Should have implemented this")
    def close_block(self, params):
        raise NotImplementedError("Should have implemented this")
    def isBlock(self):
        return True

class Statement:
    def state(self, params):
        raise NotImplementedError("Should have implemented this")
    def isBlock(self):
        return False