try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import xml.etree.ElementTree as et
import requests
import helper_functions as helper


def getStories(lvl):

    contents = urlopen("https://feeds.feedburner.com/TechCrunch/fundings-exits").read()
    root = et.fromstring(contents)
    channel = root.find('channel')

    for item in channel.iter('item'):

        # get title, date, and link url from xml feed
        title = item.find('title').text
        date = item.find('pubDate').text
        link = item.find('link').text
        article_text = item.find('description').text


        # check for interesting geographies
        interest_array = helper.checkInterestLvl(article_text)
        interest_lvl = len(interest_array)
        print(interest_array)

        if (interest_lvl > lvl): #more than 2 interesting aspects of an article
            print("Adding article")

            article_text = article_text.split("<br/><br/>About")[0]
            print(article_text)

            for word in interest_array:
                bold = "<b>" + word + "</b>"
                article_text = article_text.replace(word, bold).replace(word.capitalize(), "<b>" + word.capitalize() + "</b>")

            string = "\n\n<b><a href='" + link + "'>" + title + "</a></b>\n\n" + article_text
            save_file = open("stories.txt", 'a+')
            save_file.write(string.encode('utf-8'))
            save_file.close()
