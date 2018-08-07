import requests	
import urllib2
from lxml import html
import re
import score
import sys
import datetime



# acceleratorid's: techstars - 3012, 500startups - 2001, angelpad - 2002, dreamid - 8001, seedcamp - 4005,

# print(score.calculateScore(['https://angel.co/rapportive', 'http://www.crunchbase.com/organization/rapportive', 'Exited', 'Rapportive', 'http://rapportive.com', '6/2010', '$15,000,000', 'H', '$1,000,000']))

def getBuzzyCompanies(number, a_id, date, ilvl):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	   'Accept-Encoding': 'none',
	   'Accept-Language': 'en-US,en;q=0.8',
	   'Connection': 'keep-alive'}

	obj = {}
	fintech_obj = {}
	all_scores = []
	for accelerator in a_id:

		url = "https://www.seed-db.com/accelerators/viewall?acceleratorid=" + str(accelerator)

		req = urllib2.Request(url, headers=hdr)
		try:
		    page = urllib2.urlopen(req)
		except urllib2.HTTPError, e:
		    print e.fp.read()
		contents = page.read()
		root = html.fromstring(contents)

		max_array = []
		min_array = []



		print("getting id "+ str(accelerator))

		for i in root.xpath('//*[@id="seedcos"]/tbody/tr'):

			return_object = []

			return_object.append("")


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
			print(return_object)
			skip = False

			if(date != ""):
				a_date = int(return_object[5].split("/")[1])
				if(a_date < date):
					skip = True

			if(skip == False):
				if(return_object[2] == "" and return_object[4] != "None" and return_object[1] != ""): 
					pass_object = [return_object[1], return_object[4], return_object[8], return_object[3]] #[cb url, url, funding, name]
					reutrn_val = score.calculateScore(pass_object)

					print(reutrn_val)

					if(reutrn_val[0] != 0):
						string = return_object[3] + ": " + str(int(reutrn_val[0]))
						all_scores.append(string)

						obj[return_object[3]] = int(reutrn_val[0])

						interestLvl = reutrn_val[8] 
						if(interestLvl > ilvl):
							fintech_obj[return_object[3]] = int(reutrn_val[0])

						file = open("list.csv", "a+")
						file.write(string + ",")
						file.close()
					
					print("all:")
					print(all_scores)
				else:
					print("skipping " + return_object[3])
			else:
				print("year is too early for " + return_object[3])

	assembleTop(number, obj)

def assembleTop(number, obj):
	top_scores = sorted(obj, key=obj.get, reverse=True)[:number]

	fintech_top_scores = sorted(obj, key=fintech_obj.get, reverse=True)[:number]

	file = open("buzz.txt", "a+")
	i = 0
	for element in top_scores:
		file.write("<tr><td align='center'><h3>"+element+" - "+str(obj[element])+"</h3></td></tr>")
		i+=1
	file.close() #clear file

	file = open("fintech_buzz.txt", "a+")
	i = 0
	for element in fintech_top_scores:
		file.write("<tr><td align='center'><h3>"+element+" - "+str(fintech_obj[element])+"</h3></td></tr>")
		i+=1
	file.close() #clear file

