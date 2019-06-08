import scrapy

from myproject.items import Headline


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['http://news.yahoo.co.jp/', ]

    def parse(self, response):
        # print(response.css('ul.topics a::attr("href")').extract())
        for url in response.css('ul.topicsList_main a::attr(href)').re(r'/pickup/\d+$'):
        # for url in response.css('ul.topics a::attr("href")').re(r'/pickup/\d+$'):
            yield scrapy.Request(response.urljoin(url), self.parse_topics)

     #    for url in response.css('ul.topics a::attr("href")').re(r'/pickup/\d+$'):
     #        yield scrapy.Request(response.urljoin(url), self.parse_topics)

    def parse_topics(self, response):
        item = Headline()
        item['title'] = response.css('.tpcNews_title ::text').extract_first()
        item['body'] = response.css('.tpcNews_summary').xpath('string()').extract_first()
        yield item