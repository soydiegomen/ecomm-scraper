# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class ProductItem(Item):
    name = Field()
    sku = Field()
    price = Field()
    description = Field()
    link_url = Field()
    description = Field()