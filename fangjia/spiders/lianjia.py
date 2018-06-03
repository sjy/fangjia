# -*- coding: utf-8 -*-
import scrapy
from fangjia.items import FangjiaItem

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

class lianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domins = ["http://cd.fang.lianjia.com/"]
    start_urls = []

    def start_requests(self):
        global headers
        urlhead = 'http://cd.fang.lianjia.com/loupan/'
        for i in range(2):
            url = urlhead+'pg%snht1' % i
            self.start_urls.append(url)
        for url in self.start_urls:
            print (url)
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        global headers
        fang_links = response.css('a.name::attr(href)').extract()
        if fang_links:
            for fang_link in fang_links:
                url = 'http://cd.fang.lianjia.com'+fang_link
                yield scrapy.Request(url, headers=headers, callback=self.parse_fangjia)

    def parse_fangjia(self, response):   # /是在根节点找(只找根节点下面一层,绝对) //是在根节点下面的所有节点找,相对
        item = FangjiaItem()
        name = response.css('.DATA-PROJECT-NAME::text').extract()[0]
        url = response.css('a.clear::attr(href)').extract()[0]
        price = response.css('span.junjia::text').extract()[0]
        address = response.css('.where span::attr(title)').extract()[0]
        item['FANGJIA_NAME'] = name
        item['FANGJIA_ADDRESS'] = address
        item['FANGJIA_PRICE'] = price
        item['FANGJIA_URL'] = 'http://cd.fang.lianjia.com'+url
        yield item

