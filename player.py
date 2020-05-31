import xml.sax
#import parser
from parser import sheetHandler as sH
from pysine import sine
import notes
import time

################################
# TESTCASES:
#xmlFile = 'test.mxml' 			# --- works
xmlFile = 'test2.xml'			# --- works
#xmlFile = 'ssb.xml'			# --- works
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

### move key functionality to parser later
key=6 #amount of b's(negative) or #'s(positive)


#TODO: use it in while-loop to adjust the tones accordingly by inserting a b in the name if negative and inserting a b + counting up one letter if #
#key can also be parsed from xml in this format

#key signature as list for key from c to b
signature = ['','','','','','',''] #standard key is C-Major
if key < 0:
    signature[6] = 'b'
    if key < -1:
        signature[2] = 'b'
    if key < -2:
        signature[5] = 'b'
    if key < -3:
        signature[1] = 'b'
    if key < -4:
        signature[4] = 'b'
    if key < -5:
        signature[0] = 'b'

if key > 0:
    signature[3] = '#'
    if key > 1:
        signature[0] = '#'
    if key > 2:
        signature[4] = '#'
    if key > 3:
        signature[1] = '#'
    if key > 4:
        signature[5] = '#'
    if key > 5:
        signature[2] = '#'

print(signature)


#adjust notes
i=0
while i < len(handler.notes):
    if(handler.notes[i][0] == 'C'):
        handler.notes[i] = handler.notes[i][:1]+signature[0]+handler.notes[i][1:]
    elif(handler.notes[i][0] == 'D'):
        handler.notes[i] = handler.notes[i][:1]+signature[1]+handler.notes[i][1:]
    elif(handler.notes[i][0] == 'E'):
        handler.notes[i] = handler.notes[i][:1]+signature[2]+handler.notes[i][1:]
    elif(handler.notes[i][0] == 'F'):
        handler.notes[i] = handler.notes[i][:1]+signature[3]+handler.notes[i][1:]
    elif(handler.notes[i][0] == 'G'):
        handler.notes[i] = handler.notes[i][:1]+signature[4]+handler.notes[i][1:]
    elif(handler.notes[i][0] == 'A'):
        handler.notes[i] = handler.notes[i][:1]+signature[5]+handler.notes[i][1:]
    elif(handler.notes[i][0] == 'B'):
        handler.notes[i] = handler.notes[i][:1]+signature[6]+handler.notes[i][1:]

    i+=1

#helping array for translating #'s to b's
octaveArray = ['C','D','E','F','G','A','B']
i=0
while i < len(handler.notes):
    
    #checks for note format
    if(handler.notes[i][0].isupper()):
        if(handler.notes[i][-5:] == "whole"): noteLength=1.0
        elif(handler.notes[i][-4:] == "half"): noteLength=0.5
        elif(handler.notes[i][-7:] == "quarter"): noteLength=0.25
        elif(handler.notes[i][-6:] == "eighth"): noteLength=0.125
        elif(handler.notes[i][-4:] == "16th"): noteLength=0.0625
        else: print('ERROR: Could not read note-length of note' + handler.notes[i])

        #translate #'s to b's for conformity with variable names of stored frequences
        if handler.notes[i][1] == "#":
            if handler.notes[i][0] == 'B':
                handler.notes[i] = 'C' + handler.notes[i][2:]
            elif handler.notes[i][0] == 'E':
                handler.notes[i] = 'F' + handler.notes[i][2:]
            else:
                n=0
                while n < len(octaveArray):
                    if octaveArray[n] == handler.notes[i][0]:
                        handler.notes[i] = octaveArray[(n+1)%7] + "b" + handler.notes[i][2:]
                        break
                    n+=1 
        #play sounds
        if handler.notes[i][1] == "b":
            sine(frequency=getattr(notes, handler.notes[i][:3]),duration=noteLength*metrum)
        else:
            sine(frequency=getattr(notes, handler.notes[i][:2]),duration=noteLength*metrum)
    
    #checks for pauses
    if(handler.notes[i][0].islower()):
        if(handler.notes[i] == "whole"): noteLength=1.0
        elif(handler.notes[i] == "half"): noteLength=0.5
        elif(handler.notes[i] == "quarter"): noteLength=0.25
        elif(handler.notes[i] == "eighth"): noteLength=0.125

        time.sleep(noteLength)
    
    i+=1

print("Successfully played piece :)")