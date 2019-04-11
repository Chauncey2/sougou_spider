# -*- coding: utf-8 -*-

import re


class SougouSpiderPipeline(object):

    def process_item(self, item, spider):

        # 获取回答内容
        answer_html=item['answer'][0]

        regex=r'<[^>]+>'
        pattern=re.compile(regex,re.S)
        # 清洗答案字符串中的html标签
        item['answer'][0]=pattern.sub('',answer_html)
        print(pattern.sub('',answer_html))

        return item
