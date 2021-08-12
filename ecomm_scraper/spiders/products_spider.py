import scrapy
import traceback
import sys
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
            #locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
            #TODO Revisar porque no esta obteniendo la info de los productos

            productos = response.css('.product-card')
            #productos = response.css('.grid__item')
            for product in productos:
                product_name = product.css('.product-card__name::text').get()

                price_node = product.css('.product-card__price::text').getall()
                #El precio esta en la posición 1
                if(len(price_node) > 0):
                    price_string = price_node[1]
                    price_string = price_string.replace('MXN', '')
                    price_string = price_string.replace('$', '')
                    price_string = price_string.replace(',', '')
                    price = price_string.strip()
                    print(price)
                
                href = product.css("::attr(href)").extract()
                if(len(href)):
                    link_url = href[0]
                    print('#href final ', link_url)

            """ for quote in quotes:
                item = ProductItem()
                item['name'] = quote.css('.product-card__name::text').get()
                print('#cards', item['name'])
                #item['description'] = quote.css('.text::text').get()
                item['description'] = quote.css('.product-card__price::text').get()
                item['price'] = quote.css('.product-card__price span::text').get()
                yield item """
        except Exception as e:
            print('Exception happend', e)
            print(traceback.format_exc())
            raise CloseSpider('parse_exception')