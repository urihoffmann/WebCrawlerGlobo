from crawler import Crawler
# from bs4 import BeautifulSoup

def main():
    crawler = Crawler()
    content = crawler.getContent("http://revistaautoesporte.globo.com/rss/ultimas/feed.xml")
    # content = open('test.xml').read()
    # content = BeautifulSoup(content, "lxml-xml")
    parsedContent = crawler.parseContent(content)
    f = open('feed.json', 'w')
    f.write(parsedContent)

if __name__ == '__main__':
    main()
