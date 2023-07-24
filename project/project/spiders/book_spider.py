import scrapy


class BookSpider(scrapy.Spider):
    name = 'yakaboo'
    start_urls = ['https://www.yakaboo.ua/ua/knigi/vibir-chitachiv.html']

    def parse(self, response):
        for link in response.css('div.category-card__poster a::attr(href)'):
            yield response.follow(link, callback=self.parse_book)

        for i in range(1, 3):
            next_page = f'https://www.yakaboo.ua/ua/knigi/vibir-chitachiv.html?p={i}/'
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        yield {
            "name": response.css('div.base-product__title h1::text').get(),
            "author": response.css('div.base-product__author::text').get().strip(),
            "review_count": response.css('span.review-count::text').get(),
            "paper_price": response.css('div.ui-price-display__main span::text').get(),
        }
