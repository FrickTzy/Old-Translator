from Stuff.NihongoTranslator.Translate_Class.Jap import jap_translate
from Stuff.NihongoTranslator.Translate_Class.Fil import fil_translate
from Stuff.NihongoTranslator.Translate_Class.Errors import error


class Translate:
    @staticmethod
    def jap(word, language: str = ""):
        error(word.lower(), language.title(), "Jap")
        return jap_translate(word, language.title())

    @staticmethod
    def fil(word, language: str = ""):
        error(word.lower(), language.title(), "Fil")
        return fil_translate(word, language.title())


if __name__ == "__main__":
    print(Translate.jap("i ate two yellow apples"))
