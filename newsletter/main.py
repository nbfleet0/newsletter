import fortune
import techcrunch
import vcnewsdaily
import pehub


if __name__ == '__main__':
	open('stories.txt', 'w').close()
	fortune.getStories(2)
	techcrunch.getStories(2)
	vcnewsdaily.getStories(2)
	pehub.getStories(2)
 