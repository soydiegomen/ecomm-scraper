import scrapy

class ClothingstoreSpider(scrapy.Spider):
    name = "common_spider"
    #start_urls = ['https://nataliaa-artwork.company.site/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        filename = f'page-result.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')