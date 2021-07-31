import scrapy
import os
from scrapy.loader import ItemLoader
from scrapy.exceptions import CloseSpider
from ecomm_scraper.items import ProductItem
from ecomm_scraper.spiders.helpers import SpiderHelper


class ProductsSpider(scrapy.Spider):
    name = "products_spider"
    start_urls = None

    def __init__(self, *args, **kwargs):
        try:
            spider_name = self.name
            self.start_urls = SpiderHelper().get_start_url(spider_name)
        except:
            raise CloseSpider('get_start_url_exception')

    def parse(self, response):
        try:
            quotes = response.css('div.quote')

            for quote in quotes:
                item = ProductItem()
                item['name'] = quote.css('.author::text').get()
                item['description'] = quote.css('.text::text').get()
                yield item
        except:
            raise CloseSpider('parse_exception')