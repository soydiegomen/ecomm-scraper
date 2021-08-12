# Scrapy settings for ecomm_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ecomm_scraper'

SPIDER_MODULES = ['ecomm_scraper.spiders']
NEWSPIDER_MODULE = 'ecomm_scraper.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


ITEM_PIPELINES = {
    #'ecomm_scraper.pipelines.SaveProductPipeline': 100
}

CONNECTION_STRING = 'mysql+mysqlconnector://root:root@localhost:8889/storebot_db'


#DMG Unable the logs
LOG_ENABLED=False