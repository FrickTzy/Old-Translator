from Stuff.NihongoTranslator.Translate_Class.HiraganaConverter import HiraganaConverterz
from Stuff.NihongoTranslator.Translate_Class.Dictionary import Eng_Jap_Dict as EngDict, Fil_Jap_Dict as FilDict
from Stuff.NihongoTranslator.Translate_Class.LanguageClass import Language

Lang_dict = {
    "Eng": EngDict,
    "Fil": FilDict,
}


class VarAdd(Language):
    def __init__(self):
        super().__init__()
        self.filler_wa, self.filler_ga, self.filler_wo, self.filler_no = "", "", "", ""

    def add_filler(self):
        if self.noun != "" and self.feelings != "":
            self.filler_ga = "ga "
        if self.noun != "" and self.verb != "":
            self.filler_wo = "o "
        if self.noun != "" and (self.food != "" or self.thing != "" or self.numbering != ""):
            self.filler_wa = "wa "
        if self.numbering != "" and (self.food != "" or self.thing != ""):
            self.filler_no = "no "

    def adding(self):
        self.final += (self.season + self.time + self.greeting + self.noun +
                       self.filler_wa + self.noun2 + self.adjective + self.numbering +
                       self.filler_no + self.color + self.food + self.thing +
                       self.body + self.filler_wo + self.verb + self.filler_ga +
                       self.feelings)
        self.final += ("\n" + HiraganaConverterz(self.final.lower()))
        return self.final


def remove_filler_s(word: str, types):
    remove_s = word.removesuffix("s")
    remove_es = word.removesuffix("es")
    remove_list = [remove_s, remove_es]
    for word_remove in remove_list:
        if word_remove in EngDict[types] or word_remove in FilDict[types]:
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


def jap_translate(sentences, language=""):
    lang_dict: dict = Lang_dict.get(language, "")
    sentences = sentences.lower()
    var_add = VarAdd()
    for word in sentences.split():
        if lang_dict == "":
            translate_without_lang(word, var_add)
        else:
            translate_with_lang(word, var_add, lang_dict)

    return var_add.adding()
