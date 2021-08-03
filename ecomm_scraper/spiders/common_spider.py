import scrapy
from scrapy.exceptions import CloseSpider
from ecomm_scraper.spiders.helpers import SpiderHelper

class ClothingstoreSpider(scrapy.Spider):
    name = 'common_spider'
    start_urls = None
    pages_download = 'pages_download'

    def __init__(self, *args, **kwargs):
        try:
            pages_download = self.pages_download
            self.start_urls = SpiderHelper().get_start_url(pages_download)
            print('#to_download', self.start_urls)
        except:
            raise CloseSpider('get_start_url_exception')

    def parse(self, response):
        filename = f'public_html/tienda-uno.html'
        with open(filename, 'wb') as f:
            f.write(response.body)