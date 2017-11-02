""" 
@author:jansonlv
@file: mypipelines.py 
@time: 2017/09/30
@IDE: PyCharm
@project:general_scrapy
使用时继承,需要更改数据库的数据库名等时
重写init
"""

import pymysql
from redis import *
import pymongo
from eastmoney import settings


class GeneralMysqlPipeline(object):
    '''
    mysql管道文件使用配置
    使用时直接继承即可
    '''

    def __init__(self):
        # self.mysql_settings = mysql_settings
        self.mysql_settings = settings.MYSQL_SETTINGS

    # @classmethod
    # def from_clawer(cls, crawler):
        # return cls(mysql_settings=crawler.settings.getdict('MYSQL_SETTINGS'))

    def open_spider(self, spider):
        '''
        spider开启是否运行,开启mysql数据库连接
        :param spider: spider对象
        :return:
        '''
        try:
            self.conn = pymysql.connect(host=self.mysql_settings['host'],
                                        port=self.mysql_settings['port'],
                                        user=self.mysql_settings['user'],
                                        password=self.mysql_settings['password'],
                                        database=self.mysql_settings['database'],
                                        charset=self.mysql_settings['charset'],
                                        )
        except Exception as error:
            print('mysql数据库连接失败:', error)
        self.cs = self.conn.cursor()

    def close_spide(self, spider):
        '''
        spider关闭,mysql关闭连接
        :param spider: spider对象
        :return:
        '''
        self.cs.close()
        self.conn.close()

    def process_item(self, item, spider):
        return item


class GeneralRedisPipeline(object):
    '''
    redis 管道文件
    # 用于分布式,少使用 #
    '''

    def __init__(self, redis_settings):
        self.redis_settings = redis_settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(redis_settings=crawler.settings.getdict('redis_settings'))

    def open_spider(self):
        try:
            self.sr = StrictRedis(host=self.redis_settings['host'],
                                  port=self.redis_settings['port'],
                                  db=self.redis_settings['db'],
                                  password=self.redis_settings['password']
                                  )
        except Exception as error:
            print('redis连接失败:', error)

    def process_item(self, item, spider):
        return item


class GeneralMongoPipeline(object):
    '''
    mongoDB数据库连接
    '''

    def __init__(self, mongo_settings):
        self.mongo_settings = mongo_settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_db=crawler.settings.get('mongo_settings'),
        )

    def open_spider(self, spider):
        try:
            self.client = pymongo.MongoClient(self.mongo_settings['host'], self.mongo_settings['port'])
            self.db = self.client[self.mongo_settings['database']]
        except Exception as error:
            print('MSongoDB连接失败:', error)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        return item