try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import xml.etree.ElementTree as et
import requests
import helper_functions

vc_list = ""
geo_list = ""
keyword_list = ""

if __name__ == '__main__':
    
