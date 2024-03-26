import scrapy
import unidecode
import re

cleanString = lambda x: '' if x is None else unidecode.unidecode(re.sub(r'\s+', ' ', x))

class NytimesSpider(scrapy.Spider):
    name = 'nytimes'
    allowed_domains = ['www.nytimes.com']
    start_urls = ['https://www.nytimes.com/']

    def parse(self, response):
        for section in response.css("section.story-wrapper"):
            for article in section.css("a.css-9mylee"):
                yield {
                    'appears_url': response.url,
                    'title': cleanString(article.css('p::text').get()),
                    'article_url': article.attrib['href'],
                    'summary': cleanString(article.css('p.summary-class::text').get()),
                }
                next_page = article.attrib['href']
                if next_page is not None:
                    yield response.follow(next_page, callback=self.parse_article)

    def parse_article(self, response):
        yield {
            'appears_url': response.url,
            'title': cleanString(response.css("h1[id^='link']::text").get()),
            'authors': cleanString(', '.join(response.css("p.css-4anu6l span[itemprop='name'] a::text").extract())),
            'contents': cleanString(''.join(response.css('section[name="articleBody"] p::text').extract())),
        }

