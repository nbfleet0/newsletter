try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import xml.etree.ElementTree as et
import requests
import helper_functions


def getStories():

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
        half_one = html.split('<div id="fullArticle" class="fullArticle">')[2]
        article_text = half_one.split('</div>')[0]

        # check interest
        interest_lvl = helper_functions.checkInterestLvl(article_text)


        if (interest_lvl > 1): #more than 2 interesting aspects of an article
            string = "\n\nTitle: " + title + "\nDate: " + date + "\nLink: " + link + "\nArticle Text: " + article_text
            save_file = open("stories.txt", 'a+')
            save_file.write(string)
            save_file.close()
