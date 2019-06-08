import scrapy

from myproject.items import News


class GenDiffSpider(scrapy.Spider):
    name = 'gen_diff'
    allowed_domains = ['www.anime-eupho.com']
    start_urls = ['http://www.anime-eupho.com/news/', ]

    custom_settings = {
        'DEPTH_LIMIT': 1,
    }

    def parse(self, response):

        for li in response.css('ul.newsEntryList li'):
            yield{
                'url': response.urljoin(li.css('a::attr(href)').get()),
                'title': li.css('p.entryTitle::text').get(),
                'date': li.css('p.entryDate::text').get(),
            }

        for link in response.css('div#pager a'):
            if link.css('a::attr(title)').get() in 'next page':
                yield response.follow(link.css('a::attr(href)').get(), callback=self.parse)
