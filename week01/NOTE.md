学习笔记

这周的学习实践下来，最有帮助的是环境配置的时候使用venv。
因为我之前的mac里面充斥了各种版本的python，用了pip安装了包还是找不到，非常麻烦。
每开始一个工程都建立一个自己的venv的话，非常干净，不费力。
python3 -m venv venv1
source venv1/bin/activate
pip install -r requirements.txt 

查看版本：
python -V
pip -V
which python

安装初始化scrapy
pip install scrapy
scrapy startproject spiders
cd spriders
scrapy genspider example example.com
执行scrapy
scrapy crawl douban

抓取猫眼的时候，最开始几次还能行，后来就只能验证中心的画面了。