# -*- coding: utf-8 -*-
import scrapy
from qiubai_proj.items import ToscrapeBooksItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        '''
        next_page = \
            response.xpath('//div/ul[@class="pager"]/li[@class="next"]/a/@href').extract_first()
        print(next_page)
        if next_page == "catalogue/page-2.html":
            next_url = self.start_urls[0] + next_page
        else:
            next_url = self.start_urls[0] + "catalogue/" + next_page
        #print(next_url)
        yield scrapy.Request(next_url, callback=self.parse)
        '''

        #分析本页面--> response.url
        div_list = response.xpath('//article[@class="product_pod"]')
        print(div_list)  #[<selector 1> , <selector 2>]
        for div in div_list:
            image_url = div.xpath('./div[@class="image_container"]/a/img/@src').extract_first()
            image_url = self.start_urls[0] + image_url
            star_count = div.xpath('./p/@class').extract_first()
            star_count = star_count.split(" ")[-1]
            title = div.xpath('./h3/a/@title').extract_first()
            price = div.xpath('./div[@class="product_price"]/p[@class="price_color"]/text()').extract_first()

            detail_url = div.xpath('./h3/a/@href').extract_first()
            if detail_url != None:
                detail_url = self.start_urls[0] + detail_url
                book = ToscrapeBooksItem(image_url=[image_url], title=title, detail_url=detail_url,
                                         star_count=star_count, price=price)

                request = scrapy.Request(detail_url, callback=self.parse_detail)
                request.meta['book'] = book
                yield request


    def parse_detail(self, response):
        book = response.meta['book']
        description = response.xpath('//div[@id="content_inner"]/article/p/text()').extract_first()
        description = " ".join(description.split(","))
        book['description'] = description
        print(book)
        #yield book

