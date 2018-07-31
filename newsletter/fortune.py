import xml.etree.ElementTree as et
import requests
import helper_functions as helper
from lxml import html
import datetime


def getStories(lvl):
    page = requests.get("http://fortune.com/newsletter/termsheet/?scrape=1")
    root = html.fromstring(page.text)
    tree = root.getroottree()

    for i in root.xpath('/html/body/custom/table[1]/tr[2]/td/table/tr[10]/td/table/tr/td/table/tr[1]/td/p'):
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        link = i.xpath('a/@href')[0]
        article_text = "".join(i.itertext())


        interest_lvl = helper.checkInterestLvl(article_text)

        if (interest_lvl > lvl): #more than 2 interesting aspects of an article
            print("Adding article")

            # check for duplicates
            duplicate = False
            search_file = open("stories.txt", 'r')
            lines = search_file.readlines()
            search_file.close()

            article_query = article_text.split('\n', 1)[0].encode('utf-8')

            for i, line in enumerate(lines):
                if article_query in line:
                    duplicate = true

            if(duplicate == False):

                article_text = article_text.split("<br/><br/>About")[0]
                print(article_text)

                string = "\n\n<b><a href='" + link + "'>" + title + "</a></b>\n\n" + article_text
                save_file = open("stories.txt", 'a+')
                save_file.write(string.encode('utf-8'))
                save_file.close()