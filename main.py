from crawler import Crawler

def main():
    crawler = Crawler()
    content = crawler.getContent("http://revistaautoesporte.globo.com/rss/ultimas/feed.xml")
    crawler.parseContent(content)

if __name__ == '__main__':
    main()
