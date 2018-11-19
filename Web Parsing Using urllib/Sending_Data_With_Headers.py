# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:59:29 2018

@author: Sunny
"""

import urllib.parse

#First we have the url
url = "https://www.google.com/search?q=test"

#I create a new header and assign it the user agent of an internet explorer
#user 
new_header = {}
new_header['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 \
(KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

#Now, I make a request
'''I call the Request() with url and header. Although the 2nd argument in \
Request is data, here I am explicitly assigning the formal argument 'headers'\
the value of new_header '''
req = urllib.request.Request(url, headers = new_header)
resp = urllib.request.urlopen(req)

#Reading the response
resp_read = resp.read()
print(resp_read)

'''So here is the thing; Google can differentiate between a crawler and a \
human till the crawler is not using a header with a user-agent which makes\
it look like a real person to the servers. And the reason why I am saying this \
is that Google responded when I tried crawling it with an internet explorer\
user-agent, while it didn't respond previously when I tried without the header.'''