# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import pandas as pd


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        # 打印网页的url
        print(response.url)
        # 打印网页的内容
        # print(response.text)

        movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        for movie in movies:
        #     title = i.find('a').find('span',).text
        #     link = i.find('a').get('href')
            # 路径使用 / .  .. 不同的含义　
            title = movie.xpath('./a/text()')
            link = movie.xpath('./a/@href')
            print('-----------')
            print(title)
            print(link)
            print('-----------')
            print(title.extract())
            print(link.extract())
            print(title.extract_first())
            print(link.extract_first())
            print(title.extract_first().strip())
            print(link.extract_first().strip())


            yield scrapy.Request(url='https://maoyan.com'+link, callback=self.paser2)

    #解析具体页面
    def paser2(self, response):
        # 电影名称
        film_name = Selector(response=response).xpath('//h1[@class="name"]/text()')
        print(f'电影名称: {film_name}')

        # 电影类型
        film_category = Selector(response=response).xpath('//div[@class="movie-brief-container"]/ul/li[1]/a[1]/text()')
        print(f'电影类型: {film_category}')

        # 上映时间
        plan_date = Selector(response=response).xpath('//div[@class="movie-brief-container"]/ul/li[3]/text()')
        print(f'上映时间: {plan_date}')

        mylist = [film_name, film_category, plan_date]

        movie1 = pd.DataFrame(data = mylist)

        # windows需要使用gbk字符集
        movie1.to_csv('./movie-scrapy.csv', encoding='utf8', index=False, header=False)
