import scrapy
import logging
from scrapy.loader import ItemLoader
from ecomm_scraper.items import ProductItem
from scrapy.exceptions import CloseSpider

class ProductsSpider(scrapy.Spider):
    name = "products_spider"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        try:
            quotes = response.css('div.quote')

            for quote in quotes:
                item = ProductItem()
                item['name'] = quote.css('.author::text').get()
                item['description'] = quote.css('.text::text').get()
                yield item
        except:
            raise CloseSpider('bandwidth_exceeded')