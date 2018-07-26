import requests
import urllib2
from lxml import html
import re

url = "https://www.seed-db.com/accelerators/viewall?acceleratorid=1011"

# acceleratorid's: techstars - 3012, 500startups - 2001, angelpad - 2002, dreamid - 8001, seedcamp - 4005,

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}

req = urllib2.Request(url, headers=hdr)
try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()
contents = page.read()
root = html.fromstring(contents)


for i in root.xpath('//*[@id="seedcos"]/tbody/tr'):
	print("*ROW*")

	angellist = i.xpath('td[3]/div/button[1]/a/@href')
	print(angellist)
	crunchbase = i.xpath('td[3]/div/button[2]/a/@href')
	print(crunchbase)

	box = i.xpath('td')
	for k in box:
		info = "".join(k.itertext())
		info = "".join(info.split()).replace("\n", "")
		print(info + ",")

    # article_text = "".join(i.itertext())
    # print(article_text)