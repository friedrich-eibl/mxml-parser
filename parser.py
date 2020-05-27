import xml.sax

#################################
# This is an mxml-parser	#
# (more information in README)	#
# (C) 2020 Friedrich Eibl	#
#################################

class sheetHandler(xml.sax.ContentHandler):
	def __init__(self):

	#start element
	def startElement(self, tag, attributes):

	#end element
	def endElement(self, tag):

	#characters
	def characters(self, content):

parser = xml.sax.make_parser()
handler = sheetHandler()
