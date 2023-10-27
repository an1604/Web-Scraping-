# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    img = scrapy.Field()
    price = scrapy.Field()
    product_id = scrapy.Field()
