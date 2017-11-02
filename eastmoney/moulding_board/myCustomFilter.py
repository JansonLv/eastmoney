""" 
@author:jansonlv
@file: bloomReadisFilter.py 
@time: 2017/10/15
@IDE: PyCharm
@project:general_scrapy
url过滤器
1.url去重
2.url生成haslib
3.布隆算法
"""

from scrapy.dupefilters import RFPDupeFilter
import hashlib
# 将url标准化
from w3lib.url import canonicalize_url

class URLFilter(RFPDupeFilter):
    '''根据url过滤'''
    def __init__(self, path=None, debug=False):
        self.urls_seen = set()
        RFPDupeFilter.__init__(self, path, debug)

    def request_seen(self, request):
        if request.url in self.urls_seen:
            return True
        else:
            self.urls_seen.add(request.url)


class URLSha1Filter(RFPDupeFilter):
    """
    根据urlsha1过滤
    """
    def __init__(self, path=None, debug=False):
        self.urls_seen = set()
        RFPDupeFilter.__init__(self, path, debug)

    def request_seen(self, request):
        fp = hashlib.sha1()
        fp.update(canonicalize_url(request.url).encode())
        url_sha1 = fp.hexdigest()
        if url_sha1 in self.urls_seen:
            print('*'*50)
            print('*'*50)
            print(url_sha1)
            print('*'*50)
            print('*'*50)
            return True
        else:
            self.urls_seen.add(url_sha1)


# 导入布隆算法包
from pybloom import ScalableBloomFilter


class URLBloomFilter(RFPDupeFilter):
    '''
    根据urlhash_bloom过滤
    '''
    def __init__(self, path=None, debug=False):
        self.urls_sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
        RFPDupeFilter.__init__(self, path, debug)

    def request_seen(self, request):
        fp = hashlib.sha1()
        fp.update(canonicalize_url(request.url).encode())
        url_sha1 = fp.hexdigest()
        if url_sha1 in self.urls_sbf:

            return True
        else:
            self.urls_sbf.add(url_sha1)

