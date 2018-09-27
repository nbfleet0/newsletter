import fortune
import techcrunch
import vcnewsdaily
import pehub
import seeddb
import time
import csv


def scrape_daily():
	#parameter in the function signifies the threshold of interest level, i.e. the number of keywords in each story
	#it's currently set as 2

	titles = set()
	with open('./data/story_companies.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			titles.add(row[0])

	techcrunch.getStories(2, titles)
	print (titles)
	vcnewsdaily.getStories(2, titles)
	print (titles)
	pehub.getStories(2, titles)
	print (titles)

	with open('./data/story_companies.csv', 'a') as csvfile:
		csvwriter = csv.writer(csvfile)
		for ele in titles:
			csvwriter.writerow([ele])

	print ('daily scrape finished')
	
if __name__ == '__main__':
	scrape_daily()




 