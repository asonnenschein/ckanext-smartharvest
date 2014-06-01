csw = "http://geothermaldata.org/csw?request=GetRecords&service=CSW&version=2.0.2&resultType=results&outputSchema=http://www.isotc211.org/2005/gmd&typeNames=csw:Record&elementSetName=summary&maxRecords=10"

import requests
import xml.sax
import xml.sax.handler

class SAXHandler(xml.sax.handler.ContentHandler):
	def startElement(self, name, attrs):
		print name, attrs

r = requests.get(csw, stream=True)

#d = xml.sax.parse(data, SAXHandler())

parser = xml.sax.make_parser()
parser.setContentHandler(SAXHandler())
parser.parse(r.raw)