#-*- coding:utf-8 -*-

'''
    需求分析：
        １　https://www.zhaopin.com/  进入职位搜索
        2 通过分类进入之类详细列表
        ３　进入职位详细信息页面
    源码分析
        职位大分类　　　//div[@class='zp-jobNavigater__item--txt']
        　



//div[@class='contentpile__content__wrapper__item clearfix']/a
//div[@class='soupager']/button[2]
'''
import requests
from lxml import etree

url = 'https://sou.zhaopin.com/?jl=765'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 请求内容
r = requests.get(url,headers).text
# print(r)
# 解析
index = etree.HTML(r)
print(index)
# 提取每篇信息的地址
urls = index.xpath("//div[@class='contentpile__content__wrapper__item clearfix']/a")
print(urls)