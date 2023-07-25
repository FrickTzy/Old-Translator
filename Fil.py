from Stuff.NihongoTranslator.Translate_Class.Dictionary import Jap_Fil_Dict as JapDict, Eng_Fil_Dict as EngDict
from Stuff.NihongoTranslator.Translate_Class.LanguageClass import Language

Lang_dict = {
    "Eng": EngDict,
    "Jap": JapDict
}


class VarAdd(Language):
    def __init__(self):
        super().__init__()
        self.filler_ng = ""

    def add_filler(self):
        if self.verb != "" and self.food != "":
            self.filler_ng = "ng "
        if self.feelings != "" and self.noun != "":
            if self.noun == "Ako":
                self.noun = "'ko"

    def adding(self):
        self.final += (self.season + self.time + self.feelings + self.greeting +
                       self.verb + self.noun + self.noun2 + self.filler_ng +
                       self.adjective + self.numbering + self.color + self.food +
                       self.thing + self.body)
        return self.final


def remove_filler_s(word: str, types):
    remove_s = word.removesuffix("s")
    remove_es = word.removesuffix("es")
    remove_list = [remove_s, remove_es]
    for word_remove in remove_list:
        if word_remove in EngDict[types] or word_remove in JapDict[types]:
            return word_remove
    return False


def translate_without_lang(word, var_add):
    for lang in Lang_dict:
        for types in (dictionary := Lang_dict[lang]):
            if s_remove := remove_filler_s(word, types):
                word = s_remove
            if word in Lang_dict[lang][types]:
                class_add(var_add, dictionary, word, types)


def translate_with_lang(word, var_add, lang_dict):
    for types in lang_dict:
        if word in lang_dict[types]:
            class_add(var_add, lang_dict, word, types)


def class_add(var_add, dictionary: dict, word, types):
    temp_word = dictionary[types].get(word, '')
    temp_word += ' '
    var_add.dict_var(types, temp_word)


def fil_translate(sentences, language=""):
    lang_dict: dict = Lang_dict.get(language, "")
    sentences = sentences.lower()
    var_add = VarAdd()
    for word in sentences.split():
        if lang_dict == "":
            translate_without_lang(word, var_add)
        else:
            translate_with_lang(word, var_add, lang_dict)

    return var_add.adding()
