import xml.etree.ElementTree as et
import requests
import helper_functions as helper
from lxml import html
import datetime


def getStories():
    page = requests.get("http://fortune.com/newsletter/termsheet/?scrape=1")
    root = html.fromstring(page.text)
    tree = root.getroottree()

    for i in root.xpath('/html/body/custom/table[1]/tr[2]/td/table/tr[10]/td/table/tr/td/table/tr[1]/td/p'):
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        link = i.xpath('a/@href')[0]
        article_text = "".join(i.itertext())

        interest_lvl = helper.checkInterestLvl(article_text)

        if (interest_lvl > 1): #more than 2 interesting aspects of an article

            string = "\n\nDate: " + date + "\nLink: " + link + "\nArticle Text: " + article_text
            save_file = open("stories.txt", 'a+')
            save_file.write(string.encode('utf-8'))
            save_file.close()