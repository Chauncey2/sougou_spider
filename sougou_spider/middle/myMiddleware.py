from selenium import webdriver
from scrapy.http import HtmlResponse
import time

class JavaScriptMiddleware(object):
    def process_request(self, request, spider):

        if spider.name == "sougouSpider":
            # driver = webdriver.Chrome("./chromedriver.exe") #指定使用的浏览器插件

            driver=webdriver.PhantomJS("./browserDriver/phantomjs.exe") # 使用无界面的phantomjs.exe浏览器插件，用户体验更好
            driver.get(request.url)
            time.sleep(1)

            # js = "var q=document.documentElement.scrollTop=10000"
            # driver.execute_script(js) #可执行js，模仿用户操作。此处为将页面拉至最底端。
            # time.sleep(3)

            body = driver.page_source
            print ("访问"+request.url) # 输出访问的url链接
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return None
