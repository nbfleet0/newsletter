try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import xml.etree.ElementTree as et
import requests

# get titles of recent articles from vcnewsdaily
contents = urlopen("https://feeds.feedburner.com/vcnewsdaily?fmt=xml").read()
root = et.fromstring(contents)
channel = root.find('channel')

# open files
# vc
text_file = open("vclist.txt", "r")
vc_list = text_file.read().split(',')
text_file.close()
# geographies
text_file = open("geographies.txt", "r")
geo_list = text_file.read().split(',')
text_file.close()
# keywords
text_file = open("keywords.txt", "r")
keyword_list = text_file.read().split(',')
text_file.close()

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

    # check for interesting geographies
    interest_lvl = 0

    for geo in geo_list:
        if geo.lower() in article_text.lower():
            geo_match += (geo + ", ")
            interest_lvl += 1

    # check for interesting vc's
    for vc in vc_list:
        if vc.lower() in article_text.lower():
            vc_match += (vc + ", ")
            interest_lvl += 1

    # check for interesting keywords
    for keyword in keyword_list:
        if keyword.lower() in article_text.lower():
            keyword_match += (keyword + ", ")
            interest_lvl += 1

    print(interest_lvl)
    print(geo_match)
    print(vc_match)
    print(keyword_match)
    
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

        print('KEEP THIS ARTICLE KEEP THIS ARTICLE KEEP THIS ARTICLE KEEP THIS ARTICLE KEEP THIS ARTICLE')
