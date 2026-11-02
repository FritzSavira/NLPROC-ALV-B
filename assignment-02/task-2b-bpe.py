# Genutzte Ressourcen: https://towardsdatascience.com/byte-pair-encoding-for-beginners-708d4472c0c7/
# und https://arxiv.org/pdf/1508.07909

import collections
import re
import json

# Anzahl Iterationen
num_merges = 6
corpus_file = "assignment-02\\corpora-task-1.json"


def read_corpora(input_file):
    vocab = {}
    with open(input_file, "r", encoding="utf-8") as file:
        vocab = json.load(file)
        return vocab

# Häufigkeit benachbarter (Trenner=" ") Elemente zählen
def get_stats(vocab):
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        elements = word.split()
        for i in range(len(elements)-1): # -1, weil i noch einen Nachfolger haben muss.
            pairs[elements[i], elements[i+1]] += freq
    return pairs

# Benachbarte Elemente verschmelzen, basierend auf den Elementen im Korpus
def merge_vocab(pair, vocab_in):
    vocab_out = {}
    # Suchtext
    search_text = ' '.join(pair)
    # Ersatztext
    replace_text = ''.join(pair)
    # Sonderzeichen maskieren
    escaped_search_text = re.escape(search_text)
    # Suchmuster
    pair_pattern = re.compile(r'(?<!\S)' + escaped_search_text + r'(?!\S)')

    for word, frequency in vocab_in.items():
        new_word = pair_pattern.sub(replace_text, word)
        vocab_out[new_word] = frequency

    print(f"vocab_out {vocab_out}")     # debug print
    return vocab_out

# Beste Paarung, zuerst im Alphabet
def best_alphabetical(pairs):
    # Paar mit höchtem Wert = Anzahl
    max_count = max(pairs.values())
    if max_count == 1:
        print("ACHTUNG! Nur noch je 1 Paar vorhanden!")
    # Alle Paare mit höchstem Wert finden
    all_bests = []
    all_bests_concat = []
    for pair in pairs:
        if pairs[pair] == max_count:
            all_bests.append(pair)
            all_bests_concat.append("".join(pair))
    # Erstes Paar im Alphabet finden
    best_index = all_bests_concat.index(min(all_bests_concat))
    best = all_bests[best_index]
    print(f"max_count: {max_count} all_bests: {all_bests} best: {best}") # debug print
    return best, all_bests

# Token-Liste
def current_token_list(vocab):
    vocab_list = list(vocab)
    current_list = []
    for word in vocab_list:
        tokens = word.split()
        for token in tokens:
            if token not in current_list:
                current_list.append(token)
    return current_list

def learn_bpe(vocab, num_merges):
    for i in range(num_merges):
        print()         # debug print
        print("i:", i)  # debug print
        # Häufigkeit benachbarter, durch " " getrennte Elemente, zählen
        pairs = get_stats(vocab)         
        # Häufigste Paarung (alphabetisch) in best ablegen
        best, all_bests = best_alphabetical(pairs) 
        # Häufigsten Elemente verschmelzen, gibt das Ergebnis als neuen Korpus zurück
        vocab = merge_vocab(best, vocab) 
        token_list = current_token_list(vocab)
        print(f"token_list {token_list}")
    return vocab, token_list

# Hauptroutine
print(f"num_merges: {num_merges}")            # debug print
vocab = read_corpora(corpus_file)
print(f"corpus: {vocab}")
vocab, final_token_list = learn_bpe(vocab, num_merges)
print()                                       # debug print
print(f"final_token_list {final_token_list}") # debug print   
   



