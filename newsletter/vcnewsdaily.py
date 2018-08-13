try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import xml.etree.ElementTree as et
import requests
import helper_functions as helper
import score


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
        interest_array = helper.checkInterestLvl(article_text)
        interest_lvl = len(interest_array)
        #print(interest_array)

        if (interest_lvl > lvl): #more than 2 interesting aspects of an article
            #print("Adding article")

            article_text = article_text.split("<br/><br/>")[0]
            #print(article_text)

            #print(interest_array)

            #buzz_score = score.getBuzzScore([title, article_text])

            for word in interest_array:
                plural = word + "s"
                article_text = article_text.replace(plural, "<b>" + plural + "</b>").replace(word, "<b>" + word + "</b>").replace(word.capitalize(), "<b>" + word.capitalize() + "</b>")


            string = "<tr><td><h2 style='display:inline;'><a href='" + link + "' style='color:#006699;'>" + title \
            + " </h2></br><i style='color:#7f8c8d'>" + ", ".join(interest_array) + "</i></br></br>" + "<p><i style='color:#000000'>" \
            + article_text + "</p></td></tr>"
            save_file = open("./data/stories.txt", 'a+')
            save_file.write(string)
            save_file.close()


