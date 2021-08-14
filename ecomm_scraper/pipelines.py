import traceback
from sqlalchemy.orm import sessionmaker
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
        product.url = item["link_url"]
        product.price = float(item["price"])
        product.discount = 0
        product.final_price = float(item["price"])
        product.sku = item["sku"]
        product.name = item["name"]
        product.description = item["description"]
        product.quantity = 0
        product.order = 1
        product.views = 0
        product.instagram_likes = 0
        product.is_active = True
        #print('product', product)

        try:
            session.add(product)
            session.commit()
            print('#Guardo un producto')

        except Exception as e:
            print('parse_exception', e)
            print(traceback.format_exc())
            session.rollback()
            raise

        finally:
            session.close()

        return item
