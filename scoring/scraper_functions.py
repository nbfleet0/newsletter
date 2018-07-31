import requests
import urllib2
from lxml import html
import re
import time

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}

def infoFromAngel(url):

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


def infoFromCrunchbase(url):

    # print("getting crunchbase info")

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



    twitter = ""
    for m in re.finditer('twitter.com/', contents): #search for twitter handle
        if contents.find("crunchbase", m.start()) != m.end(): #find crunchbase starting at 'twitter.com' start, compare starting position to ending of 'twitter.com'
            end = contents.find('"', m.start())
            twitter = contents[m.start():end]
            # print(twitter)
            break

    pos = contents.find("/search/organization.companies/field/organizations/rank_org_company/")
    end = contents.find('"',pos+68) #70 characters in '"/search/organization.companies/field/organizations/rank_org_company/"'
    cbrank = contents[pos+68:end]
    # print(cbrank)
            
    pre_pos = contents.find("/search/funding_rounds/field/organizations/funding_total/")
    pos = contents.find('">', pre_pos)
    end = contents.find('<',pos) 
    funding = contents[pos+2:end].replace(" ", "") #2 characters in '">'
    if (end - pos) == 0:
        funding = ""



    return [twitter, cbrank, funding]


    
#alexa
def getAlexaRankings(website):

    url = "https://www.alexa.com/siteinfo/" + website
    # print(url)

    req = urllib2.Request(url, headers=hdr)
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
    contents = page.read()
    root = html.fromstring(contents)

    
    rank = root.xpath('//*[@id="traffic-rank-content"]/div/span[2]/div[1]/span/span/div/strong')[0]
    rank = "".join(rank.itertext())
    rank = re.sub('[^0-9]','', rank)
    if(rank == ""):
        return [0,0,0,0,0,0]
    rank = int(rank)


    rank_increase = root.xpath('//*[@id="traffic-rank-content"]/div/span[2]/div[1]/span/span/div/span')[0]
    rank_increase = "".join(rank_increase.itertext())
    rank_increase = re.sub('[^0-9]','', rank_increase)
    rank_increase = float(rank_increase)


    inbound_links = root.xpath('//*[@id="linksin-panel-content"]/div[1]/span/div/span')[0]
    inbound_links = "".join(inbound_links.itertext())
    inbound_links = re.sub('[^0-9]','', inbound_links)
    inbound_links = int(inbound_links)

    home_geo = root.xpath('//*[@id="traffic-rank-content"]/div/span[2]/div[2]/span/span/h4/a')
    if not home_geo:
        home_geo = "None"
    else:
        home_geo = home_geo[0]
        home_geo = "".join(home_geo.itertext())

    bounce_rate = root.xpath('//*[@id="engagement-content"]/span[1]/span/span/div/strong')[0]
    bounce_rate = "".join(bounce_rate.itertext())
    bounce_rate = ''.join(bounce_rate.split())
    bounce_rate = bounce_rate.replace('%','')
    if(bounce_rate == "-"):
        bounce_rate = 100
    bounce_rate = float(bounce_rate)

    search_increase = root.xpath('//*[@id="keyword-content"]/span[1]/span/span/div/span')
    if not search_increase:
        search_increase = 0
    else:
        search_increase = search_increase[0]
        search_increase = "".join(search_increase.itertext())
        search_increase = ''.join(search_increase.split())
        search_increase = search_increase.replace('%', '')
        if search_increase == "":
            search_increase = 0
        else:
            search_increase = float(search_increase)


    return_obj = [rank, rank_increase, inbound_links, home_geo, bounce_rate, search_increase]
    
    return return_obj



def numberOfWebResults(website):
    website = website.replace('https://', '').replace('http://', '').replace('www', '').replace('/', '')
    url = "https://www.google.com/search?q=%22" + website + "%22&hl=en"
    # print(url)
    page = requests.get(url)
    root = html.fromstring(page.text)
    results = root.xpath('//*[@id="resultStats"]')[0]   
    text = "".join(results.itertext())
    number = re.sub('[^0-9]','', text)
    number = float(number)
    return number


def numberOfTwitterFollowers(username):
    # username.replace('https://twitter.com/')
    url = "https://" + username
    print(url)
    page = requests.get(url)
    root = html.fromstring(page.text)
    results = root.xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[3]')
    # print(results)
    if not results:
        return 0
    results = results[0]
    text = "".join(results.itertext())
    modifier = 1
    if(text.find('K') != -1):
        modifier = 1000
        text = text.replace('K', '')
    elif(text.find('M') != -1):
        modifer = 1000000
        text = text.replace('M', '')
    else:
        modifer = 1
    text = text.replace(",", "")
    number = float(text)
    number = number*modifer

    return number

# def totalTweetLikes(username):
#     url = "https://twitter.com/" + username
#     page = requests.get(url)
#     root = html.fromstring(page.text)
#     results = root.xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[4]/a/span[3]')[0]
#     text = "".join(results.itertext())
#     text.replace(',', '')
#     return text

