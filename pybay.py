import urllib
import urllib2


import sys

print str(sys.argv[1])



class get_s(object):

    def search(self,query):
        url = "http://www.google.com"
        query_s = urllib.quote(query)
        request_headers = {
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Referer": "http://thewebsite.com",
            "Connection": "keep-alive"
        }

        request = urllib2.Request(url, headers=request_headers)
        contents = urllib2.urlopen(request).read()
        return contents




