# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    qid = scrapy.Field() #问题ID
    aid = scrapy.Field() #答案ID
    atoken = scrapy.Field() #问题token
    title = scrapy.Field()
    agreeCount = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()


