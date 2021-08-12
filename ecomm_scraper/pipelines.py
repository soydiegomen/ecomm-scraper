import logging
import re
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from sqlalchemy.sql.elements import Null
from  sqlalchemy.sql.expression import select
from ecomm_scraper.spiders.models import Product, db_connect


class SaveProductPipeline(object):
    Session = None

    def __init__(self):
        engine = db_connect()
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        print('#Entra a guardar la info de un produto')
        session = self.Session()
        
        product = Product()

        #Fill product
        product.brand_id = 1
        product.url = 'http://localhost.com'
        product.price = 100
        product.discount = 0
        product.final_price = 0
        product.sku = item["price"]
        product.name = item["name"]
        product.description = item["description"]
        product.quantity = 50
        product.order = 1
        product.views = 2
        product.instagram_likes = 3
        product.is_active = True

        """ print('product', product)
        print(item["name"])
        print(item["price"])
        print(item["description"]) """

        try:
            #session.add(product)
            #session.commit()
            print('#Guardo un producto')

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item
