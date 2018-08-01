import scraper_functions


def calculateScore(object):
	# print("calculating score")
    # object: [angellist url, crunchbase url, exited?, name, url, acceleration date, exit value, ?, funding]
	if(object[2] == "" and object[4] != "None" and object[1] != ""): #if comnpany hasnt exited or died

	# ["", "CB.COM","","Even","even.com","","","",""]

		cbinfo = scraper_functions.infoFromCrunchbase(object[1]) # angelinfo: [twitter, cbrank, funding]

		followers = scraper_functions.numberOfTwitterFollowers(cbinfo[0])
		cbrank = cbinfo[1]
		funding = cbinfo[2] #going off cb
		if(funding == ""):
			funding = object[8] #fallback
		webresults = scraper_functions.numberOfWebResults(object[4])

		alexa_object = scraper_functions.getAlexaRankings(object[4].replace('https://', '').replace('http://', '')) # [rank, rank_increase, inbound_links, home_geo, bounce_rate%, search_increase%
		# print(alexa_object)
		rank = alexa_object[0]
		rank_increase = alexa_object[1]
		inbound_links = alexa_object[2]
		home_geo = alexa_object[3]
		bounce_rate = alexa_object[4]
		search_increase = alexa_object[5]

		static_web = [int(followers), int(webresults), int(rank), int(inbound_links), bounce_rate]


		print(static_web)
		static_constant = (int(followers)/10 + int(webresults)/10 + int(inbound_links)*5 - bounce_rate*2)/(int(rank)/50000) 
		print(static_constant)

		dynamic_web = [rank_increase, search_increase]
		print(dynamic_web)

		dynamic_constant = rank_increase
		dynamic_constant = rank_increase*search_increase/1000

		print(dynamic_constant)

		return (static_constant+dynamic_constant)
	else:
		return object[3] + " exited, has no crunchbase, or no website"

print(calculateScore(['', 'https://www.crunchbase.com/organization/clustrix', '', 'clustrix', 'www.clustrix.com', '6/2010', '$15,000,000', 'H', '$1,000,000']))
