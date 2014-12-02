import json
import urllib2

regInfo = {"token":"ikzx5gqLtN"}
req = urllib2.Request('http://challenge.code2040.org/api/haystack')
req.add_data(regInfo)
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(regInfo))
response = response.read()
print response
#response = {"result":{"haystack":["MFIFc","8Vw3b","37wsb","CJtWB","8fQey","Wpz0C","2mEIu","uIcV8","z3U0J","rSPj4","vGUpD","KewyI","MUQ08","RdXFp","sBI5f","tMAYN","r1yMn","BfbPK","yOQM6","iPIHs"],"needle":"MFIFc"}}

#********************************************************************************************************************************************************************************************************************#

response = {"haystack":["MFIFc","8Vw3b","37wsb","CJtWB","8fQey","Wpz0C","2mEIu","uIcV8","z3U0J","rSPj4","vGUpD","KewyI","MUQ08","RdXFp","sBI5f","tMAYN","r1yMn","BfbPK","yOQM6","iPIHs"],"needle":"MFIFc"}

i = 0
while response['haystack'][i] != response['needle']:
    i += 1

needle = {"token":"ikzx5gqLtN", "needle":i}

req = urllib2.Request('http://challenge.code2040.org/api/validateneedle')
req.add_data(needle)
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(needle))
response = response.read()
print response
