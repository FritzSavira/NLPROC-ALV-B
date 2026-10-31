# Task 2a - Rule-based stemming

# define rules for English:
# remove suffixes:
# ing    playing -> play
# ed     played -> play
# ly     quickly -> quick
# es     moxes -> box
# s      cats -> cat
# remove prefixes:
# un    unhappy -> happy
# dis   disagree -> agree
# mis   misunderstand -> understand (stemmimng only applied once for prefix)

#define rules for German:
# remove suffixes:
# en    zahlen -> zahl
# keit  Heiterkeit -> Heiter
# e     Hunde -> e
# st    kannst -> kann
# s     Autos -> Auto
#remove prefixes:
# un    unglücklich -> glücklich (lich could also be removed with a rule)
# ver   verkaufen -> kaufen
# ge    gesagt -> sagt

# test words English:
# playing (trus), played (true), cats (true), boxes (true), byes (false), dogs(true), 
# his (false), walking(true), studies (true), sing(false), news(false), 
# misunderstand (true), disagree (true), disturb (false), mister (false)
# unhappy (true), until (false)

# test words German:
# unglücklich (true), verkaufen (true), gesagt (true), zahlen (true), Hunde (true),
# Heiterkeit (true), Autos (true), kannst (true), unklar (true), Gesicht (false),
# gestern (false), Ungeheuer (un), Universität (false), Keks (false), "Fenster",
# Verb (false), verbinden(true), Ast (false), Keule (false), verkaufst (true)


# Define stemming rules
# from long to short
prefixes_english = ["dis", "mis", "un"]
suffixes_english = ["ing", "ed", "es", "ly", "s"]

prefixes_german = ["ver", "ge", "un", ]
suffixes_german = ["keit", "en", "st", "e", "s"]

def stem(word, language):
    """cuts prefixes ond suffixes depending on language"""
    if language == "english":
        prefixes = prefixes_english
        suffixes = suffixes_english
    elif language == "german":
        prefixes = prefixes_german
        suffixes = suffixes_german
    else:          # other language s could be added later
        return word

    # remove prefix
    for prefix in prefixes:
        if word.startswith(prefix):
            word = word[len(prefix):]
            break # only one rule applyed per word

    # Remove suffixes
    for suffix in suffixes:
        if word.endswith(suffix):
            word = word[:-len(suffix)]
            break

    return word

#test English
words_english = ["playing", "played", "walking", "sing", "quickly", "cats", "dogs", "his",
         "news", "boxes", "byes", "studies", "misunderstand", "disagree", "disturb",
         "mister", "unhappy", "until"]

words_german = [
    "unglücklich", "verkaufen", "gesagt", "zahlen", "Hunde", "Heiterkeit", "Autos",
    "kannst", "unklar",  "Gesicht", "gestern", "Ungeheuer", "Universität", "Keks",
    "Fenster", "Verb", "verbinden", "Ast", "Keule", "verkaufst"
]

# Apply English rules
print("English stemming:")
for word in words_english:
    print(word, "->", stem(word, "english"))

# Apply German rules
print("\nGerman stemming:")
for word in words_german:
    print(word, "->", stem(word, "german"))


# Second part
print("\nApply on sentences")
# test sentences
sentences_english = ["The children are playing with their dogs.", 
                     "She quickly opened the boxes.",
                     "The unhappy student disagreed with the teacher.",
                     "They are walking and singing in the garden.",
                     "He misunderstood the question and replayed the video."]

sentences_german = ["Die Kinder spielen mit ihren Hunden.",
                    "Der unglückliche Schüler verkauft seine Bücher.",
                    "Sie bezahlten gestern die Einkäufe.",
                    "Die Verkäufer arbeiten meistens sehr schnell.",
                    "Das Geschenk wurde gestern ausgepackt und geöffnet."]

# Apply English stemming
print("English sentences:")
for sentence in sentences_english:
    words = sentence.split()
    stemmed_words = [stem(word.lower().strip(".,!?"), "english")
                     for word in words]
    print(sentence)
    print(stemmed_words)


# Apply German stemming
print("\nGerman sentences:")
for sentence in sentences_german:
    words = sentence.split()
    stemmed_words = [stem(word.lower().strip(".,!?"), "german")
                     for word in words]
    print(sentence)
    print(stemmed_words)