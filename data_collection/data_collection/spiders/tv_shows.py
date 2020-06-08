# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestShowsSpider(CrawlSpider):
    name = 'tv_shows'
    allowed_domains = ['theverge.com']
    start_urls = ['http://www.theverge.com/tv/archives/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r"//div[contains(@class ,'c-compact-river__entry')]/div[1]/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=r"//a[@class='c-pagination__next c-pagination__link p-button']")),
    )

    def parse_item(self, response):
        # print(response.body)
        yield {
            'title': response.xpath("//h1[@class='c-page-title']/text()").get(),
            'date': response.xpath("//span[@class='c-byline__item']/time/text()").get(),
            'author': response.xpath("//span[@class='c-byline__author-name']/text()").get(),
            'text': response.xpath("//div[@class='c-entry-content ']/p/text()").getall()}