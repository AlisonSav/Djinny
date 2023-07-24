import scrapy

class RentHouse(scrapy.Spider):
    name = "rent_house"
    start_urls = ['https://djursbo.dk/for-boligsoegende/afdeling/']

    def parse(self, response):
        for link in response.css('div.row a::attr(href)'):
            yield response.follow(link, callback=self.parse_book)

        # for i in range(1, 3):
        #     next_page = f'https://djursbo.dk/for-boligsoegende/afdeling/?p={i}/'
        #     yield response.follow(next_page, callback=self.parse)


