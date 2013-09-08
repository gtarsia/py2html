'''
Created on 25/08/2013

@author: guidi
'''
import re

class UnyfyReader(Reader):
    last_line = None
    def __iter__(self):
        return self
    
    def next(self):
        return self.__next__()
    
    def __next__(self):
        if self.eof():
            raise StopIteration
        else:
            return UnyfyLine(self.read_line())
    
    def _is_block(self, line):
        return line.rstrip()[-1:]
