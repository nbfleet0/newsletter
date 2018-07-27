import requests
import urllib2
from lxml import html
import re
import time


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


def infoFromCrunchbase(url):

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
            print(twitter)
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

    # first_info = root.xpath('//*[@id="section-traffic"]/mat-card/div/div/big-values-card/div/div/div[2]/mat-card/span[2]/field-formatter/span')
    # print(first_info)
    print(contents.find('-61.13%'))



    return [twitter, cbrank, funding]


    


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


def score(object):
    # object: [angellist url, crunchbase url, exited?, name, url, acceleration date, exit value, ?, funding]
    if(object[2] == ""): #if comnpany hasnt exited or died
        angelinfo = infoFromAngel(object[0]) # angelinfo: [location, website, twitter, linkedin, funding]
        webresults = numberOfWebResults(object[4])
# //*[@id="section-overview"]/mat-card/div[2]/div/fields-card[3]/div/div/span[4]/field-formatter/link-formatter/a
# //*[@id="section-overview"]/mat-card/div[2]/div/fields-card[2]/div/div/span[6]/field-formatter/link-formatter/a
print(infoFromCrunchbase("https://www.crunchbase.com/organization/segasec-2"))

print(infoFromCrunchbase("https://www.crunchbase.com/organization/workflowy"))

print(infoFromCrunchbase("https://www.crunchbase.com/organization/atrium-lts"))

print(infoFromCrunchbase("https://www.crunchbase.com/organization/starbutter-ai"))
time.sleep(2)
print(infoFromCrunchbase("https://www.crunchbase.com/organization/numoola"))
time.sleep(2)

print(infoFromCrunchbase("https://www.crunchbase.com/organization/workflowy"))
time.sleep(2)

print(infoFromCrunchbase("https://www.crunchbase.com/organization/atrium-lts"))
time.sleep(2)

