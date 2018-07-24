try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import xml.etree.ElementTree as et
import requests
import helper_functions
import techcrunch as tc
import vcnewsdaily as vcnews

if __name__ == '__main__':
    tc.getStories()
    vcnews.getStories()
