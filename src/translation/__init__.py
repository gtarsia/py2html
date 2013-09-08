from grammar import GrammarForest, GrammarTranslator
from common import Reader, Writer, global_reader, global_writer

class Translator:
    def __init__(self, file):
        global_reader = Reader(file)
        global_writer = Writer()
        
    def translate(self):
        self.grammar_forest = GrammarForest()
        self.grammar_translator = GrammarTranslator(self.grammar_forest)
        for line in global_reader:
            if line.level() != 0:
                raise SyntaxError('This line should be of level 0')
            translation = self.grammar_translator.translate(line)
            global_writer.write