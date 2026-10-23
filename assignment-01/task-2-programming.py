# Bei dem CMU Pronouncing Dictionary http://www.speech.cs.cmu.edu/cgi-bin/cmudict
# unterscheidet sich Codierung der Phoneme im wesentlichen dadurch von dem IPA-System,
# dass Großbuchstaben des lateinischen Alphabets verwendet werden. Bei dem IPA-System wird 
# für jedes Phonem ein eigenes Zeichen genutzt. Das Phonemen-Set besteht aus 39 Phonemen,
# aus denen die Worte zusammengesetzt werden. Betonungen werden durch die Indizes
# 0=Ohne Betonung, 1=primäre Betonung, 2=sekundäre Betonung abgebildet.
# Das CMU Pronouncing Dictionary nutzt das ARPABET https://en.wikipedia.org/wiki/ARPABET,
# ein Set phonetischer Transkriptions-Codes, die in den 1970er Jahren von
# der Advanced Research Projects Agency (ARPA) entwickelt wurde.

# Pronounciation of "Peter put the blue book ..."
import pronouncing

sentence = ["Peter", "put", "the", "blue", "book", "beside", "the", "big", "window"]
for word in sentence:
    print(f"{word}: {pronouncing.phones_for_word(word)}")
print()


# The Chaos was taken from: https://ncf.idallen.com/english.html
# Erledigt: Write a function are_rhymes(word1, word2) that returns
# True for slant or exact rhymes (e.g., “skate” and “eight”) despite mismatched spellings.
# Noch offen: Extract the nucleus and coda of the
# primary stressed syllable to define a valid rhyme condition.

def are_rhymes(word1, word2):                   # Reim-Funktion
    rhyme = word1 in pronouncing.rhymes(word2)
    return rhyme

word1 = ""                                              # Ablage wort1 initiieren
word2 = ""                                              # Ablage wort2 initiieren
# eigenen lokalen Pfad in input_file eintragen:
input_file = "C:/Users/Fried/OneDrive/Studium/Inf/NLPROC-ALV-B/assignment-01/the-chaos.txt"
with open(input_file, "r", encoding="utf-8") as file:
    for line in file:
        if len(line) > 1:                               # Leerzeilen überspringen
            end_word = line.split()[-1]                 # letztes Wort holen
            end_word = end_word.rstrip(".,;:-?!\"\)'")  # Satzzeichen rechts löschen
            end_word = end_word.lstrip(".,;:-?!\"\)'")  # Satzzeichen links löschen
            if word1 == "":                             # letztes Wort Satz 1 ablegen 
                word1 = end_word
            elif word2 == "":                           # letztes Wort Satz2 ablegen
                word2 = end_word
                print(word1, word2, are_rhymes(word1, word2)) # abgelegtes Wortpaar auf Reim mit Funktion prüfen.
                word1 = ""                              # Ablage wort1 leeren
                word2 = ""                              # Ablage wort2 leeren
            
        
       
