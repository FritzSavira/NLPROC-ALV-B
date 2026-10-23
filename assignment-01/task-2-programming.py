# Bei dem CMU Pronouncing Dictionary http://www.speech.cs.cmu.edu/cgi-bin/cmudict
# unterscheidet sich Codierung der Phoneme im wesentlichen dadurch von dem IPA-System,
# dass Großbuchstaben des lateinischen Alphabets verwendet werden. Bei dem IPA-System wird 
# für jedes Phonem ein eigenes Zeichen genutzt. Das Phonemen-Set besteht aus 39 Phonemen,
# aus denen die Worte zusammengesetzt werden. Betonungen werden durch die Indizes
# 0=Ohne Betonung, 1=primäre Betonung, 2=sekundäre Betonung abgebildet.
# Das CMU Pronouncing Dictionary nutzt das ARPABET https://en.wikipedia.org/wiki/ARPABET,
# ein set phonetischer Transkriptions-Codes, die in den 1970er Jahren von
# der Advanced Research Projects Agency (ARPA) entwickelt wurde.

# Pronounciation of "Peter but the blue book ..."
import pronouncing

sentence = ["Peter", "put", "the", "blue", "book", "beside", "the", "big", "window"]

for word in sentence:
    print(f"{word}: {pronouncing.phones_for_word(word)}")


# The Chaos was taken from: https://ncf.idallen.com/english.html

with open("the-chaos.txt", "r", encoding="utf-8") as file:
    text = file.read
    print(text)

