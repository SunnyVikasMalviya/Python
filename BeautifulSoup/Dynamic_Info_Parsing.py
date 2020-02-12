import bs4 as bs
import urllib.request

#Loading the source code and the soup
source = urllib.request("c").read()
soup = bs.BeautifulSoup(source, 'lxml')

'''
Source codes have javascript tags that can dynamically update other elements in
the document through element_name.getElementById.innerHtml().
Now, if you access this code using a client like a browser, it shows the
dynamically updated information. But if you try to access the same data using
web parsing, you will get the data without updation. So, in order to get the
updated data, we need to mimic a client, since its the client who runs the
script tags and not the server and BeautifulSoup doesn't mimic a client.
We will be needing PyQT for this purpose.
'''

#The below code gets the un-updated data
js_test = soup.find('p', class_='jstest')
print(js_test)

#The below code gets the updated data
import sys      #Because PyQt4 needs some system arguments to function
from PyQt4.QtGui import QApplication    #Helps make an application
from PyQt4.QtCore import QUrl           #Helps open the url
from PyQt4.QtWebKit import QWebPage     #Helps load the webpage, act like a client and run the javascript code

class Client(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()


url = 'http://pythonprogramming.net/parsememeparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test)

#USING DRYSCRAPE FOR SAME PURPOSE
import dryscrape

sess = dryscrape.Session()
sess.visit('https://pythonprogramming.net/parsememcparseface/')
source = sess.body()
soup = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test)


