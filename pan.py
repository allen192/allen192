import pandas as pd 
import numpy as np 
# import matplotlib.pypot as plt


# 一　两种数据结构之Series
# １　Series:一种类型类似于一维数组的对象，是由一组数据(各种numpy数据类型)以及一组与之相关的数据标签(即索引)组成．
#     仅有一组数据也可以产生简单的Series对象，注意：Series中的索引值是可以重复的
# ２　DataFrame:一个表格型的数据结构，包含有一组有序的列，每列可以是不同的值类型(数值，字符串，布尔型等)，DataFrame既有
#     行索引也有列索引，可以被看做是有Series组成的字典
# ３　创建
# ser1 = pd.Series([1,2,3,4])
# print(ser1)
# print(type(ser1))
# ser2 = pd.Series(np.array([1,2,3,4]))
# print(ser2)
# print(ser2.dtype)
# print(ser2.values)
# print(ser2.index)
# # 修改索引
# ser1.index=['a','b','c','d']
# print(ser1)
# # 创建是设置索引
# ser2 = pd.Series(np.array([1,2,3,4]),dtype=np.float64,index=['a','b','c','d'])
# print(ser2)
# # 通过字典的方式创建
# ser3 = pd.Series(
#     {
#     'a':10,
#     'b':20,
#     'c':30
#     })
# print(ser3)
# ４　Series值的获取方法
# 通过方括号＋索引的方式获取对应的数据，有可能返回多条数据
# 通过方括号＋下标值的方式获取对应下标值的数据，下标值的取值范围为：
#   [0,len(Series.values)]；另外下标值也可以是负数，表示从右往左取数据
# Series中获取多个值的方式类似与numpy中的ndarray的切片操作，通过方括号＋下标／索引＋冒号：的形式
#   来截取Series对象中的一部分数据
# ser2 = pd.Series(np.array([1,2,3,4]),dtype=np.float64,index=['a','b','c','d'])
# print(ser2['a'])
# print(ser2[0])
# # 切片的时候，用索引的值和下标的值不同，索引包含的终止值，下标没有
# print(ser2['a':'c'])
# print(ser2[0:2])
# ５　Series的运算,都是元素级的运算
# ser2 = pd.Series(np.array([10,20,30,40]),dtype=np.float64,index=['a','b','c','d'])
# print(ser2>10)
# print(ser2+10)
# print(ser2-10)
# print(ser2*10)
# print(ser2/10)
# ６　常用函数　　参照numpy的函数使用
# ser2 = pd.Series(np.array([10,20,30,40]),dtype=np.float64,index=['a','b','c','d'])
# print(np.exp(ser2))
# ７　缺失值处理,会自动加载为空
# ser1 = pd.Series(
#     {
#     'a':10,
#     'b':20,
#     'c':30
#     })
# ser2 =pd.Series(ser1,index=['a','b','c','d'])
# print(ser2)
# # 缺失值检测
# print(pd.isnull(ser2))
# print(pd.notnull(ser2))
# # 缺失值过滤
# print(ser2[pd.isnull(ser2)])
# print(ser2[pd.notnull(ser2)])
# ８　Series自动对齐
# 当多个Series对象之间进行运算的时候，如果不同Series之间具有不同的索引值，那么运算会自动对齐不同
#     索引值的数据，如果某个Series没有某个索引值，那么最终结果会赋值给NaN，即根据索引值相同的相加，不同的返回NaN
# ser1 =pd.Series([1,2,3,4],index=['a','b','c','d'])
# ser2 =pd.Series([10,20,30,40],index=['e','a','b','f'])
# print(ser1+ser2)
# ９　name属性,表示该Series对象的名字Series.name;
# 可以给索引index添加name属性，表示索引的名字，Series.index.name
# ser1 =pd.Series([1,2,3,4],index=['a','b','c','d'])
# ser1.name='aaa'
# ser1.index.name='hello'
# print(ser1)


# 二　两种数据结构之DataFrame
# １　创建
# df1 = pd.DataFrame([['joe','suan','anne'],[70,80,90]])
# print(df1)
# 创建并指定索引值，行索引index,列索引columns
# df2 = pd.DataFrame([['joe','suan','anne'],[70,80,90]],index=['one','two'],columns=['a','b','c'])
# print(df2)
# 通过字典创建  key变成列索引，行索引自己添加，默认０１２．．．
# 放在字典中的value只能是一维数组或者是单个的数据类型，如果是数组，要求长度一致
# df3 = pd.DataFrame({'name':['joe','suan','anne'],
#     'sex':['man','woman','secret'],
#     'classid':3,
#     'age':[18,19,20]},index=['one','two','three'])
# print(df3)
# 修改索引值
# df3.index = ['A','B','C']
# print(df3)
# 不挂是Series还是DataFrame对象，都有索引对象
# 索引对象负责管理轴标签和其他元数据（如轴名称等）
# 通过索引可以从Series DataFrame中获取值或者对某个索引值进行重新赋值
# Series或者DataFrame的自动对齐功能是通过索引实现的


# ２　通过列索引获取数据
# df3 = pd.DataFrame({'name':['joe','suan','anne'],
#      'sex':['man','woman','secret'],
#      'classid':3,
#      'age':[18,19,20]},index=['one','two','three'])
# # 列获取
# print(df3['name'])
# print(df3.name)
# # 列添加
# df3['address']=['beijing','shanghai','shenzhen']
# print(df3)
# # 列删除
# df3.pop('address')
# print(df3)
# # 列修改
# df3['classid'] = 4
# print(df3)
# #　行获取
# print(df3.ix['one'])
# print(df3.loc['one']) 
# # 精确获取某一个
# print(df3.loc['two']['name'])
# print(df3.loc['two','name'])
# print(df3.ix['two']['name'])
# print(df3.ix['two','name'])
# # 行增加
# df3.ix['four'] = [21,3,'black','men']
# df3.loc['four'] = [21,3,'black','men']
# print(df3)
# # 行修改
# df3.ix['four'] = [21,4,'hanxiu','men']
# df3.loc['four'] = [21,4,'hanxiu','men']
# print(df3)
# # 行删除  drop需要重新赋值
# df4 = df3.drop('four')
# print(df4)

# ３　基本操作
# 1) 数据文件读取
# 读取csv和text文档
# df01 = pd.read_csv('data1.csv')
# df03 = pd.read_csv('data2.txt',sep=';',header=None)
# print(df01)
# print(df03)
# 读取excel
# df02 = pd.read_excel('data1.xlsx')
# print(df02)
# ２）　数据的过滤获取
# df3 = pd.DataFrame({'name':['joe','suan','anne'],
#      'sex':['man','woman','secret'],
#      'classid':3,
#      'age':[18,19,20]},index=['one','two','three'])
# print(df3)
#列索引为一个列表,可用切片等
# print(df3.columns[2:])
# ３）　缺省值NaN的处理方法
# 对于DataFrame/Series中的NaN一般采取的方式是删除对应的列／行或者填充一个默认值
# dropna　根据标签的值中是否存在缺失值对轴标签进行过滤（删除），可以通过阈值对缺失值的容忍度进行调节
# fillna 用指定的值或者插值的方式填充数据，比如：ffill 或者 bfill
# isnull 返回一个含有布尔值的对象，这些布尔值表示那些值是缺失值NaN
# notnull isnull的否定式
# df01 = pd.DataFrame(np.random.randint(1,9,size=(4,4)))
# print(df01)
# df01.ix[1:2,1]=np.NaN
# df01.ix[1:2,2]=np.NaN
# df01.ix[1:2,3]=np.NaN
# print(df01)
# # dropna
# print(df01.dropna())   #dropna默认值要包含nan就删除
# print(df01.dropna(how='all'))   #通过how设置行包容度，要全部包含nan才删除
# print(df01.dropna(axis=1))   #通过axis设置列包容度，包含nan的列都删除
# # fillna
# print(df01.fillna(0))    #将NaN的位置变成0
# print(df01.fillna({0:1,1:1,2:2,3:3}))  #根据需要，在不同位置插入不同的值
                                        # 第０列插入一个１，１列插入一个１
                                        # ２列插入两个２，三列插入三个３
# ４）　常用的数学统计方法
# 方法  说明
# count   计算非NA的数量
# describe    针对Series或各dataframe列计算总统计值,获得一个统计信息．各个参数
# min/max 计算最大最小值
# idxmin/idxmax   计算能够获得最大最小值得索引位置（整数）
# sum 值得总和
# mean    值得平均数
# median  值得中位数
# quantile    计算样本的分位数
# mad 根据平均值计算平均绝对距离差
# var 样本数值的方差
# std 样本的标准差
# cumsum  样本值得累积和
# cummin/cummax   样本累计最小值和最大值
# cumprod 样本值的累计积
# pct_change  计算百分数变化    和上一次数据比较的增幅减幅
#   如：7,4,8,2,5        NaN,-0.428571,1.0000,-0.75,1.5

# 求和sum
# df01.sum(axis=0)      #０是按列求，默认按列求和
# df01.sum(axis=1)      #１是按行计算
# ５）　相关系数corr和协方差cov
# 相关系数:反应两个样本之间的相互关联的程度．在协方差的基础上进行了无量纲化操作，即标准化操作．
#   相关系数只能在-1~1之间变化，当相关系数为１的时候，两者相似度最大；０表示不相关；－１表示完全反向负相关
# 协方差cov：反应两个样本或变量之间的相互关系以及之间的相关程度．
# cov(x,y)=E[(X-E(x)(Y-E(y))]=E(X,Y)-E(X)E(Y)
# df01 = pd.DataFrame({
#     'GDP':[400,500,600,700],
#     'foregin_trade':[100,200,100,20],
#     'year':['2012','2013','2014','2015']
#     })
# print(df01)
# print(df01.cov())
# # 具体求值
# print(df01['GDP'].cov(df01['foregin_trade']))
# # 相关系数
# print(df01.corr())
# 6) 唯一值　值计数以及成员资格
# unique方法用于获取Series中的唯一数组（去重数据后的数组），DataFrame需要指定哪一列去重
# value_counts方法用于计算一个Series中各值出现的频率,DataFrame需要指定哪一列计数
# isin方法用于判断矢量化集合的成员资格，可用于选取Series中或者DataFrame中的列数据的子集
# ser01 = pd.Series(['a','b','c','d','a','b','c'])
# print(ser01)
# df01 = pd.DataFrame({
#     'GDP':[400,500,600,700],
#     'foregin_trade':[100,200,100,20],
#     'year':['2012','2013','2014','2015']
#     })
# # 唯一值　　去重
# print(ser01.unique())
# print(df01['foregin_trade'].unique())
# # # 值计数
# print(ser01.value_counts())
# print(df01['foregin_trade'].value_counts())
# # 成员资格判断,返回的布尔值可用来做布尔索引
# print(ser01.isin(['b','c']))
# print(df01['foregin_trade'].isin([200,300]))
# # dataframe的布尔索引显示的是符合条件的一行
# print('测验dataframe的布尔索引：',df01[df01['foregin_trade'].isin([200,300])])
# ７）　层次索引
# 在一个方向上拥有多个（两个及以上）索引级别
# 通过层次化索引，pandas能够以较低的维度形式处理高维度的数据
# 通过层次化索引，可以按照层次统计数据
# 层次索引包括Series层次索引和DataFrame层次索引
#   series层次索引
# data = pd.Series([100,200,122,150,180],
#     index=[
#     ['2016','2016','2016','2017','2017'],
#     ['苹果','香蕉','西瓜','苹果','西瓜']
#     ])
# print(data)
# print(data['2016'])
# print(data[:,'苹果'])
# # 交换分层索引?
# # data01 = data.swaplevel(1,1).sort_index()
# # print(data01)
# # 转化成为DataFrame索引的堆
# data02 = data.unstack(level=1)    #指定那一列的索引为表格的列索引
# print(data02)
# # 转换回Series
# data03 = data02.stack(level = 0)
# print(data03)
#   DataFrame层次索引
df = pd.DataFrame({
    'year':[2001,2001,2002,2002,2003],
    'fruit':['apple','banana','apple','banana','apple'],
    'production':[2345,3124,5668,2532,2135],
    'profits':[233.44,4452.2,1225.2,7845.2,2335.2]
    })
print(df)
# 转换成两个行索引
df01 = df.set_index(['year','fruit'])
print(df01)
# 根据索引获取值
print(df01.ix[2002,'apple'])
# 按照层次索引进行数据统计
print(df01.sum(level='year'))
print(df01.mean(level='fruit'))
print(df01.min(level='fruit'))







