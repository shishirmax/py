# -*- coding: utf-8 -*-
import scrapy


class ProtivitiSpider(scrapy.Spider):
    name = 'protiviti'
    allowed_domains = ['protiviti.com']
    start_urls = ['http://protiviti.com/']

    def start_requests(self):
        urls = [
            'https://www.protiviti.com/US-en/insights'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'protiviti-%s.html' % page
        with open(filename,'wb') as f:
            f.write(response.body)
            self.log('Saved file %s' % filename)
