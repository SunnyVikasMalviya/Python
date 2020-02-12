import bs4 as bs
import urllib.request


'''Getting Ugly Source(Sauce) Code'''
#Read the source code of the online page
#The sauce is just the messy source code of the page with all the \n, \t and
#many other extra things present in it.
sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
#print(sauce)


'''Getting Pretty Source(Soup) Code'''
#To get away form these extra things we use a BeautifulSoup() which makes the
#whole code look a little more prettier.
#lxml is the parser which is explicitly called
#we can also call html5lib
#Soup is what the source code looks like in the browser.
soup = bs.BeautifulSoup(sauce, 'lxml')
#print(soup)


'''Getting different elements of the document'''
#print(soup.title)  #For title of the document
#print(soup.p)      #For the first paragraph element in the document
#print(soup.find_all('p')) #Finds all the paragraph tags


'''Getting properties of html tags'''
#print(soup.div.name)   #Returns the name of the tag i.e. div
#print(soup.p.string)   #Returns the content of the first p tag in the document
                        #and it will not get data if there are child tags
                        #inside the given tag
#print(soup.span.text)  #Returns the content even from the child tags inside
                        #the given tag


for paragraph in soup.find_all('p'):
    print(paragraph.text)


'''Getting all the text from the document(some texts are also written in div tags
and parsing through just the p tags won't help much)'''
print(soup.get_text())


'''Getting url from the document'''
for url in soup.find_all('a'):
    print("""
            {}
            {}
            {}""".format(url, url.text, url.get('href')))
#This prints the whole tag, the text associated with the link and the link itself.


'''Getting a specific part of the whole code'''
nav = soup.nav
#The nav variable contains only the code inside the nav tags in the soup.
#The nav variable is itself a beautiful soup object/variable, hence functions
#like find all can be used on nav.

'''Getting link to other pages in the site from the nav'''
for url in nav.find_all('a') :
    print(url.get('href'))
#find_all and get can be applied to nav as it is also a beautiful soup object.

#Similarly
body = soup.body    #extracts just the source code inside the body tags
for paragraph in body.find_all('p'):
    print(paragraph.text)

'''Getting text not present in body tags'''
#Sometimes body tags are not used to display the website contentsd.
#So, for instance if div tag is used for displaying the website content,
for div in soup.find_all('div', class_='body'):
    print(div.text)
#The class_ parameter in the find_all function helps show only the div tags
#that has a class name as body. We can also use id, value, name etc.
