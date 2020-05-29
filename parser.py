import xml.sax

################################
# TESTCASES:
#xmlFile = 'test.mxml' 			# --- works
#xmlFile = 'test2.xml'			# --- X
xmlFile = 'test3.xml'			# --- X
################################

#################################
# This is an mxml-parser	#
# (more information in README)	#
# (C) 2020 Friedrich Eibl	#
#################################

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

	#start element
	def startElement(self, tag, attributes):
		self.currcont = tag
		if tag == 'note':
			print('++++ Note ++++')
			self.octaveCount = 0
			self.typeCount = 0


	#end element
	def endElement(self, tag):
		if self.currcont == 'step':
			print(' Step: ' + self.step)
		if self.currcont == 'octave' and self.octaveCount == 0:
			print(' Octave: ' + self.octave)
			self.octaveCount = 1
		elif self.currcont == 'type' and self.typeCount == 0:
			print(' Type: ' + self.type)
			self.typeCount = 1

	#characters
	def characters(self, content):
		if self.currcont == 'step':
			self.step = content
		if self.currcont == 'octave':
			self.octave = content
		elif self.currcont == 'type':
			self.type = content


parser = xml.sax.make_parser()
handler = sheetHandler()

parser.setContentHandler(handler)
parser.parse(xmlFile)
