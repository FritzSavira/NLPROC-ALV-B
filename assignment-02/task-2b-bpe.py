# Genutzte Ressourcen: https://towardsdatascience.com/byte-pair-encoding-for-beginners-708d4472c0c7/
# und https://arxiv.org/pdf/1508.07909

import collections
import re

# Korpus
vocab = {'l o w </w>' : 5,
         'l o w e r </w>' : 2,
         'l o w e s t </w>' : 3,
         'n e w e r </w>' : 3,
         'w i d e r </w>' : 2,
         'w i d e s t </w>' : 3}

# Anzahl Iterationen
num_merges = 10

print("***")                                     # debug print
print(f"num_merges: {num_merges}")                    # debug print

# Zählt Häufigkeit benachbarter (Trenner=" ") Elemente
def get_stats(vocab):
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        elements = word.split()
        for i in range(len(elements)-1): # -1, weil i noch einen Nachfolger haben muss.
            pairs[elements[i], elements[i+1]] += freq
    print(f"pairs: {dict(pairs)}")        # debug print
    return pairs

# Benachbarte Elemente verschmelzen, basierend auf den Elementen im Korpus
def merge_vocab(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    print(f"v_out {v_out}")     # debug print
    return v_out

# Beste Paarung, zuerst im Alphabet
def best_alphabetical(pairs):
    # Paar mit höchtem Wert = Anzahl
    max_count = max(pairs.values())
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
    print(f"all_bests: {all_bests} best: {best}") # debug print
    return best, all_bests

# Finale Token-Liste
def token_list(vocab):
    vocab_list = list(vocab)
    token_list = []
    for word in vocab_list:
        tokens = word.split()
        for token in tokens:
            if token not in token_list:
                token_list.append(token)
    return token_list

def learn_bpe(vocab, num_merges):
    for i in range(num_merges):
        print()         # debug print
        print("i:", i)  # debug print
        # Zählt Häufigkeit benachbarter, durch " " getrennte Elemente
        pairs = get_stats(vocab)         
        # Legt die häufigste Paarung (alphabetisch) in best ab
        best, all_bests = best_alphabetical(pairs) 
        # Verschmilzt die beiden häufigsten Elemente, gibt das Ergebnis als neuen Korpus zurück
        vocab = merge_vocab(best, vocab) 
    final_token_list = token_list(vocab)
    print(f"final_token_list {final_token_list}") # debug print   
    return final_token_list




# Hauptroutine
print("Initialer Korpus")           # debug print
for word, freq in vocab.items():
    word_list = word.split()
    print(word_list, freq) # debug print

#for i in range(num_merges): 
#    pairs = get_stats(vocab)         # Zählt Häufigkeit benachbarter, durch " " getrennte Elemente 
#    best, all_bests = best_alphabetical(pairs) # Legt die häufigste Paarung (alphabetisch) in best ab
#    vocab = merge_vocab(best, vocab) # Verschmilzt die beiden häufigsten Elemente, gibt das Ergebnis als neuen Korpus zurück
final_token_list = learn_bpe(vocab, num_merges)
   



