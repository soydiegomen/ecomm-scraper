from sqlalchemy import create_engine, Column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Date, Boolean, Numeric, Text
from scrapy.utils.project import get_project_settings

Base = declarative_base()

def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


class Product(Base):
    __tablename__ = "products_product"
    id = Column('id', Integer, primary_key=True)
    brand_id = Column('brand_id', Integer)

    url = Column('url', String(512))
    price = Column('price', Numeric(precision=2))
    discount = Column('discount', Numeric(precision=2))
    final_price = Column('final_price', Numeric(precision=2))
    sku = Column('sku', String(255))
    name = Column('name', String(255))
    description = Column('description', String(255))
    quantity = Column('quantity', Integer)
    order = Column('order', Integer)
    views = Column('views', Integer)
    instagram_likes = Column('instagram_likes', Integer)
    is_active = Column('is_active', Boolean)
    created_at = Column('created_at', Date)
    updated_at = Column('updated_at', Date)