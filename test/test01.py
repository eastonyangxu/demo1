# import xml.sax
# import xml.sax.handler
# import pprint
#
#
# class XMLHandler(xml.sax.handler.ContentHandler):
#     def __init__(self):
#         self.buffer = ""
#         self.mapping = {}
#
#     def startElement(self, name, attributes):
#         self.buffer = ""
#
#     def characters(self, data):
#         self.buffer += data
#
#     def endElement(self, name):
#         self.mapping[name] = self.buffer
#
#     def getDict(self):
#         return self.mapping
#
#
# data = '<?xml version="1.0" encoding="UTF-8"?>' \
#        '<note><to>World</to><from>Linvo</from>' \
#        '<heading>Hi</heading><body>Hello World!</body></note>'
#
# xh = XMLHandler()
# xml.sax.parseString(data.encode(), xh)
# ret = xh.getDict()
#
# pprint.pprint(ret)
# print ret['note']
# print type(ret)
# print ret
