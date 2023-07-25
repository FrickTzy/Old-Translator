class Language:
    def __init__(self):
        self.noun, self.noun2, self.verb, self.feelings, self.food = "", "", "", "", ""
        self.numbering, self.thing, self.greeting, self.color = "", "", "", ""
        self.body, self.time, self.season, self.adjective = "", "", "", ""
        self.final = ""

    def add_noun(self, word):
        if self.noun != "":
            self.noun2 += word.title()
        else:
            self.noun += word.title()

    def add_verb(self, word):
        self.verb += word.title()

    def add_feelings(self, word):
        self.feelings += word.title()

    def add_food(self, word):
        self.food += word.title()

    def add_thing(self, word):
        self.thing += word.title()

    def add_numbering(self, word):
        self.numbering += word.title()

    def add_greeting(self, word):
        self.greeting += word.title()

    def add_body(self, word):
        self.body += word.title()

    def add_time(self, word):
        self.time += word.title()

    def add_season(self, word):
        self.season += word.title()

    def add_adjective(self, word):
        self.adjective += word.title()

    def add_color(self, word):
        self.color += word.title()

    def dict_var(self, typez, word):
        var_dict: dict = {
            "noun": self.add_noun,
            "verb": self.add_verb,
            "feelings": self.add_feelings,
            "food": self.add_food,
            "numbering": self.add_numbering,
            "thing": self.add_thing,
            "greeting": self.add_greeting,
            "body": self.add_body,
            "time": self.add_time,
            "season": self.add_season,
            "adjective": self.add_adjective,
            "color": self.add_color,
        }
        var_dict.get(typez, "")(word)
        self.add_filler()

    def add_filler(self):
        pass
