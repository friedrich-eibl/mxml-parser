[Deutsch](README_de.md)

# mxml-parser

This parser is a Program to read MusicXML-files with the file extension .mxml or
.xml and store them in an array. MXML is one of the most common file formats for storing musical notes and can be downloaded on many sites e.g. musescore.com


## Prerequisites

The only necessary library for the usage of this parser is the xml.sax library. If you also plan on using the player.py file you will need additional access to the pysine library. 


## Download

There are two ways to download the files.

The easiest option is to simply use the GitHub-UI. If for some reason this doesnot work for you, you can use the linux command:


```bash
git clone https://github.com/friedrich-eibl/mxml-parser
```

It is also possible to only download parser.py and use it as a standalone script. The seperate usage of the player.py script on the other hand will not work since it requires the parser for running properly. If you want to use player.py, you will also need the notes.py file, which stores the frequency values of all tones playable by a standard piano. 


## Usage

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
handler.notes is an Array, which stores all notes of the parsed file using following format:

handler.notes = ["C1whole", "Ab4eighth", . . . ]  or generally speaking handler.notes = [<step><octave><duration>]

#### handler2.key
handler2.key contains the key as an integer referencing its spot on the circle of fifths:

- negative numbers for b's
- 0 for C-Major/a-Minor
- positive numbers for #'s 

### Important:

As of this stage the Player only works for single-voice sheet music!

## Contact

For questions/requests send an e-mail to: friedrich-eibl@hu-berlin.de 
