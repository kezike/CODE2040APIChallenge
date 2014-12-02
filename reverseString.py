import json
import urllib2

regInfo = {"token":"ikzx5gqLtN"}
req = urllib2.Request('http://challenge.code2040.org/api/getstring')
req.add_data(regInfo)
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(regInfo))
response = response.read()
print response
#response = {"result":"W1q9V"}

#******************************************************************#

response = "W1q9V"
revString = {"token":"ikzx5gqLtN", "string":response[::-1]}
req = urllib2.Request('http://challenge.code2040.org/api/validatestring')
req.add_data(revString)
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(revString))
response = response.read()
print response
