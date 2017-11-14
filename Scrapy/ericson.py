import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.ericsson.com/ourportfolio/a-to-z']

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}
            console.log(title)

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
