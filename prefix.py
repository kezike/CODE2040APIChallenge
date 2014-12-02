import json
import urllib2

regInfo = {"token":"ikzx5gqLtN"}
req = urllib2.Request('http://challenge.code2040.org/api/prefix')
req.add_data(regInfo)
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(regInfo))
response = response.read()
print response
#response = {"result":{"array":["675iFATV","675PZlYX","675089za","675BJLEB","187vhY2J","308ZBQIQ"],"prefix":"308"}}

#*****************************************************************************************************************#

response = {"array":["675iFATV","675PZlYX","675089za","675BJLEB","187vhY2J","308ZBQIQ"],"prefix":"308"}
##There may have been a built in string method to accomplish this, but I decided
##to use the length of the prefix to index into the each of the strings from the
##beginning up until this index in order to determine if the string contained the
##the prefix or not:
noPref = [i for i in response["array"] if i[:len(response["prefix"])] != response["prefix"]]

prefix = {"token":"ikzx5gqLtN", "array":noPref}

req = urllib2.Request('http://challenge.code2040.org/api/validateprefix')
req.add_data(prefix)
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(prefix))
response = response.read()
print response
