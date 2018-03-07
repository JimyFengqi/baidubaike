# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy import Spider
from baidu_baike.items import BaiduBaikeItem

class baidubaikeSpider(Spider):
    name='baidu_baike'
    allowed_domains=["www.baidu.com"]
    start_urls=["https://baike.baidu.com/",
    "https://baike.baidu.com/item/Python/407313"]
    
    def parse(self,response):
        print (response.url)
        title=response.xpath('//head/title/text()').extract_first()
        print ('title is '+title)
        print ('hello,world!')
        item=BaiduBaikeItem()

        print ('hello,world!')
        return item