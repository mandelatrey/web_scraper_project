from pathlib import Path
import scrapy

class QuoteSpider(scrapy.Spider):
    name = "newSpider2"
    start_urls = ["https://www.monitor.co.ug/uganda/news/world"]
         
    def parse(self, response):
          for article in response.css('article.nested-cols'):
                
            yield {
              "headline": article.css("h3::text").getall(),
              "tag": article.css("aside.article-metadata span::text").getall()
            }
            pages = response.css("ul.categories-nav_sub li a")
            
            response_pages = yield from response.follow_all(pages, callback=self.parse)
            response_pages