import fortune
import techcrunch
import vcnewsdaily
import pehub
import seeddb
import time


def scrape():
	f = open('./data/stories.txt', 'w')
	f.write('<center><table width="80%" style="border: 1px solid black; background-color:#ffffff" cellpadding="16">')
	f.close()
	time.sleep(1)

	#parameter in the function signifies the threshold of interest level, i.e. the number of keywords in each story
	#it's currently set as 2

	fortune.getStories(2) 
	techcrunch.getStories(2)
	vcnewsdaily.getStories(2)
	pehub.getStories(2)

	f = open('./data/stories.txt', 'a')
	f.write('</table></center>')
	f.close()

	##################################################################################
	##### NEED TO BE CHANGED ACCORDINGLY TO CRUNCHBASE VENTURE PARTNERS PROGRAM ######
	##################################################################################

	'''
	this section creates the "buzzy companies" list. It makes a ton of requests to crunchbase and google and will usually get us banned for the day. 
	only use when nessesary

	file = open("./data/list.csv", "w").close() #clear file, list.csv is only used for debugging


	f = open('./data/buzz.txt', 'w')
	f.write('<br /><br /><center><table width="50%" style="border: 1px solid black; background-color:#ffffff" cellpadding="2"><tr><td align="center" style="padding-left:5px;padding-right:5px;"><h2>Buzzy Companies</h2></td></tr>')
	f.close()

	f = open('./data/fintech_buzz.txt', 'w')
	f.write('<table width="50%" style="border: 1px solid black; background-color:#ffffff" cellpadding="2"><tr><td align="center" style="padding-left:5px;padding-right:5px;"><h2>Buzzy Fintech Companies</h2></td></tr>')
	f.close()
	time.sleep(1)

	seeddb.getBuzzyCompanies(10, [1011], 2012, 1) #number of top companies, array of acclerator id's from seed-db.com, earliest year we're interested in, interest level threshold

	f = open('./data/buzz.txt', 'a')
	f.write('</table>')
	f.close()

	f = open('./data/fintech_buzz.txt', 'a')
	f.write('</table></center>')
	f.close()
	'''

if __name__ == '__main__':
	scrape()




 