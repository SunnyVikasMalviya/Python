import bs4 as bs
import urllib.request

sauce = urllib.request('https://pythonprogramming.net/parsememcparseface/').read()
soup = BeautifulSoup(sauce, 'lxml')

'''PARSING TABLES'''
table = soup.table
#or
table = soup.find('table')
#So, now we have the table
#Getting the table rows
table_rows = table.find_all('tr')
#table_rows is a list of all the tr tags
for tr in table_rows:
    #Getting data from table rows
    td = tr.find_all('td')
    #td is a list of all the td tags in a particular table row
    row = [i.text for i in td]
    #row is a list of all the table data in a particular row
    print(row)
#The above will print the  table as a list of lists.

'''PARSING TABLES USING PANDAS'''
import pandas as pd

#read_html() automatically finds all the tables on the webpage and makes a list
#of all the different tables or dataframes present on the table.
dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header=0)
#Printing dataframes
for df in dfs:
    print(df)
#The above will print the table as a dataframe which provides many functions to
#work with the dataframe.
#We can convert it to a list of lists by using the function df.value.to_list()

'''READING THROUGH XML PAGES'''
x_sauce = urllib.request('https://pythonprogramming.net/sitemap.xml').read()
#Sitemaps are maps of all the urls of your website
#XML pages are usually used to represent sitemaps
x_soup = BeautifulSoup(sauce, 'xml')

for url in soup.find_all('loc'):
    #loc is the location tag that is normally used to contain the urls.
    print(url.text)
#This will give all the links present in the python  programming sitemap
