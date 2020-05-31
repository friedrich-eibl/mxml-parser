# mxml-Parser

Der mxml-Parser ist ein Programm um MusicXML-Dateien, welche ein beliebtes Format zum Download digitaler Noten sind einzulesen und die Noten nach dem unten erklärten Format in einem Array zu speichern.


## Vorraussetzungen

Für das Verwenden des Parsers brauchen Sie ausschließlich die xml.sax bibliothek. Für den Player benötigen Sie zusätzlich einen Teil der pysine bibliothek.


## Download

Sie können die Dateien entweder direkt hier von GitHub herunterladen oder in Ihrem Terminal folgenden Befehl verwenden:

```bash
git clone https://github.com/friedrich-eibl/mxml-parser
```
Es ist auch möglich nur den parser.py herunterzuladen und unabhängig zu nutzen. Für das player.py skript ist dies jedoch nicht möglich da es auf dem Parser aufbaut und diesen verwendet. Zusätzlich brauchen sie für player.py die datei notes.py welche die Frequenzen zur Wiedergabe enthält.


## Benutzung

```python
import xml.sax
from parser import sheetHandler
from parser import addInfo 

#get notes
parser = xml.sax.make_parser()
handler = sH()

parser.setContentHandler(handler)
parser.parse(xmlFile)
print(handler.notes) #prints array of all notes

#get key and additional information
parser2 = xml.sax.make_parser()
handler2 = addInfo()

parser2.setContentHandler(handler2)
parser2.parse(xmlFile)
print(handler2.key) #prints out key
```
#### handler.notes
handler.notes ist ein Array, der alle Noten des eingelesenen Stückes nach folgendem Format speichert:

handler.notes = ["C1whole", "Ab4eighth", . . . ]  oder allgemein  handler.notes = [<step><octave><duration>]
#### handler2.key
handler2.key enthält die Vorzeichen als integer nach dem Quintenzirkel:

- negative Zahlen für b's
- 0 für C-Dur/a-Moll
- positive Zahlen für #'s 

###Wichtig:
Bis dato funktioniert der Player leider nur für einstimmige Notendarstellungen!

## Kontakt

Bei Fragen oder Vorschlägen bitte Email an: friedrich.eibl@hu-berlin.de 
