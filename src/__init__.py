from translation import Translator

class UnyfyTranslator:
    def __init__(self):
        self.level = 0
    
    def translate(self, file):
        translator = Translator(file)
        return translator.translate()
            
def main():
    file = "in.p2h"
    return UnyfyTranslator().translate(file)

if __name__ == "__main__":
    main()