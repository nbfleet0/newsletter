import requests
import urllib2
from lxml import html
import re


def infoFromAngel(url):

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    req = urllib2.Request(url, headers=hdr)
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
    contents = page.read()
    root = html.fromstring(contents)

    location = root.xpath('//*[@id="root"]/div[4]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/span/span/a[1]')[0]
    location = "".join(location.itertext())

    website = root.xpath('//*[@id="root"]/div[4]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/span/span[1]/a')[0]
    website = "".join(website.itertext())

    twitter = root.xpath('//*[@id="root"]/div[4]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/span/span[2]/a/@href')[0]
    twitter = re.sub(r'.*/', '/', twitter)[1:]

    linkedin = root.xpath('//*[@id="root"]/div[4]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/span/span[4]/a/@href')[0]
    linkedin = re.sub(r'.*/', '/', linkedin)[1:]

    funding = root.xpath('//*[@id="root"]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[3]/div/div[1]/ul/li/div/div/div[1]/div[2]')[0]
    funding = "".join(funding.itertext())
    funding = funding.replace('\n', '')

    # ceo = root.xpath('//*[@id="root"]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div/ul/li/div/div/div[2]/div[1]/a')[0]
    # ceo = "".join(ceo.itertext())

    return [location, website, twitter, linkedin, funding]



def numberOfWebResults(website):
    url = "https://www.google.com/search?q=%22" + website + "%22&hl=en"
    page = requests.get(url)
    root = html.fromstring(page.text)
    results = root.xpath('//*[@id="resultStats"]')[0]   
    text = "".join(results.itertext())
    number = re.sub('[^0-9]','', text)
    return number


def numberOfTwitterFollowers(username):
    url = "https://twitter.com/" + username
    page = requests.get(url)
    root = html.fromstring(page.text)
    results = root.xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[3]')[0]
    text = "".join(results.itertext())
    return text

def totalTweetLikes(username):
    url = "https://twitter.com/" + username
    page = requests.get(url)
    root = html.fromstring(page.text)
    results = root.xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[4]/a/span[3]')[0]
    text = "".join(results.itertext())
    return text



    

print(infoFromAngel("https://angel.co/adtuo"))
