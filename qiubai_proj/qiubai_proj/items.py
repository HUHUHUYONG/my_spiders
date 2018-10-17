# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiProjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_url = scrapy.Field()
    name  = scrapy.Field()
    sex = scrapy.Field()
    age = scrapy.Field()
    content = scrapy.Field()
    image_figer = scrapy.Field()


class ToscrapeBooksItem(scrapy.Item):
    image_url = scrapy.Field()
    title = scrapy.Field()
    detail_url = scrapy.Field()
    star_count = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()



class BooksQuan(scrapy.Item):
    a_title = scrapy.Field()
    a_info = scrapy.Field()
    a_content = scrapy.Field()
    a_img = scrapy.Field()
    a_createtime = scrapy.Field()


class BooksQuantag(scrapy.Item):
    id = scrapy.Field()
    t_name = scrapy.Field()
    t_info = scrapy.Field()
    t_createtime = scrapy.Field()
    t_flag = scrapy.Field()





