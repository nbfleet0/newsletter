import scraper_functions


def calculateScore(object):
	print("calculating score")
    # object: [angellist url, crunchbase url, exited?, name, url, acceleration date, exit value, ?, funding]
	if(object[2] == "" and object[4] != "None" and object[1] != ""): #if comnpany hasnt exited or died

		cbinfo = scraper_functions.infoFromCrunchbase(object[1]) # angelinfo: [twitter, cbrank, funding]

		followers = scraper_functions.numberOfTwitterFollowers(cbinfo[0])
		cbrank = cbinfo[1]
		funding = cbinfo[2] #going off cb
		if(funding == ""):
			funding = object[8] #fallback
		webresults = scraper_functions.numberOfWebResults(object[4])

		alexa_object = scraper_functions.getAlexaRankings(object[4].replace('https://', '').replace('http://', '')) # [rank, rank_increase, inbound_links, home_geo, bounce_rate%, search_increase%

		rank = alexa_object[0]
		rank_increase = alexa_object[1]
		inbound_links = alexa_object[2]
		home_geo = alexa_object[3]
		bounce_rate = alexa_object[4]
		search_increase = alexa_object[5]

		static_web = [int(followers), int(webresults), int(rank), int(inbound_links), bounce_rate]
		print(static_web)

		static_constant = int(followers) + int(webresults) - int(rank)/100 + int(inbound_links)*3 - bounce_rate
		print(static_constant)


		dynamic_web = [rank_increase, search_increase]

		return static_constant

# print(calculateScore(['https://angel.co/clustrix', 'http://www.crunchbase.com/organization/clustrix', '', 'Clustrix', 'http://www.clustrix.com', '1/2006', '', '', '$71,650,000']))
