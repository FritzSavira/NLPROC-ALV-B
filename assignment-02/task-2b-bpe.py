# Genutzte Ressourcen: https://towardsdatascience.com/byte-pair-encoding-for-beginners-708d4472c0c7/
# und https://arxiv.org/pdf/1508.07909

import collections
import re

# corpus
vocab = {'l o w </w>' : 5,
         'l o w e r </w>' : 2,
         'l o w e s t </w>' : 3,
         'n e w e r </w>' : 3,
         'w i d e r </w>' : 2,
         'w i d e s t </w>' : 3}

# print corpus
print("print corpus")
for word, freq in vocab.items():
    word_list = word.split()
    print(word_list, freq)

def get_stats(vocab):
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        elements = word.split()
        for i in range(len(elements)-1): # -1, weil i noch einen Nachfolger haben muss.
            pairs[elements[i], elements[i+1]] += freq
    return pairs

# print pairs
print()
print("print pairs")
print(dict(get_stats(vocab)))


def merge_vocab(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out

print()
print("merge_vocab")
print(merge_vocab(('l', 'o'), vocab))
print(merge_vocab(('e','s'), {'n we st </w>': 1}))


