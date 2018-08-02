import scraper_functions
import helper_functions as helper

def calculateScore(object):
	# print("calculating score")
    # object: [cb url, url, funding, name, cbinfo?]
	print(object[0])
	if len(object) == 5:
		cb_object = object[4]
	else:
		cb_object = scraper_functions.infoFromCrunchbase(object[0]) 

	followers = scraper_functions.numberOfTwitterFollowers(cb_object[0])
	cbrank = cb_object[1]
	funding = cb_object[2] #going off cb
	if(funding == ""):
		funding = object[2] #fallback
	webresults = scraper_functions.numberOfWebResults(object[1])

	alexa_object = scraper_functions.getAlexaRankings(object[1].replace('https://', '').replace('http://', '')) # [rank, rank_increase, inbound_links, home_geo, bounce_rate%, search_increase%

	rank = alexa_object[0]
	rank_increase = alexa_object[1]
	inbound_links = alexa_object[2]
	home_geo = alexa_object[3]
	bounce_rate = alexa_object[4]
	search_increase = alexa_object[5]

	static_web = [int(followers), int(webresults), int(rank), int(inbound_links), bounce_rate]

	if(rank == 0 or rank == ''): #no alexa data, ignore startups with broken/unvisited websites
		return [0, 0, 0, 0, 0, 0, 0, 0]

	print(static_web)

	static_constant = (int(followers)/10 + int(webresults)/10 + int(inbound_links)*5 - bounce_rate*2)/float(rank)

	print(static_constant)

	dynamic_web = [rank_increase, search_increase]
	print(dynamic_web)

	dynamic_constant = rank_increase

	dynamic_constant = rank_increase*search_increase/1000
	print(dynamic_constant)

	all_web = [static_constant+dynamic_constant, int(followers), int(webresults), int(rank), int(inbound_links), bounce_rate, rank_increase, search_increase]


	return all_web

def getBuzzScore(story_obj):
	name = helper.extractName(story_obj)

	cburl = helper.getCrunchbaseURL(name)

	cbinfo = scraper_functions.infoFromCrunchbase(cburl)

	print(cbinfo)

	buzz_score = calculateScore([cburl, cbinfo[3], "", name, cbinfo])
	return buzz_score[0]

