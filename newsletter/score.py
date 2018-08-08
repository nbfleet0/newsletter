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
		if(cb_object == 0):
			return [0, 0, 0, 0, 0, 0, 0, 0]

	followers = scraper_functions.numberOfTwitterFollowers(cb_object[0])
	cbrank = cb_object[1]
	funding = cb_object[2] #going off cb
	categories = cb_object[4]
	interesting_words = helper.checkInterestLvl(categories)

	if(funding == ""):
		funding = object[2] #fallback
	webresults = scraper_functions.numberOfWebResults(object[1])
	if webresults == 0:
		print("WARNING - NO WEB RESULT DATA")

	alexa_object = scraper_functions.getAlexaRankings(object[1].replace('https://', '').replace('http://', '')) # [rank, rank_increase, inbound_links, home_geo, bounce_rate%, search_increase%

	rank = alexa_object[0]
	rank_increase = alexa_object[1]
	inbound_links = alexa_object[2]
	home_geo = alexa_object[3]
	bounce_rate = alexa_object[4]
	search_increase = alexa_object[5]
	rank_change = alexa_object[6]

	rank_increase = rank_increase*rank_change
	print("rank change")
	print(rank_change)

	static_web = [int(followers), int(webresults), int(rank), int(inbound_links), bounce_rate]

	if(rank == 0 or rank == ''): #no alexa data, ignore startups with broken/unvisited websites
		return [0, 0, 0, 0, 0, 0, 0, 0]

	print(static_web)

	static_constant = (int(followers)/4 + int(webresults) + int(inbound_links)*10 - float(rank)/10000)/(bounce_rate/100)
#top = (356000 + 500000 + 8000*10 - 300/10000)/(50/100)

	print(static_constant)
	#best: 438000


	dynamic_web = [rank_increase, search_increase]
	print(dynamic_web)

	rank_increase = (rank_increase/rank)*100 #express as a percentage

	if rank_increase == 0:
		rank_increase = 1
	if search_increase == 0:
		search_increase = 1

	dynamic_constant = rank_increase*search_increase
	print(dynamic_constant)

	total_score = (static_constant+dynamic_constant)/500 #500000 0-1, 50000 0-10, 5000 0-100

	print(total_score)
	interestLvl = len(interesting_words)

	all_web = [total_score, int(followers), int(webresults), int(rank), int(inbound_links), bounce_rate, rank_increase, search_increase, interestLvl]


	return all_web

def getBuzzScore(story_obj):
	name = helper.extractName(story_obj)
	if name == "":
		print("couldnt find name for " + story_obj[0])
		return 0

	cburl = helper.getCrunchbaseURL(name)
	print(cburl)

	cbinfo = scraper_functions.infoFromCrunchbase(cburl)

	if(cbinfo != 0):
		buzz_score = calculateScore([cburl, cbinfo[3], "", name, cbinfo])
		return buzz_score[0]
	else:
		print("no cbinfo")
		return 0
