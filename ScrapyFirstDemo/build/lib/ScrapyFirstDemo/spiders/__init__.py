# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from ScrapyFirstDemo.items import RateItem
class RateSpider(scrapy.Spider):        # 創立物件 Spider
    name = "rate"         # 蜘蛛的名字
    allowed_domains = ['rate.bot.com.tw']           # 它是一個 List, 擷取網站的住址部分
    start_urls = ['http://rate.bot.com.tw/xrt?Lang=zh-TW']          # spider 開始擷取網站的起點
    def parse(self, response):          # parse是擷取的功用, 可把文件當成 response
        for single_row in response.xpath('//table/tbody/tr'):    # 第一次的尋找路徑
            item  = RateItem()          # 回傳到 item
            t = single_row.xpath('td[1]/div/div[2]/text()').extract_first()
            r = single_row.xpath('td[3]/text()').extract_first()    # 找到內容的位置
            item['title'] = t.replace('\r', '').replace('\n', '').replace(' ','')       # 定義資料成為 key
            item['rate'] = r
            print("aa:", t, t)
            yield item          # yield 每次執行時產生程式, 輸出到 item ; return 的功能是結束跳出迴圈
