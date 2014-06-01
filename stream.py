import requests
import xml.sax
import xml.sax.handler

url = "http://geothermaldata.org/csw"
payload = {"request": "GetRecords",
		   "service": "CSW",
		   "version": "2.0.2",
		   "resultType": "results",
		   "outputSchema": "http://www.isotc211.org/2005/gmd",
		   "typeNames": "csw:Record",
		   "elementSetName": "summary",
		   "maxRecords": "1"}

class SAXHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.parent_flag = False
		self.record = {}
		self.tag = ""

	def startElement(self, name, attrs):
		if name == "gmd:MD_Metadata":
			self.parent_flag = True
		if self.parent_flag:
			self.record[name] = ""
			self.tag = name

#			print name, dict(attrs)
#			self.child_list.append(name)
	
	def characters(self, content):
		print self.tag, content
		self.record[self.tag] += content

	def endElement(self, name):
		if name == "gmd:MD_Metadata":
			self.parent_flag = False
#			print self.record

response = requests.get(url, params=payload, stream=True)
raw_response = response.raw

xml.sax.parse(raw_response, SAXHandler())