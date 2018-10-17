import scrapy
import datetime
from qiubai_proj.items import BooksQuantag


class BookSpider(scrapy.Spider):
    name = 'booksspider'
    allowed_domains = ['quanshuwang.com/']
    start_urls = ['http://www.quanshuwang.com/']

    def parse(self, response):
        id = 1
        t_name = response.xpath("//ul[@class='channel-nav-list']/li/a")
        for T_name in t_name:
            t_name = T_name.xpath("./text()").extract_first()
            print(t_name)
            request = BooksQuantag(id=id,t_name=t_name,t_info=t_name,t_createtime=datetime.datetime.now(),t_flag=1)
            id += 1
            yield request


