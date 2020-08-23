# 翻页的处理

import requests
import lxml.etree
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd

def getData(url):
    print(url)
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'

    # 声明为字典使用字典的语法赋值
    header = {}
    header['user-agent'] = user_agent
    response = requests.get('https://maoyan.com' + url, headers=header)

    # xml化处理
    selector = lxml.etree.HTML(response.text)

    # 电影名称
    film_name = selector.xpath('//h1[@class="name"]/text()')
    print(f'电影名称: {film_name}')

    # 电影类型
    film_category = selector.xpath('//div[@class="movie-brief-container"]/ul/li[1]/a[1]/text()')
    print(f'电影类型: {film_category}')

    # 上映时间
    plan_date = selector.xpath('//div[@class="movie-brief-container"]/ul/li[3]/text()')
    print(f'上映时间: {plan_date}')

    mylist = [film_name, film_category, plan_date]

    movie1 = pd.DataFrame(data = mylist)

    # windows需要使用gbk字符集
    movie1.to_csv('./movie-requests.csv', encoding='utf8', index=False, header=False)


myurl = 'https://maoyan.com/films?showType=3'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'

header = {'user-agent':user_agent}
response = requests.get(myurl,headers=header)
print(response.status_code)
bs_info = bs(response.text, 'html.parser')
print(bs_info)
count = 0

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
for atags in bs_info.find_all('a', attrs={'data-act': 'movie-click'}):
    print(atags)
    # 获取链接
    url = atags.get('href')
    if url == "/films" : continue
    print(url)

    if count > 10: break

    getData(url)

    count +=1
    sheep(10)




