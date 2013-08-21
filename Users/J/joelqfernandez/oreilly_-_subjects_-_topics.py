#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import scraperwiki

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from scrapy.item import Item, Field
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import MapCompose, TakeFirst

from scrapy.conf import settings
from scrapy import log

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.http import Request
from urlparse import urljoin


class TopicsSpider(BaseSpider):
    name = 'topics'
    allowed_domains = [ 'shop.oreilly.com' ]
    start_urls = [ 'https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=htmltable&name=oreilly_-_subjects_1&query=select%20url%20from%20%60subject%60' ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        subjects = hxs.select('//tr/td[1]/text()').extract()
        for subject in subjects:
            yield Request(subject, self.parseTopic)
        
    def parseTopic(self, response):
        hxs = HtmlXPathSelector(response)
        topics = hxs.select('//div[@class="navLeft2Off"]')
        items = []
        for topic in topics:
            loader = WebsiteLoader(selector=topic)
            #loader.add_xpath('name', 'a/text()')
            loader.add_xpath('url', 'concat("http://shop.oreilly.com", a/@href)' )
            loader.add_xpath('description', 'string()')
            items.append(loader.load_item())
            # yield Request(topicLink, self.parsePages)
        return items            

class Website(Item):
    #name = Field()
    url = Field()
    description = Field()

class WebsiteLoader(XPathItemLoader):
    default_item_class = Website
    default_input_processor = MapCompose(lambda x: x.strip())
    default_output_processor = TakeFirst()

class SWPipeline(object):
    """A pipeline for saving to the Scraperwiki datastore"""
    def __init__(self):
        self.buffer = 20
        self.data = []
        self.counter = 0
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def process_item(self, item, spider):
        self.data.append(dict(item))
        if len(self.data) >= self.buffer:
            self.write_data(spider)
        return item

    def spider_closed(self, spider):
        if self.data:
            self.write_data(spider)
    
    def write_data(self, spider):
        unique_keys = spider.settings.get('SW_UNIQUE_KEYS', ['id'])
        scraperwiki.sqlite.save(table_name=spider.name, unique_keys=unique_keys, data=self.data)
        self.data = []

def run_spider(spider, settings):
    """Run a spider with given settings"""
    from scrapy.crawler import CrawlerProcess
    crawler = CrawlerProcess(settings)
    crawler.install()
    crawler.configure()
    crawler.crawl(spider)
    log.start()
    crawler.start()

def main():
    import sys
    sys.path.append("/home/scriptrunner/")
    print sys.path
    options = {
        'SW_SAVE_BUFFER': 30,
        'SW_UNIQUE_KEYS': ['url'],
        'ITEM_PIPELINES': ['script.SWPipeline'],
    }

    settings.overrides.update(options)
        
    run_spider(TopicsSpider(), settings)

if __name__ == 'scraper':
    main()