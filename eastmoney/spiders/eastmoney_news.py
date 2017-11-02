# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from eastmoney.items import EastmoneyNewsItem

class EastmoneyNewsSpider(CrawlSpider):
    name = 'eastmoney_news'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://wap.eastmoney.com/']
    agent_method = 'ipone'
    custom_settings = {
        'ITEM_PIPELINES':{
            'eastmoney.pipelines.EastmoneyNewsPipeline':1,
        }
    }

    rules = (
        Rule(LinkExtractor(allow=r'http://wap.eastmoney.com/3g/news/.+?shtml?'), callback='parse_items', follow=True),
    )

    def parse_items(self, response):
        i = EastmoneyNewsItem()
        # 抓取标题
        i['title'] = response.xpath('//div[@class="atitle"]/text()').extract_first()
        # 抓取摘要
        i['abstract'] = response.xpath('//div[@class="digest_content"]/text()').extract_first()
        stocks = response.xpath('//*[@id="xgstock"]/a/text()').extract()
        # 关联股票
        i['stocks'] = ''
        if stocks:
            for stock in stocks:
                i['stocks'] += (stock + ',')
        else:
            i['stocks'] = '无'
        # 新闻信息
        news = response.xpath('//article[@id="zwtext"]').extract_first()
        # 提取新闻信息
        pattern = re.compile(r'>([^<]+?)?<', re.S)
        texts = re.findall(pattern, news)
        i['content'] = ''
        for text in texts:
            if '\r\n' not in text or not text :
                i['content'] += text
        i['content'] = re.sub(r'&gt;', '', i['content'])
        i['content'] = re.sub(r'\n', '', i['content'])
        i['url'] = response.url
        yield i
