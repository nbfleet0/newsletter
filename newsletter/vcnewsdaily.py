try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import xml.etree.ElementTree as et
import requests
import helper_functions as helper


def getStories(lvl):

    contents = urlopen("https://feeds.feedburner.com/vcnewsdaily?fmt=xml").read()
    root = et.fromstring(contents)
    channel = root.find('channel')


    for item in channel.iter('item'):

        # get title, date, and link url from xml feed
        title = item.find('title').text
        date = item.find('pubDate').text
        link = item.find('link').text

        # get article text from link
        article = requests.get(link, verify=False)
        html = article.content
        half_one = html.split('<div id="fullArticle" class="fullArticle">')
        article_text = ""
        if(len(half_one) > 1):
            half_two = half_one[2]
            article_text = half_two.split('</div>')[0]


        # check interest
        interest_lvl = helper.checkInterestLvl(article_text)


        if (interest_lvl > lvl): #more than 2 interesting aspects of an article
            print("Adding article")

            article_text = article_text.split("<br/><br/>About")[0]
            print(article_text)

            string = "\n\n<b><a href='" + link + "'>" + title + "</a></b>\n\n" + article_text
            save_file = open("stories.txt", 'a+')
            save_file.write(string)
            save_file.close()

