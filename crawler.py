import requests
from bs4 import BeautifulSoup
import simplejson as json
class Crawler:

    def getContent(self, url):
        content = requests.get(url).content
        soup = BeautifulSoup(content, "lxml-xml")
        return soup

    def parseDescritionP(self, p):
        p = BeautifulSoup(p.get_text(), "lxml")
        if len(p.html.body.p.get_text()) > 1:
            return {
                'type': 'text',
                'content': p.html.body.p.get_text()
            }
        else:
            return None

    def parseDescritionDivImg(self, div):
        return {
            'type': 'image',
            'content': div.img['src']
        }


    def parseDescritionDivUl(self, div):
        content = []
        for li in div.ul.findAll('li'):
            content.append(li.a['href'])
        return {
            'type': 'links',
            'content': content
        }

    def parseDescritionDiv(self, div):
        if div.find('img'):
            return self.parseDescritionDivImg(div)
        elif div.find('ul'):
            return self.parseDescritionDivUl(div)
        else:
            return None

    def parseContentDescription(self, description):
        feedDescription = []
        description = BeautifulSoup(description, "lxml")

        for child in description.descendants:
            if child.name == 'p':
                feedP = self.parseDescritionP(child)
                if feedP:
                    feedDescription.append(feedP)
            elif child.name == 'div':
                feedDiv = self.parseDescritionDiv(child)
                if feedDiv:
                    feedDescription.append(feedDiv)
        return feedDescription


    def parseContent(self, content):
        feed = {
            'feed' : [],
        }
        for item in content.findAll('item'):
            feedItem = {}
            feedItem['title'] = item.title.get_text()
            feedItem['link'] = item.link.get_text()
            feedItem['description'] = self.parseContentDescription(item.description.get_text())
            feed['feed'].append(feedItem)
        return json.dumps(feed)
