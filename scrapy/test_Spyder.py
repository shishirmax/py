import scrapy

class TestSpider(scrapy.Spider):
    name = 'paths'
    start_urls = [
        'https://www.protiviti.com/US-en/insights',
    ]

    def parse(self, response):
        for path in response.css('div.views-row'):
            yield{
                #'urlpath':path.css('a').xpath('@href').get(),
                'urltitle':path.css('div.field-content::text').get(),
            }
        next_page = response.css('li.pager-next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page,self.parse)