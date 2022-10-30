import scrapy
from NewsPostman.items import NewspostmanItem


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    start_urls = [
        'https://top.baidu.com/board?tab=realtime'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'Baidu.html'
        news_title_list = response.xpath('//div[@class="c-single-text-ellipsis"]/text()').getall()
        for news_title in news_title_list:
            news_title = news_title[2:] # baidu title begin with two space
            yield NewspostmanItem(
                title = news_title,
                url = '',
                hot_index = 0,
                category = 'baidu',
                descrip = ''
            )