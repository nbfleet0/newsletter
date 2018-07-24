try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import xml.etree.ElementTree as et
import requests
import functions


def getNews():
    # get titles of recent articles from vcnewsdaily
    contents = urlopen("https://feeds.feedburner.com/vcnewsdaily?fmt=xml").read()
    root = et.fromstring(contents)
    channel = root.find('channel')


    for item in channel.iter('item'):
        geo_match = ""
        vc_match = ""
        keyword_match = ""

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
        interest_lvl = checkInterestLvl(article_text)

        
        if (interest_lvl > 1): #more than 2 interesting aspects of an article
            header = ""
            if(geo_match):
                header += "Geography Match: " + geo_match[:-1]
            if(vc_match):
                header += "VC Match: " + vc_match[:-1]
            if(keyword_match):
                header += "Keyword Match: " + keyword_match[:-1]

            string = "\n\n" + header + "\nTitle: " + title + "\nDate: " + date + "\nKeyword: " + vc + "\nArticle Text: " + article_text
            save_file = open("stories.txt", 'a+')
            save_file.write(string)
            save_file.close()

