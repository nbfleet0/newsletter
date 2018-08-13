import xml.etree.ElementTree as et
import requests
import helper_functions as helper
from lxml import html
import datetime
import score
import time

def getStories(lvl):
    page = requests.get("http://fortune.com/newsletter/termsheet/?scrape=1")
    root = html.fromstring(page.text)
    tree = root.getroottree()

    xpath = '/html/body/custom/table[1]/tr[2]/td/table/tr[10]/td/table/tr/td/table/tr[1]/td/p['
    i = 0
    linkcheck = root.xpath(xpath + str(i) + ']')
    while not linkcheck:
        i += 1
        #print(i)
        #print(linkcheck)
        time.sleep(1)
        linkcheck = root.xpath(xpath + str(i) + ']')

    for i in root.xpath(xpath + str(i) + ']'):
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        link = i.xpath('a/@href')[0]
        article_text = "".join(i.itertext())


        interest_array = helper.checkInterestLvl(article_text)
        interest_lvl = len(interest_array)
        #print(interest_array)

        if (interest_lvl > lvl): #more than 2 interesting aspects of an article
            #print("Adding article")

            # check for duplicates
            duplicate = False
            search_file = open("./data/stories.txt", 'r')
            lines = search_file.readlines()
            search_file.close()

            article_query = article_text.split('\n', 1)[0].encode('utf-8')

            #Check for duplicity because the RSS Feed is only updated weekly
            for line in lines:
                if article_query in line:
                    duplicate = true

            if duplicate is False:

                article_text = article_text.split("<br/><br/>")[0]
                #print(article_text)

                title = article_text.split(",")[0] #company name

                #buzz_score = score.getBuzzScore([title, article_text])

                for word in interest_array:
                    bold = "<b>" + word + "</b>"
                    article_text = article_text.replace(word, bold).replace(word.capitalize(), "<b>" + word.capitalize() + "</b>")

                string = "<tr><td><h2 style='display:inline;'><a href='" + link + "' style='color:#006699;'>" + title \
                 + " </h2></br><i style='color:#7f8c8d'>" + ", ".join(interest_array) + "</i></br></br>" + "<p><i style='color:#000000'>" \
                 + article_text + "</p></td></tr>"
                save_file = open("./data/stories.txt", 'a+')
                save_file.write(string.encode('utf-8'))
                save_file.close()