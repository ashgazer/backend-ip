import urllib
import urllib2


import sys

#print str(sys.argv[1])
#https://thepiratebayproxylist.net/


class get_s(object):


    def __init__(self,url= 'https://unblocktpb.pro/search/{0}/0/7/0'):
        self.url = url

    def search(self,query):
        query_s = urllib.quote(query)
        request_headers = {
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Referer": "http://thewebsite.com",
            "Connection": "keep-alive"
        }

        request = urllib2.Request(self.url.format(query_s), headers=request_headers)
        contents = urllib2.urlopen(request).read()
        return self.__clean_data(contents)

    def __clean_data(self,data):
        start = data.find("<table")
        finished = data.find("</table",start)
        return data[start:finished+8]


#url= 'https://unblocktpb.pro/search/{0}/0/7/0'

#man = get_s(url)

#site_data = man.search(str(sys.argv[1]))

#print(site_data)
