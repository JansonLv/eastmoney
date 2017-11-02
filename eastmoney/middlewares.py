# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from eastmoney import settings
from urllib.parse import urlparse

class EastmoneySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

"""
class RandomUserAgent1(object):
    '''
    产生随机user-agent
    智能在settings中设置pc端还是移动端,效率低
    '''
    def __init__(self):
        self.agent_method = settings.AGENT_METHOD
        if self.agent_method == 'pc':
            self.user_agents = settings.PC_USER_AGENT
        elif self.agent_method == 'ipone':
            self.user_agents = settings.IPHONE_USER_AGENT

    def process_request(self, request, spider):
        '''
        随机取请求user_agents
        :param request:
        :param spider:
        :return:
        '''
        request.headers['User-Agent'] = random.choice(self.user_agents)
        print('*******')
        print(request.headers)

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
class MyRandomUserAgent2(UserAgentMiddleware):
    '''
    继承框架的类,
    只能在settings中设置
    '''
    @classmethod
    def from_crawler(cls, crawler):
        # 得到的竟然是一个对象
        # 解决,因为加了一个cls,所以返回的是一个类对象
        method = crawler.settings['AGENT_METHOD']
        # 判断agent是电脑还是移动端
        if method == 'ipone':
            o = cls(crawler.settings['IPHONE_USER_AGENT'])
        else:
            o = cls(crawler.settings['PC_USER_AGENT'])
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    # def spider_opened(self, spider):
    # 如果在spider自定义一个user_agent则使用user_agent
    #     self.user_agent = getattr(spider, 'user_agent', self.user_agent)

    def process_request(self, request, spider):
        if self.user_agent:
            request.headers['User-Agent'] = random.choice(self.user_agent)
"""

class MyRandomUserAgent(object):
    '''
    随机获取user_agent中间件
    1.在spider中定义一个agent_method变量,未定义则为pc端,定义为ipone则为手机端
    2.在settings中DOWNLOADER_MIDDLEWARES中添加'eastmoney.middlewares.MyRandomUserAgent': 500,
    '''

    def __init__(self):
        self.pc_user_agent = settings.PC_USER_AGENT
        self.ipone_user_agent = settings.IPHONE_USER_AGENT

    def process_request(self, request, spider):
        # 获取主机地址
        host = urlparse(request.url).netloc
        request.headers['Host'] = host
        # 获取随机请求头
        agent_method = getattr(spider, 'agent_method', 'pc')
        if agent_method == 'ipone':
            request.headers['User-Agent'] = random.choice(self.ipone_user_agent)
        else:
            request.headers['User-Agent'] = random.choice(self.pc_user_agent)
        # print('请求中间件--------------------')


class RandomProxy(object):
    '''
    代理未调试
    随机代理池
    '''
    def __init__(self, ip_list, proxy_switch):
        self.ip_list, self.switch = ip_list, proxy_switch

    def process_request(self, request, spider):
        '''
        在请求上加上代理
        :param request:
        :param spider:
        :return:
        '''
        if self.switch == True:
            proxy = random.choice(self.ip_list)
            request.meta['proxy'] = proxy