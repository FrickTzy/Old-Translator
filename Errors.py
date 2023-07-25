from Stuff.NihongoTranslator.Translate_Class.Dictionary import Eng_Jap_Dict as EngDict, Fil_Jap_Dict as FilDict

LangDict = {
    "Fil": FilDict,
    "Eng": EngDict,
}


def check_all_dictionaries(word):
    for languages in LangDict:
        for types in LangDict[languages]:
            if word in LangDict[languages][types]:
                return " "
    return ''


def error(wordz, language, targeted_language):
    Languages = ["Eng", "Jap", "Fil", ""]
    if language not in Languages:
        raise UnknownLanguageError
    elif language == targeted_language:
        raise SameLanguageError
    else:
        emp = ""
        other = ""
        dictz = LangDict.get(language, "")
        for word in wordz.split():
            other += check_all_dictionaries(word)
            for Dict in dictz:
                if word in dictz[Dict]:
                    emp += " "
        if other == "":
            raise UnknownWordError
        if emp == "" and language != "":
            raise LanguageNotMatching


class UnknownLanguageError(Exception):
    def __init__(self):
        self.message = "The language is unknown"
        super().__init__(self.message)


class UnknownWordError(Exception):
    def __init__(self):
        self.message = "The input word is unknown"
        super().__init__(self.message)


class LanguageNotMatching(Exception):
    def __init__(self):
        self.message = "The input does not match the language"
        super().__init__(self.message)


class SameLanguageError(Exception):
    def __init__(self):
        self.message = "Language is the same as the targeted language"
        super().__init__(self.message)
