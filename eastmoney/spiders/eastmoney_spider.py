# -*- coding: utf-8 -*-
import scrapy
import re

class EastmoneySpider(scrapy.Spider):
    name = 'eastmoney_spider'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://wap.eastmoney.com/3g/news/article,8,344,1,20171101797350781.shtml']
    agent_method = 'ipone'

    def parse(self, response):
        i = {}
        i['title'] = response.xpath('//div[@class="atitle"]/text()').extract_first()
        i['abstract'] = response.xpath('//div[@class="digest_content"]/text()').extract_first()
        stocks = response.xpath('//*[@id="xgstock"]/a/text()').extract()
        i['stocks'] = ''
        if stocks:
            for stock in stocks:
                i['stocks'] += (stock + ',')
        else:
            i['stocks'] = '无'

        news = response.xpath('//article[@id="zwtext"]').extract_first()

        pattern = re.compile(r'>([^<]+?)?<', re.S)
        texts = re.findall(pattern, news)
        i['content'] = ''
        for text in texts:
            if '\r\n' not in text or not text:
                i['content'] += text

        print(response.url)
