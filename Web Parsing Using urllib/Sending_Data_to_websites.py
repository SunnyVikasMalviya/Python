# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:01:55 2018

@author: Sunny
"""

import urllib.parse

#The url that we are going to search
#url = "https://www.google.com/search"
url = "https://stackoverflow.com/search"
#url = "https://www.google.com/search?q=test"

#The data that we are going to pass to the server
value = {'q' : "python programming tutorials"}

#Encoding the data
data = urllib.parse.urlencode(value)
#print(data)          #For Debugging

#The data should be encoded in utf-8 format 
data = data.encode('utf-8')
#print(data)          #For Debugging

#Forming the request using Request 
req = urllib.request.Request(url, data)
#print(req)          #For Debugging

#Opening the website and storing the response in a variable
resp = urllib.request.urlopen(req)

#Reading the response
resp_read = resp.read()

#Printing the response
print(resp_read)


'''First I tried with the google website, but it showed an error 405 because \
Google is Smart and don't want any unnecessary loads on its servers just because \
Vikas suddenly decides to crawl their website using python. So I tried with \
Stackoverflow and it responded with loads of data which is basically the \
source code of the page that opened up. '''

"""Question : Now here is the important part. When i tried it with stackoverflow,\
the data that I am sending is encoded and added into the url. When I tried \
crawling and browsing using the same url, the html code that I got from \
crawling and browsing were different(I did inspect the code of the page).\
I know that pages are dynamic and hence the code  can be changing but \
its not about that. The code was a lot different. So here is my question; 
Does urlopen really give the html source code?"""

"""Answer : header modification. Sometimes, websites do not appreciate being \
visited by robots, or they might treat them differently. In the past, most \
websites, if they had a stance at all, would just block programs. Now, the \
prevailing method seems to be to serve different data to programs, so they \
don't realize as easily what has happened, or maybe to share information with\
the developers. Sometimes, they also simply serve the program with limited \ 
data, to keep the load on their servers low. Wikipedia used to outright block \ 
programs, but now they serve a page, same with Google. This is usually a page\ 
that is not what you actually want, so you will need to work around it."""
