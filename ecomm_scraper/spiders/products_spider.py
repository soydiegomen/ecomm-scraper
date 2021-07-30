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
            print('#Inicia el spider de los productos')
            quotes = response.css('div.quote')

            for quote in quotes:
                print('#Obtiene la info de una quote')
                loader = ItemLoader(item=ProductItem(), selector=quote)
                loader.add_css('name', '.author::text')
                loader.add_css('description', '.text::text')
                yield loader.load_item()
        except:
            raise CloseSpider('bandwidth_exceeded')