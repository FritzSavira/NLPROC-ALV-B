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
num_merges = 18

# Zählt Häufigkeit benachbarter (Trenner=" ") Elemente
def get_stats(vocab):
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        elements = word.split()
        for i in range(len(elements)-1): # -1, weil i noch einen Nachfolger haben muss.
            pairs[elements[i], elements[i+1]] += freq
    return pairs

# Benachbarte Elemente verschmelzen, basierend auf den Elementen im Korpus
def merge_vocab(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out

# Beste Paarung, zuerst im Alphabet
def best_aphabetical(pairs):
    # Paar mit höchtem Wert = Anzahl
    max_count = max(pairs.values())
    # Alle Paare mit höchstem Wert finden
    all_bests = []
    for pair in pairs:
        if pairs[pair] == max_count:
            all_bests.append(pair)
    # Erstes Paar im Alphabet finden
    best = min(all_bests)
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

# Hauptroutine
#print("Initialer Korpus")
for word, freq in vocab.items():
    word_list = word.split()
    # print(word_list, freq)

for i in range(num_merges): 
    pairs = get_stats(vocab)         # Zählt Häufigkeit benachbarter, durch " " getrennte Elemente 
    best, all_bests = best_aphabetical(pairs) # Legt die häufigste Paarung (alphabetisch) in best ab
    vocab = merge_vocab(best, vocab) # Verschmilzt die beiden häufigsten Elemente, gibt das Ergebnis als neuen Korpus zurück

   
    # Ausgaben
    #print()
    #print(f"Iteration: {i}")
    #print(f"Gezählte Nachbarn: {pairs}")
    #print(f"Beste Paarung(en): {all_bests} Gewählt: {best}")
    #print(f"Aktualisierter Korpus {vocab}")

final_token_list = token_list(vocab)
print(f"Finale Token-Liste {final_token_list}")
