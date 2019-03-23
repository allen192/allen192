#-*- coding:utf-8 -*-


# 爬python 100网站的源代码题目
import re
from bs4 import BeautifulSoup
import requests

url = 'http://www.runoob.com/python/python-100-examples.html'
# headers ={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/65.0'}
# 发送请求
r = requests.get(url).content.decode('utf-8')
# print(r)
# 解析文档
soup=BeautifulSoup(r,'lxml')
# print(soup)
html = soup.prettify()
with open('python100.html','w',encoding='utf-8') as file:
     file.write(html)

# 查找每个a标签的href属性对应的链接
re_a = soup.find(id = 'content').ul.find_all('a')
# print(re_a)   #拿到100个a 标签的列表
lis = []
for i in re_a:
    # print(i.attrs['href'])
    lis.append(i.attrs['href'])
# print(lis)

# 根据获得的每个链接的地址来获得练习的页面内容
s ='http://www.runoob.com'
datas = []
for x in lis:
    dict = {}
    ar = requests.get(s+x).content.decode('utf-8')
    # print(ar)
    # 解析成html文档
    soup_ar = BeautifulSoup(ar,'lxml')
    # print(type(soup_ar))
    # 查找练习
    # a 查找标题
    title = soup_ar.find(id='content').h1.text
    # print(title)
    dict['title'] = title
    # 查找题目
    tm = soup_ar.find(id='content').find_all('p')[1].text
    # print(tm)
    dict['tm'] = tm
    # c 程序分析
    cxfx = soup_ar.find(id='content').find_all('p')[2].text
    dict['cxfx'] = cxfx
    # d 源代码
    try:
        code = soup_ar.find(class_='hl-main').text
    except Exception as e:
        code = soup_ar.find('pre').text
    # print(code)
    dict['code'] = code
    # print(dict['title'],dict['tm'])
    datas.append(dict)
# 保存文件
# import pandas as pd
# data = pd.DataFrame(datas)
# data.to_csv('py-100.csv')

    with open('100-py.csv','a+',encoding='utf-8') as file:
        file.write(dict['title']+'\n')
        file.write(dict['tm']+'\n')
        file.write(dict['cxfx']+'\n')
        file.write(dict['code']+'\n')
        file.write('*'*50+'\n')






