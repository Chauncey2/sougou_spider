# -*- coding: utf-8 -*-

import scrapy


class SougouSpiderItem(scrapy.Item):

    # 问题
    question=scrapy.Field()
    # 回答
    answer=scrapy.Field()

