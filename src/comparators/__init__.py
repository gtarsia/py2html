import re

class StringComparator:
    
    def __init__(self, string):
        self.string = string
        
    def match(self, string):
        return self.string == string

    def has_capture_list(self):
        return False

class RegexComparator:
    
    def __init__(self, pattern):
        self.pattern = pattern
        self._capture_list = []
        self._match = None

    def match(self, string):
        if not self._match:
            self._capture_list = re.match(self.pattern, string)
            self._match = bool(self._capture_list)
        return self._match
    
    def capture_list(self):
        return self._capture_list
    
    def has_capture_list(self):
        return True