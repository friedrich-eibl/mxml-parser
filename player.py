import xml.sax
#import parser
from parser import sheetHandler as sH
from pysine import sine
import notes
################################
# TESTCASES:
#xmlFile = 'test.mxml' 			# --- works
xmlFile = 'test2.xml'			# --- works
#xmlFile = 'test3.xml'			# --- works
################################


#################################
# This is an player script      #
# for the parsed notes		    #
# (more information in README)	#
# (C) 2020 Friedrich Eibl		#
#################################



parser = xml.sax.make_parser()
handler = sH()

parser.setContentHandler(handler)
parser.parse(xmlFile)
print(handler.notes)

noteLength = 0
metrum=2

i=0
while i < len(handler.notes):
    if(handler.notes[i][2:] == "whole"): noteLength=1.0
    elif(handler.notes[i][2:] == "half"): noteLength=0.5
    elif(handler.notes[i][2:] == "quarter"): noteLength=0.25
    elif(handler.notes[i][2:] == "eighth"): noteLength=0.125
    
    sine(frequency=getattr(notes, handler.notes[i][:2]),duration=noteLength*metrum)
    i+=1

print("Successfully played piece :)")