import requests	
import urllib2
from lxml import html
import re
import score


# acceleratorid's: techstars - 3012, 500startups - 2001, angelpad - 2002, dreamid - 8001, seedcamp - 4005,

# print(score.calculateScore(['https://angel.co/rapportive', 'http://www.crunchbase.com/organization/rapportive', 'Exited', 'Rapportive', 'http://rapportive.com', '6/2010', '$15,000,000', 'H', '$1,000,000']))

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}


url = "https://www.seed-db.com/accelerators/viewall?acceleratorid=1011"

req = urllib2.Request(url, headers=hdr)
try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()
contents = page.read()
root = html.fromstring(contents)

# print("getting seed db")
for i in reversed(root.xpath('//*[@id="seedcos"]/tbody/tr')):
	# print("*ROW*")

	return_object = []

	return_object.append("")

	# angellist = i.xpath('td[3]/div/button[1]/a/@href')
	# if not angellist:
	# 	return_object.append("")
	# else:
	# 	return_object.append(angellist[0])

	crunchbase = i.xpath('td[3]/div/button[2]/a/@href')
	if not crunchbase:
		return_object.append("")
	else:
		return_object.append(crunchbase[0])

	box = i.xpath('td')

	for k in box:
		info = "".join(k.itertext())
		info = "".join(info.split()).replace("\n", "")
		return_object.append(info)

	# return_object: [angellist url = "", crunchbase url, exited?, name, url, acceleration date, exit value, ?, funding]

	# print(return_object)

	print(return_object[3] + ": " + str(score.calculateScore(return_object)))




