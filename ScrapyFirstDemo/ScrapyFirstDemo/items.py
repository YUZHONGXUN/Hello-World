# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RateItem(scrapy.Item):            # 先把物件定義來繼承
    title = scrapy.Field()          # 給定一個欄位資料
    rate = scrapy.Field()

