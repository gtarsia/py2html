from myhtml import Html
import re

class Declaration:
    group = ""
    action = ""
    params = ""
    def __init__(self, group, action, params):
        self.group = group
        self.action = action
        self.params = params

def getClass(cls):
    return cls

def process_py2html(file):
    #html = ""
    f = open(file)
    for line in f:
        list = re.search('(\w+)\.(\w+)\(?([^)]*)\)?', line).groups()
        print(line)
        if list:
            instance_id = list.index(0) + '.' + list.index(1)
            print(instance_id)
        print(line)

def main():
    html = process_py2html("in.p2h")
    #return html

if __name__ == "__main__":
    main()