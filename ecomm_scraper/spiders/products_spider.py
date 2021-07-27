import scrapy
import logging
from scrapy.loader import ItemLoader
from ecomm_scraper.items import ProductItem

class ProductsSpider(scrapy.Spider):
    name = "products_spider"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        products = response.css('.grid-product__wrap-inner')
        logging.info("#Items4 {}".format(len(products)) )
        
        for product in products:
            loader = ItemLoader(item=ProductItem(), selector=product)
            loader.add_css('name', '.grid-product__title-inner::text')
            loader.add_css('price', '.grid-product__price-value::text')
            yield loader.load_item()