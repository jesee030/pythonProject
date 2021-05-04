# -*- coding: utf-8 -*-
import scrapy


class JySpider(scrapy.Spider):
    name = 'jy'
    allowed_domains = ['guet.edu.cn']
    start_urls = ['https://www.guet.edu.cn/jy/zhaopin.jsp?a165823t=475&a165823p=1&a165823c=10&urltype=tree.TreeTempUrl&wbtreeid=1003']
    date = '' #此date为给定日期，已在__init__.py中初始化，直接在下面函数中用self.date调用即可

    def parse(self, response):
        # 爬取1到200页
        for i in range(1, 100):
            url = 'https://www.guet.edu.cn/jy/zhaopin.jsp?a165823t=475&a165823c=10&urltype=tree.TreeTempUrl&wbtreeid=1003&a165823p='+str(i)
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
    # 在此处添加代码

