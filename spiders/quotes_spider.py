from pathlib import Path
import scrapy
from ..items import MonitorItem


class QuoteSpider(scrapy.Spider):
    name = "monitor"
    
    def start_requests(self):
      url = "https://www.monitor.co.ug/uganda/news/world"
      yield scrapy.Request(url, callback=self.parse)
    
    def parse(self, response):
          # monitor_item = MonitorItem()
          # # self.logger.info("Parsing %s", response.url)
          # for article in response.css('article.nested-cols'):
          #     monitor_item['headline'] = article.css("h3::text").getall(),
          #     monitor_item['tag'] = article.css("aside.article-metadata span::text").getall()
          #     yield article
          article = response.css('article.nested-cols')
          self.log("title: %s" % response.css(article.css("h3::text")).extract())
          self.log("tag: %s" % response.css(article.css("aside.article-metadata span::text")).extract())        

          #scrapy crawl monitor -o news.json