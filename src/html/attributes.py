'''
Created on 21/08/2013

@author: open0130
'''
import re

class GlobalAttributeList:
    attributes = []
    def __init__(self):
        self.attributes.append("id")
        self.attributes.append("style")
    def has_attribute(self, attribute):
        return attribute in self.attributes
        
class AttributeParser:
    output = []
    def __init__(self, params, attributeList):
        paramAttributes = re.findall(r'(\w+\),\S+', params)
        for attribute in paramAttributes:
            if attribute in attributeList:
                self.output.append(attribute[0]) 
            else:
                print("tag does not have that " + attribute + " attribute")
            #Buscar en attributeList cada paramAttributes
            
    