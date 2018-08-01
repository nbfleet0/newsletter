import fortune
import techcrunch
import vcnewsdaily
import pehub
import time
import send


if __name__ == '__main__':
	f = open('stories.txt', 'w')
	f.write('<html style="background-color:#ecf0f1; font-family: Helvetica, Arial, sans-serif; a{color:#006699;}"><center><table width="80%" style="border: 1px solid black; background-color:#ffffff" cellpadding="16">')
	f.close()
	time.sleep(1)

	fortune.getStories(1)
	techcrunch.getStories(1)
	vcnewsdaily.getStories(1)
	pehub.getStories(1)

	f = open('stories.txt', 'a')
	f.write('</table></center>	</html>')
	f.close()

	send.sendEmail()