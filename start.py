# -*- coding: utf-8 -*-
from scrapy import cmdline

# cmdline.execute("scrapy crawl POS -o baiketxt.json".split())

# cmdline.execute("scrapy crawl POS".split())

# scrapy crawl POS -s JOBDIR=crawls/somespider -o baikedict.json

cmdline.execute("scrapy crawl lianjia -o rent.csv -t csv".split())

