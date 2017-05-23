import requests
from bs4 import BeautifulSoup

class Crawler:

    def getContent(self, url):
        content = requests.get(url).content
        soup = BeautifulSoup(content, "lxml-xml")
        return soup

    def parseContentDescription(self, description):
        for p in description.findAll('p'):
            print p

    def parseContent(self, content):
        for item in content.findAll('item'):
            print item.title.get_text()
            # return
