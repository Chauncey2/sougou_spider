# -*- coding: utf-8 -*-
import scrapy
from ..pipelines import SougouSpiderPipeline

class SougouspiderSpider(scrapy.Spider):
    name = 'sougouSpider'
    # allowed_domains = ['https://www.sogou.com']
    base_url ='https://www.sogou.com/sogou?' \
              'query=%E6%B7%AE%E9%98%B4%E5%B7%A5%E5%AD%A6%E9%99%A2' \
              '&pid=sogou-wsse-a9e18cb5dd9d3ab4' \
              '&insite=wenwen.sogou.com&duppid=1&page={}&ie=utf8'

    start_urls=[base_url]
    # 页面偏移量
    offset=1

    def parse(self, response):
        headers = {
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/71.0.3578.98 Safari/537.36',
            'Accept': '*/*'
        }

        baseUrl = 'https://www.sogou.com/'
        result=response.xpath("//div[@class='results']/div/h3/a/@href")

        for url_item in result.extract():
            url=baseUrl+url_item
            print(url)
            # yield scrapy.Request(url=url,headers=headers,callback=self.parse_detail_age)

        self.offset+=1
        next_page_url=self.base_url.format(str(self.offset))

        if next_page_url:
            yield scrapy.Request(url=next_page_url,callback=self.parse)

    '''
    详细页面的页面解析函数
    可以在这个页面上获取详细的回答内容
    '''

    def parse_detail_age(self,response):

        items=dict()
        question=response.xpath("//div[@class='main']/div/h1/span/text()").extract()
        answer=response.xpath("//*[@id='bestAnswers']/div/div[2]/pre").extract()

        items['title']=question
        items['content']=answer
        print(items)


