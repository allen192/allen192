import re
import requests
from bs4 import BeautifulSoup


# ２　匹配全是中文字符   [\u4E00-\u9FA5]
# str = '广东省深圳市'
# pattern = re.compile('^[\u4E00-\u9FA5]+$')
# print(pattern.findall(str))

# ３　过滤掉网页上的所有JS脚本（即把script标记及其内容都去掉）
# s = '''<head><script>
# if(bds.comm.supportis){
#     window.__restart_confirm_timeout=true;
#     window.__confirm_timeout=8000;
#     window.__disable_is_guide=true;
#     window.__disable_swap_to_empty=true;
# }
# initPreload({
#     'isui':true,
#     'index_form':"#form",
#     'index_kw':"#kw",
#     'result_form':"#form",
#     'result_kw':"#kw"
# });
# </script></head>'''
# pattern = re.compile('<script>.*</script>',flags=re.S)
# print(pattern.findall(s))
# print(pattern.sub('',s))

# ４　匹配img标签中的src路径
# str ='''<img name='photo' src='../public/img/img1.png' />
# <img name='news' src='xxx.jpg' titles='news' />'''
# pattern = re.compile('src=[\'\"](.*?)[\'\"]')
# # print(pattern.findall(str))
# str2 = pattern.finditer(str)
# for x in str2:
#     print(x.group(1))
# ５　匹配电话号码
# phone = '13866669999'   #138****9999
# pattern =re.compile('^(1[3578]\d)(\d{4})(\d{4})$')
# phone2 = pattern.finditer(phone)
# for i in phone2:
#     print(i.group())
#     print(i.group(1))
#     print(i.group(2))
#     print(i.group(3))
# print(pattern.sub(r'\1****\3',phone))    #\1\2\3是三个分组



# ====================爬虫=======================

'''
# 请求页面获取html
r =requests.get('http://www.baidu.com').content.decode('utf-8')
# 解析成html文档格式
soup = BeautifulSoup(r,'html.parser')    #有两种，html.parser和lxml
# print(type(soup))
# 美化格式，可用可不用,将之前横着的变成html层级结构，方便看
html = soup.prettify()
# print(html)
# 可以将这个html页面保存到文档中，也可以不保存
# with open('baidu.html','a+',encoding='utf-8') as file:
#     file.write(html)
'''


soup = BeautifulSoup(open('baidu.html','r',encoding='utf-8'),'lxml')

# print(type(soup))
# 四大对象
#   TAG：通俗点讲就是html中的标签对于Tag有两个重要的属性：
#           Name:返回标签名称　　　Attrs:返回标签属性
#   NavigableString:通过string获取标签里的内容；strings:获取多个内容，不过需要遍历获取
#   BeautifulSoup:BeautifulSoup对象表示的是一个文档的内容．大部分的时候，可以把它当做Tag对象，
#           是一个特殊的Tag，我们可以分别获取它的类型，名称以及属性
#   Comment:Comment对象是一个特殊类型的NavigableString对象，其输出内容不包括注释符号

#  Tag   拿标签
# print(soup.html.head.meta)    # 通过标签获取
# # 标签的属性：Name Attrs
# print(soup.div.input.name)    #返回标签姓名
# print(soup.div.input.attrs)    #返回标签里的属性，字典的格式   字典索引：soup.div.input.attrs['type']
# #   NavigableString　　　　　拿标签的文本内容
# print(soup.html.title.string)    #即使注释掉也可以拿到,注释掉了就是comment,没注释就是 NavigableString
# print(type(soup.html.title.string))

# 如何遍历文档树？
    # 直接子节点：
        # contents:标签的contents属性可以将Tag的子节点以列表的方式输出
        # children:返回一个可迭代的对象
# print(soup.head.contents)    #空格，换行都会算作子节点加入列表中显示，需要手动计算需要的标签是第几个子节点
# print(soup.head.contents[7])   #列表索引提取子节点
# print(soup.head.contents[7].attrs['href'])   #列表索引提取子节点的标签属性
    # 所有子孙节点：
        # descendants属性可以对所有的Tag的子孙节点进行递归循环，和children类似，需要遍历获取内容
print(soup.head.children)   #返回一个迭代对象
for d in soup.head.children:
    print(d)
    # 节点内容：
        # string:返回标签里面的内容
        # text:返回标签的文本


