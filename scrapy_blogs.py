#-*- coding:utf-8 -*-
'''
    需求分析
        爬取博客园的帖子
    源码分析：
        https://www.cnblogs.com/
        tz =post_item_body   帖子的链接

        title = cb_post_title_url
        content = cnblogs_post_body
    代码实现
        １根据入口url请求源码
        ２提取数据（每篇帖子的url）
        ３根据帖子的url进去到帖子的详情，获取详细的内容
        ４保存数据
'''

import requests
from lxml import etree

# １根据入口url请求源码
url = 'https://www.cnblogs.com/'
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
r = requests.get(url,headers).text
# print(r)
# 解析
index = etree.HTML(r)
# print(index)

#２提取数据（每篇帖子的url） 
tz_url = index.xpath("//div[@class='post_item_body']/h3/a/@href")
for i in tz_url:
    # print(i)
    # ３根据帖子的url进去到帖子的详情，获取详细的内容
    re = requests.get(i).text
    # 解析
    html = etree.HTML(re)
    # print(html)
    # 提取标题和内容
    tz_title = html.xpath("//a[@id='cb_post_title_url']/text()")
    # print(tz_title)
    tz_cotent = html.xpath("string(//*[@id='cnblogs_post_body'])")
    # print(tz_cotent)

    # 保存内容
    with open('cn-blogs.csv','a+',encoding='utf-8') as file:
        file.write(tz_title[0]+'\n')
        file.write(tz_cotent+'\n')
        file.write(i+'\n')
        file.write('*'*50+'\n')
    
