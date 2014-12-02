import json
import urllib2
import datetime

regInfo = {"token":"ikzx5gqLtN"}
req = urllib2.Request('http://challenge.code2040.org/api/time')
req.add_data(regInfo)
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(regInfo))
response = response.read()
print response
#response = {"result":{"datestamp":"2024-01-15T15:22:00.000Z","interval":352497454}}

#**********************************************************************************#

response = {"datestamp":"2024-01-15T15:22:00.000Z","interval":352497454}

datestamp = response["datestamp"]
interval = response["interval"]

#search for first "-" in datestamp and store index in datestampDash1
datestampDash1 = datestamp.find("-")
#search for second "-" in datestamp and store index in datestampDash2
datestampDash2 = datestamp.find("-", datestampDash1+1)
#search for "T" in datestamp and store index in datestampT
datestampT = datestamp.find("T")
#search for first ":" in datestamp and store index in datestampCol1
datestampCol1 = datestamp.find(":")
#search for second ":" in datestamp and store index in datestampCol2
datestampCol2 = datestamp.find(":", datestampCol1+1)
#search for decimal point in datestamp and store index in datestampDec
datestampDec = datestamp.find(".")
#search for "Z" in datestamp and store index in datestampZ
datestampZ = datestamp.find("Z")

year = int(datestamp[:datestampDash1])
month = int(datestamp[datestampDash1+1:datestampDash2])
day = int(datestamp[datestampDash2+1:datestampT])
hour  = int(datestamp[datestampT+1:datestampCol1])
minute = int(datestamp[datestampCol1+1:datestampCol2])
second = int(datestamp[datestampCol2+1:datestampDec])
microsecond = int(datestamp[datestampDec+1:datestampZ])

dt = datetime.datetime(year,month,day,hour,minute,second, microsecond)
nds = dt + datetime.timedelta(0,interval)
newDateStamp = str(nds.year) + "-" + "0" + str(nds.month) + "-" + str(nds.day) + "T" + str(nds.hour) + ":" + str(nds.minute) + ":" + str(nds.second) + "." + str(nds.microsecond) + "00" + "Z"
time = {"token":"ikzx5gqLtN", "datestamp":newDateStamp}

req = urllib2.Request('http://challenge.code2040.org/api/validatetime')
req.add_data(time)
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(time))
response = response.read()
print response

'''
##Before I decided to take advantage of the datetime module provided by Python,
##I was thinking of manipulating modular arithmetic to determine appropriate values
##for the time intervals below. While this was a fun brainteaser that I may revisit
##in the future, I decided it would be a better investment of my time to use the
##datetime module in order to meet the deadline comfortably.
##Below are some of my original ideas in working progress:
yearDelta = interval/60/60/24/365
monDelta = (interval - yearDelta*12)%12
dayDelta = (interval - yearDelta*12)%12%365 - (interval - monDelta*30)%30
hourDelta = (interval - sum([yearDelta*365*12*24, monDelta*12*24, dayDelta*24]))/60/60
minDelta = (interval - sum([yearDelta*365*12*24*60, monDelta*12*24*60, dayDelta*24*60, hourDelta*60]))/60
secDelta = (interval - sum([yearDelta*365*12*24*60*60, monDelta*12*24*60*60, dayDelta*24*60*60, hourDelta*60, minDelta*60]))/1000000
micDelta = (interval - sum([yearDelta*365*12*24*60*60, monDelta*12*24*60*60, dayDelta*24*60*60, hourDelta*60, minDelta*60]))%1000000
'''
