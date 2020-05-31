import xml.sax

################################
# TESTCASES:
xmlFile = 'test2.xml' 			# --- works
#xmlFile = 'test2.xml'			# --- works
#xmlFile = 'test3.xml'			# --- works
################################

#################################
# This is an mxml-parser		#
# (more information in README)	#
# (C) 2020 Friedrich Eibl		#
#################################

#addInfo parses any additional info like key
class addInfo(xml.sax.ContentHandler):
	def __init__(self):
		self.currcont = ""
		self.key = 0
		self.keycounter = 0
	def startElement(self, tag, attributes):
		self.currcont = tag
		#if tag == 'key':
			#self.key = 0
	def endElement(self, tag):
		if self.currcont == 'fifths' and self.keycounter == 0:
			self.key = self.key
			#print("Key: " + self.key +'.')
	def characters(self, content):
		if self.currcont == 'fifths' and self.keycounter == 0:
			self.key = content
			self.keycounter += 1

#the sheetHandler gets the notes
class sheetHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.currcont = ""
		#data that is parsed for
		self.step = ""
		self.octave = ""
		self.type = ""
		#boolean values to prevent double parsing
		self.octaveCount = 0
		self.typeCount = 0 
		#array representation and cache variable
		self.notes = []
		self.currNote = ""
		#TODO: handle multiple voices, maybe add second array for base?

	#start element
	def startElement(self, tag, attributes):
		self.currcont = tag
		if tag == 'note':
			#print('++++ Note ++++')
			self.octaveCount = 0
			self.typeCount = 0
			self.currNote = ""

	#end element
	def endElement(self, tag):
		if self.currcont == 'step':
			#print(' Step: ' + self.step)
			self.currNote += self.step
		if self.currcont == 'octave' and self.octaveCount == 0:
			#print(' Octave: ' + self.octave)
			self.octaveCount = 1
			self.currNote += self.octave
		elif self.currcont == 'type' and self.typeCount == 0:
			#print(' Type: ' + self.type)
			self.typeCount = 1
			self.currNote += self.type
			self.notes.append(self.currNote)
		
	#characters
	def characters(self, content):
		if self.currcont == 'step':
			self.step = content
		if self.currcont == 'octave':
			self.octave = content
		elif self.currcont == 'type':
			self.type = content
	
	def getNotes(self):
		return self.notes


parser = xml.sax.make_parser()
handler = sheetHandler()

parser.setContentHandler(handler)
parser.parse(xmlFile)

#print(handler.notes)

parser2 = xml.sax.make_parser()
handler2 = addInfo()

parser2.setContentHandler(handler2)
parser2.parse(xmlFile)

#print(handler2.key)