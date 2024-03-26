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

