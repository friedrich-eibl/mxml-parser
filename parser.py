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
		self.name = ""

	#start element
	def startElement(self, tag, attributes):
		self.currcont = tag
		if tag == 'note':
			print('++++ Note ++++')


	#end element
	def endElement(self, tag):
		if self.currcont == 'step':
			print(' Step: ' + self.name)

	#characters
	def characters(self, content):
		if self.currcont == 'step':
			self.name = content

parser = xml.sax.make_parser()
handler = sheetHandler()

parser.setContentHandler(handler)
parser.parse(xmlFile)
