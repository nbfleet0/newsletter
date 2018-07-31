import urllib2
import xml.etree.ElementTree as et
import requests
import helper_functions as helper
import cookielib


def getStories():

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    req = urllib2.Request("https://www.pehub.com/category/vc-deals/feed/", headers=hdr)
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
    contents = page.read()

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
