Eng_Jap_Dict = {
    'noun': {
        "i": "ore",
        "you": "kimi",
    },

    'verb': {
        "eat": "taberu",
        "ate": "tabeta",
        "ran": "hashitta",
        "drank": "nonda",
        "met": "atta",
        "meet": "airu",
        "open": "akeru",
        "opened": "aketa",
        "played": "asonda",
        "washed": "aratta",
        "insert": "ireru",
        "inserted": "ireta"

    },

    'feelings': {
        "love": "daisuki",
        "hate": "daikirai",
    },

    'food': {
        "apple": "ringo",
        "water": "mizu",
        "breakfast": "asa gohan",
    },

    'numbering': {
        "one": "hitotsu",
        "two": "futatsu",
        "three": "mittsu",
    },

    'thing': {
        "pencil": "enpitsu",
        "box": "hako",
        "smartphone": "sumaho",
        "phone": "denwa",
        "rainbow": "niji",
        "glasses": "megane",
        "bag": "kaban",
        "stair": "kaidan",
        "pillow": "makura",
    },

    'greeting': {
        "hi": "konnichiwa",
        "hello": "konnichiwa"
    },

    'color': {
        "red": "akai",
        "yellow": "kiiroi",
        "blue": "aoi",
        "pink": "pinku",
        "orange": "orenji",
        "green": "midori",
        "brown": "chairoi",
        "black": "kuroi",
        "white": "shiroi",
        "color": "iro"
    },

    'adjective': {
        "bright": "akarui",
        "new": "atarashii",
        "warm": "atatakai",
        "hot": "atsui",
        "cool": "suzushii",
        "cold": "samui",
        "thick": "atsui",
        "various": "iroiro"
    },

    'season': {
        "fall": "aki",
        "autumn": "aki",
        "summer": "natsu",
    },

    'time': {
        "morning": "asa",
        "tommorow": "ashita",
    },

    'body': {
        "leg": "ashi",
        "foot": "ashi",
        "head": "atama",
        "face": "kao",
        "back": "senaka",
        "stomach": "onaka",
    },

}

Fil_Jap_Dict = {
    'noun': {
        "ako": "ore",
        "ako'y": "ore",
        "'ko": "ore",
        "ikaw": "kimi",
        "kita": "kimi"
    },

    'verb': {
        "kumain": "tabeta",
        "uminom": "nonda",
        "kain": "taberu"
    },

    'feelings': {
        "mahal": "daisuki",
        "ayaw": "daikirai"
    },

    'food': {
        "mansanas": "ringo",
        "tubig": "mizu",
    },

    'numbering': {
        "isang": "hitotsu",
        "dalawang": "futatsu",
        "tatlong": "mittsu",
    },

    'thing': {
        "lapis": "enpitsu",
        "kahon": "hako",
        "selpon": "sumaho",
        "telepono": "denwa",
        "salamin": "megane"
    },

    'greeting': {
        "kamusta": "konnichiwa",
    },

    'color': {
        "dilaw": "kiiroi"
    },

    'adjective': {
        "mabigat": "omoi"
    },

    'season': {
        "maulan": "ame"
    },

    'time': {
        "umaga": "asa"
    },

    'body': {
        "kamay": "te"
    },
}

Jap_Fil_Dict = {}
for (key, value) in Fil_Jap_Dict.items():
    temp_dict = {value2: key1 for (key1, value2) in value.items()}
    Jap_Fil_Dict[key] = temp_dict

Eng_Fil_Dict = {
    'noun': {
        "i": "ako",
        "you": "ikaw",
    },

    'verb': {
        "eat": "kumain",
        "ate": "kumain",
        "ran": "tumakbo",
        "drank": "iminom"
    },

    'feelings': {
        "love": "mahal",
        "hate": "galit",
    },

    'food': {
        "apple": "mansanas",
        "water": "tubig",
    },

    'numbering': {
        "one": "isang",
        "two": "dalawang",
        "three": "tatlong",
    },

    'thing': {
        "pencil": "lapis",
        "box": "kahon",
        "smartphone": "selpon",
        "phone": "selpon",
        "rainbow": "bahaghari",
        "glasses": "salamin",
        "bag": "bag",
    },

    'greeting': {
        "hi": "kamusta",
    },

    'color': {
        "yellow": "dilaw",
    },

    'adjective': {
        "heavy": "mabigat",
    },

    'season': {
        "rainy": "maulan",
    },

    'time': {
        "morning": "umaga",
    },

    'body': {
        "hands": "kamay",
    },

}
