from translation import Translator

def main():
    file = "in.p2h"
    translator = Translator(file)
    return translator.translate()

if __name__ == "__main__":
    main()
    

