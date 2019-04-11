from scrapy.cmdline import execute
# 保存为csv格式
# execute(["scrapy","crawl","sougouSpider","-o","answer_data.csv"])

# 保存为json格式
execute(["scrapy","crawl","sougouSpider","-o","answer_data.json"])