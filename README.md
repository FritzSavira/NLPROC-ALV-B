# NLPROC-ALV-B – Natural Language Processing

Unterlagen und Übungsabgaben zur Lehrveranstaltung **Natural Language Processing (Introduction to NLP)** im Wintersemester 2026/27 an der Otto-Friedrich-Universität Bamberg, Lehrstuhl für Grundlagen der Sprachverarbeitung.

Dozierende: Roman Klinger und Sabine Weber

## Ziel der Veranstaltung

Die Veranstaltung gibt einen Überblick über die zentralen Herausforderungen der Sprachverarbeitung und stellt beispielhafte Methoden vor, mit denen sie sich lösen lassen. Sie zielt nicht auf State-of-the-Art-Verfahren, sondern legt das Fundament dafür. Der Schwerpunkt liegt auf dem Sprachverstehen (Natural Language Understanding), nicht auf der Sprachgenerierung.

## Themen

- Phonetik – Wortfolgen aus einem Audiosignal rekonstruieren
- Preprocessing und Tokenisierung
- Part-of-Speech-Tagging, Shallow Parsing und Konstituentenanalyse
- Dependenzanalyse
- Lexikalische Semantik (Wortbedeutungen, WordNet)
- Ähnlichkeit und distributionelle Semantik
- Kompositionelle und kontextualisierte distributionelle Semantik
- Attention-Mechanismus, Transformer und Large Language Models
- Informationsextraktion und Named Entity Recognition
- Relationsextraktion und Semantic Role Labeling

## Organisation

| | |
|---|---|
| Vorlesung | dienstags 16–18 Uhr, WE5/04.003 |
| Übung / Fragestunde | donnerstags 10–12 Uhr, GU13/01.03 |
| Sprache | Deutsch (Englisch auf Anfrage), Folien auf Englisch |
| Kursplattform | Virtueller Campus (VC) |
| Prüfung | schriftliche Klausur (60 Minuten) nach Semesterende |

Prüfungsrelevant sind alle Themen aus Vorlesung und Übung, auch Inhalte, die nur auf den Übungsblättern vorkommen.

## Übungen

- Kurz nach jeder Vorlesung erscheint ein Übungsblatt mit Pen-&-Paper- und Programmieraufgaben.
- Abgabe über den VC bis zum Ende des auf dem Blatt genannten Tages; verspätete Abgaben sind nicht möglich.
- Gruppen aus 1–3 Personen; die Zusammensetzung darf von Blatt zu Blatt wechseln.
- Abgegeben wird eine einzige PDF-Datei pro Gruppe, mit Programmcode und den Namen und E-Mail-Adressen aller Gruppenmitglieder auf der ersten Seite.
- Pro Blatt gibt es 20 Punkte. 80 % der Gesamtpunktzahl gelten als perfekte Teilnahme; die Punkte fließen als Bonus mit bis zu 20 % in die Klausurnote ein (sofern die Klausur auch ohne Bonus bestanden ist).
- Ausgewählte Gruppen stellen ihre Lösungen in der Übung vor. Wer auf Anfrage nicht präsentieren kann, erhält für diese Abgabe keine Punkte.
- **KI-Werkzeuge:** Der Einsatz von LLMs wird nicht empfohlen. Wer sie nutzt, muss System, vollständigen Prompt und vollständige Antwort im Anhang dokumentieren; bewertet wird nur der eigene Beitrag. Nicht offengelegte Nutzung gilt als Plagiat.
- **Plagiat:** führt zu null Punkten für die gesamte Abgabe aller beteiligten Gruppen.

## Repository-Struktur

```
.
├── NLPROC-AVL-B-XX-*.pdf    Vorlesungsfolien
├── nlp-plan-ws2026-2027.pdf Semesterplan (vorläufig)
└── assignment-XX/           Übungsblatt, Materialien und Lösungen je Übung
```

Praat-Verzeichnisse (Programm und Schriften) sind nicht eingecheckt, siehe `.gitignore`.

## Werkzeuge

- [Praat](https://praat.org/) – Analyse von Sprachaufnahmen (Wellenform, Spektrogramm, Formanten)
- Python mit NLP-Bibliotheken für die Programmieraufgaben

## Literatur

- Jurafsky, Daniel und James H. Martin (2009): *Speech and Language Processing* (2. Auflage). Prentice Hall.
- Weiteres Material wird im Laufe des Semesters bereitgestellt.
