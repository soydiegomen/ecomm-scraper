import scrapy
import traceback
from scrapy.exceptions import CloseSpider
from ecomm_scraper.items import ProductItem
from ecomm_scraper.spiders.helpers import SpiderHelper


class ProductsSpider(scrapy.Spider):
    name = "products_spider"
    start_urls = None

    def __init__(self, *args, **kwargs):
        try:
            spider_name = self.name
            #TODO Redd JSON file with the details of the url to scrap (url, brandId, etc)
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
                
                price_string = ''
                if(len(price_node) == 1):
                    price_string = price_node[0]
                if(len(price_node) > 1):
                    price_string = price_node[1]
                price_string = price_string.replace('MXN', '')
                price_string = price_string.replace('$', '')
                price_string = price_string.replace(',', '')
                price = price_string.strip()
                
                href = product.css("::attr(href)").extract()
                link_url = ''
                sku = ''
                if(len(href)):
                    link_url = href[0]
                    parts_url = link_url.split('/')
                    #TODO sku must allow Null values
                    sku = parts_url[-1] if len(parts_url) > 0 else ''
                    print(f'sku {sku}')
                
                item = ProductItem()
                item['name'] = product_name
                item['sku'] = sku
                item['price'] = price
                item['description'] = product_name
                item['link_url'] = link_url
                yield item

        except Exception as e:
            print('parse_exception', e)
            print(traceback.format_exc())
            raise CloseSpider('parse_exception')