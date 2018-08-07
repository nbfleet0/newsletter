import fortune
import techcrunch
import vcnewsdaily
import pehub
import seeddb
import time


if __name__ == '__main__':
	f = open('stories.txt', 'w')
	f.write('<center><table width="80%" style="border: 1px solid black; background-color:#ffffff" cellpadding="16">')
	f.close()
	time.sleep(1)

	fortune.getStories(2)
	techcrunch.getStories(2)
	vcnewsdaily.getStories(2)
	pehub.getStories(2)

	f = open('stories.txt', 'a')
	f.write('</table></center>')
	f.close()


	file = open("list.csv", "w").close() #clear file, list.csv is only used for debugging


	f = open('buzz.txt', 'w')
	f.write('<br /><br /><center><table width="50%" style="border: 1px solid black; background-color:#ffffff" cellpadding="2"><tr><td align="center" style="padding-left:5px;padding-right:5px;"><h2>Buzzy Companies</h2></td></tr>')
	f.close()

	f = open('fintech_buzz.txt', 'w')
	f.write('<table width="50%" style="border: 1px solid black; background-color:#ffffff" cellpadding="2"><tr><td align="center" style="padding-left:5px;padding-right:5px;"><h2>Buzzy Companies</h2></td></tr>')
	f.close()
	time.sleep(1)

	seeddb.getBuzzyCompanies(10, [2001, 1011], 2018, 1) #number of top companies, array of acclerator id's from seed-db.com, earliest year we're interested in, interest level threshold

	f = open('buzz.txt', 'a')
	f.write('</table>')
	f.close()

	f = open('fintech_buzz.txt', 'a')
	f.write('</table></center>')
	f.close()


 