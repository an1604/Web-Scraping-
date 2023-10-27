import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from marketSpider.items import Product  # Assuming your project is named 'marketSpider'

class ProductSpider(CrawlSpider):
    name = 'product'
    
    allowed_domains = ['shop.hazi-hinam.co.il']
    start_urls = ['https://shop.hazi-hinam.co.il/catalog/products/7749/7290000074245/קרם-קרקר']

    rules = [
        Rule(
            LinkExtractor(allow=r'.*'),
            callback='parse_items',
            follow=True
        )
    ]

    def parse_items(self, response):
        product = Product()
        product['url'] = response.url
        product['title'] = response.css('h2.p1::text').extract_first()
        product['img'] = response.css('img::attr(src)').extract_first()
        product['price'] = response.css('span::text').extract_first()
        product['product_id'] = response.css('p::text').extract_first()
        return product
