import urllib.request
import re

url = 'http://pythonprogramming.net/parse-website-using-regular-expressions-urllib/'

resp = urllib.request.urlopen(url)
respData = str(resp.read())

paragraphs = re.findall(r'<p>(.*?)</p>', respData)

for para in paragraphs :
    print(para)
