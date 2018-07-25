try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import xml.etree.ElementTree as et
import requests
import helper_functions as helper


def getStories():

    contents = urlopen("https://www.pehub.com/category/vc-deals/feed/").read()
    root = et.fromstring(contents)
    channel = root.find('channel')

    for item in channel.iter('item'):

        # get title, date, and link url from xml feed
        title = item.find('title').text
        date = item.find('pubDate').text
        link = item.find('link').text
        article_text = item.find('description').text

        # check for interesting geographies
        interest_lvl = helper.checkInterestLvl(article_text)

        if (interest_lvl > 1): #more than 2 interesting aspects of an article

            string = "\n\nTitle: " + title + "\nDate: " + date + "\nLink: " + link + "\nArticle Text: " + article_text
            save_file = open("stories.txt", 'a+')
            save_file.write(string.encode('utf-8'))
            save_file.close()
