# Genutzte Ressourcen: https://towardsdatascience.com/byte-pair-encoding-for-beginners-708d4472c0c7/


corpus = ["low", "low", "low", "low", "low",
        "lower", "lower",
        "lowest", "lowest", "lowest",
        "newer", "newer", "newer",
        "wider", "wider",
        "widest", "widest", "widest",]

# Anzahl Merges zur Ermittlung des Vokabulars
merges = 4

def init_vocabulary(corpus):
    vocabulary = {}
    for word in corpus:
        for token in word:
            vocabulary[token] = vocabulary.pop(token, 0) + 1
    vocabulary = dict(sorted(vocabulary.items()))       # Nach Schlüssel = token sortieren
    return vocabulary
            
# Zerlege Worte des Korpus in einzelne Buchstaben
def init_corpus(corpus):
    corpus_streched = []
    for word in corpus:
        word_streched = ""
        for token in word:
            word_streched = word_streched+token+" "
        word_streched = word_streched[:-1]              # Leerzeichen am Ende d. Wortes weg
        corpus_streched.append(word_streched)        
    return corpus_streched            
            
def merge_token(tokenized_corpus):
    for word in tokenized_corpus:
        # merge benachbarte token
        word_merged = ""
        new_token = ""
        i = 0
        for token in word.split():
            new_token = token
            word_merged = word_merged+new_token
            
            print(f"{i} token:{token} word_merged:{word_merged}")
            i = i+1
             
    
    
    # zähle gemergte token-kombi
    # token-kombi mit größer Anzahl = neuer token
    # aktualisiere vocabulary
    return

# main            
vocabulary = init_vocabulary(corpus)
print(f"Initial vocabulary {vocabulary}")            
tokenized_corpus = init_corpus(corpus)      
print(f"tokenized corpus {tokenized_corpus}")
merge_token(tokenized_corpus)    