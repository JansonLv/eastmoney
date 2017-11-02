# -*- coding: utf-8 -*-

# Scrapy settings for eastmoney project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'eastmoney'

SPIDER_MODULES = ['eastmoney.spiders']
NEWSPIDER_MODULE = 'eastmoney.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT =     'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',

# Obey robots.txt rules
# 是否遵循robots规则
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 将由Scrapy下载程序执行的并发（即同时）请求的最大数量
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载器在从同一网站下载连续页面之前应等待的时间（以秒为单位）
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 任何单个域执行的并发（即同时）请求的最大数量。
CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 将对任何单个IP执行的并发（即同时）请求的最大数量
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    # 请求的发起网页
    # 'Refer': '',
    # 主机地址
    # 'Host':'',

}

# Enable or disable spider moulding_board
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# 包含在您的项目中启用的爬虫中间件的字典及其顺序
# SPIDER_MIDDLEWARES = {
#    'general_scrapy.moulding_board.GeneralScrapySpiderMiddleware': 543,
# }

# Enable or disable downloader moulding_board
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# 包含在您的项目中启用的下载器中间件及其顺序的字典。
DOWNLOADER_MIDDLEWARES = {
    # 'general_scrapy.general_scrapy.moulding_board.MyCustomDownloaderMiddleware': 543,
    # 随机请求头池,需要设置settings
    'eastmoney.middlewares.MyRandomUserAgent': 500,
    # 随机代理池,需要设置settings的proxy_switch和IP_PROXY
    # 'eastmoney.middlewares.RandomProxy': 400,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# 包含项目中启用的扩展名及其顺序的字典。
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# 包含要使用的项目管道及其顺序的字典。
#ITEM_PIPELINES = {
#    'general_scrapy.pipelines.GeneralScrapyPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 指定过滤器路径
# DUPEFILTER_CLASS = 'genderal_scrapy.myCustomFilter.URLFilter'         # 基于url算法
# DUPEFILTER_CLASS = 'eastmoney.moulding_board.myCustomFilter.URLSha1Filter'     # 基于sha1算法
DUPEFILTER_CLASS = 'eastmoney.moulding_board.myCustomFilter.URLBloomFilter'    # 基于布隆算法



# pc or ipone
# 非ipone即为pc
AGENT_METHOD = 'pc'

PC_USER_AGENT = (
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)',
    'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11',
    'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
    'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
    'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
    'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
    'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;',
    'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',

    # 老式的请求头,用到不多,但是可以方便直接获取数据
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0) ",
 )

# 移动端
IPHONE_USER_AGENT = (
    'Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5',
    'Mozilla/5.0(iPod;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5',
    'Mozilla/5.0(iPad;U;CPUOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5',
    'Mozilla/5.0(Linux;U;Android2.3.7;en-us;NexusOneBuild/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1',
    'MQQBrowser/26Mozilla/5.0(Linux;U;Android2.3.7;zh-cn;MB200Build/GRJ22;CyanogenMod-7)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1',
    'Opera/9.80(Android2.3.4;Linux;OperaMobi/build-1107180945;U;en-GB)Presto/2.8.149Version/11.10',
    'Mozilla/5.0(Linux;U;Android3.0;en-us;XoomBuild/HRI39)AppleWebKit/534.13(KHTML,likeGecko)Version/4.0Safari/534.13',
    'NOKIA5700/UCWEB7.0.2.37/28/999',
    'Mozilla/4.0(compatible;MSIE6.0;)Opera/UCWEB7.0.2.37/28/999',
)

proxy_switch = False

IP_PROXY = [
    # 'http://ip:port',


]


MYSQL_SETTINGS = {
    'host': 'localhost',
    'port': 3306,
    'database': 'eastmoney',
    'user': 'root',
    'password': 'janson',
    'charset': 'utf8',
}

redis_settings = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
    'password': '',
}

mongo_settings = {
    'host': '',
    'port': 27017,
    'database': '',
}
