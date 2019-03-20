import numpy as np 
import random

# 一　创建
# １　numpy的数组类被称为ndarray。通常被称作数组。注意，numpy和标准python库类array.array
# 并不相同，后者只处理一维数组和提供少量的功能。
# ２　一种由相同类型的元素组成的多维数组，元素数量是事先给定好的
# ３　元素的数据类型由dtype(data-type)对象来指定，每个ndarray只有一种dtype类型
# ４　ndarray的大小固定，创建好数组后数组大小是不会再发生改变的。注意，是大小。


# ones,zeros,logspace,linspace,引入random模块，random,randint,randn也可以创建
# １　array函数：接受一个普通的python序列，并将其转换成ndarray
# a = np.array([[1,2,3],[4,5,6]])
# ２　zeros函数：创建指定长度或者形状的全０数组
# arr1 = np.zeros((2,3))
# print(arr1)
# ３　ones函数：创建指定长度或者形状的全１数组
# arr2 = np.ones((4,3))
# print(arr2)
# ４　empty函数：创建一个没有任何具体值的数组（准确的说是创建一些未初始化的ndarray多维数组）和ones差不多
# arr = np.empty((3,3))
# print(arr)
# ５　arrange函数：类似python的range函数，通过指定开始值，终止值，步长来创建一个一维数组．不包含终止值．
# np.arange(9)
# np.arange(1,9)
# np.arange(1,9,2)
# ６　linspacs函数：通过指定开始值，终止值和元素个数类创建一个一维数组，数组的数据元素符合等差数列，
#   可以通过endpoint关键字指定是否包含终止值，默认包含．
# np.linspace(1,10,5)   #开始１，结束１０，５个
# ７　logspacs函数：通过指定开始值，终止值和元素个数类创建一个一维数组，数组的数据元素符合等比数列，
#   可以通过endpoint关键字指定是否包含终止值，默认包含．
#   0表示10的0次方，2表示10的2次方，5表示最终生成的元素数量为5个（可以通过参数base指定具体的底数）
# np.logspace(0,2,5)   #开始１，结束１０，５个
# ８　使用随机数填充数组：使用numpy.random中的random()函数来创建0-1之间的随机元素，数组包含的元素数量
#   由参数确定
# np.random.random((3,3))  #创建0-1之间的数，３行３列 
# np.random.randint(1,9,size=(3,3)) #创建1-9之间的整数，３行３列
# np.random.random(3,3)  #创建符合标准正态分布数，３行３列 
# np.random.rand(9)  #创建0-1之间的数，9个




# 二　基本属性
# ndarray的大小固定，创建好数组后数组的大小不会发生改变
# a = np.array([[1,2,3],[4,5,6]])
# print(a)
# １　ary.ndim数组轴（维度）的个数，轴的个数被成为秩
# ary = np.random.randint(1,9,size=(3,3))
# print(ary.ndim)
# 也可以通过sry.shape查看数组的维度，如上所说
# 测试数组维度,返回一个元祖
# print(a.shape)

# ndarray形状修改
# ２　直接修改数组的shape值，要求修改后乘积不变
# 改维度,要求修改后乘积不变,如６个可以变成2x3,3x2,1x6,6x1。不能改为5x1.2，会报错
# a.shape=(6,)    #强制修改
# print(a)
# ３　当指定某一轴为－１的时候，表示将根据数组元素的数量自动计算该轴的长度值
# a.shape=(2,-1)  #－１是让系统自动计算，２行多少列
# print(a)
# a.shape=(-1,2)  #－１是让系统自动计算，２列多少行
# print(a)
# ４　使用reshape函数创建一个改变尺寸的新新数组，原数组的shape保持不变，但是和新数组共享同一个
#   内存空间，也就是说修改任何一个数组的值会对另外一个造成影响
# arr = a.reshape(3,2)   #通过reshape()修改,需要重新赋值
# print(arr)
# arr[0,0]=100   #索引更改赋值,浅拷贝，原数组也会跟着改变
# print(arr)
# print(a)

# ５ 测试元素的类型,可以通过创造或者指定python标准类型，不过／numpy有自己的数据类型
# print(a.dtype)

# ６ 测试数组元素的个数
# print(a.size)

# ７　数组中每个元素的字节大小,如float64的数组itemsize的属性值为64/8=8
# print(a.itemsize)

# ８ 测试维度,里面有几个列表
# print(len(a))

# ９　数组元素的索引
# ary = np.arange(1,28)
# ary.shape=(3,3,3)     #3页，３行，３列
# print(ary,'ary.shape',ary.shape)
# print('ary[0]',ary[0])
# print('ary[0][0]',ary[0][0])
# print('ary[0][0][0]',ary[0][0][0])  # 第一页上的第一行的第一个字
# print('ary[0,0,0]',ary[0,0,0])
# print('ary.shape[0]',ary.shape[0])
# print('ary.shape[1]',ary.shape[1])
# print('ary.shape[2]',ary.shape[2])


# １０　切片
# 在各维度上单独切片，如果某维度都保留，则直接使用：冒号，不指定起始值和终止值
# ary = np.array([
#     [
#     [6,3,6],
#     [4,4,6],
#     [5,8,7]],
#     [[4,3,2],
#     [6,1,4],
#     [6,3,6]
#     ]])
# print(ary)
# print(ary[:,:,1])
# print(ary[0,0:3:2,1:3])
# [[3 4 8]
 # [3 1 3]]


# １０　遍历三维数组
# for i in range(ary.shape[0]):
#     for j in range(ary.shape[1]):
#         for k in range(ary.shape[2]):
#             print(i,j,k)   # 索引
#             print(ary[i,j,k])# 对应的值
# 思考？能否直接用ary遍历？

# １１　numpy内置的基本数据类型
# 布尔型　　bool_
# 有符号整型　int8(-128~127)/int16/int32/int64
# 无符号整型 uint8(0~255)/uint16/uint32/uint64
# 浮点型　float16/float32/float64
# 复数型　complex64(实部，虚部均是float32)/complex128(实部，虚部均是float64)
# 字符串型　str_(每个字符串用３２位的unicode编码表示)

# １２　查看并修改数据类型   astype属性修改数据类型
# arr2 = np.array([1,2,3,4])
# print(arr2.dtype)
# arr3=arr2.astype(float)
# print(arr3.dtype)
# 创建时指定数据类型，数组中元素的数据类型都时相同的
# arr2=np.array([1,2,3,4],dtype=float)
# print(arr2.dtype)

# arr2=np.array(['a','b','c','d'])
# print(arr2.dtype)

# 三　基本操作
# 数组不用循环即可对每个元素执行批量的算数运算操作，这过程叫做矢量化，
# 即用数组表达式代替循环的做法
# 矢量化数组运算能力比纯python方式快一两个数量级
# 大小相等的两个数组之间的任何算数运算都会将其运算应用到元素级上的操作
# 元素级操作：在numpy中，大小相等的数组之间的运算，为元素级的运算，即只用于位置相同的元素之间，
# 所得的运算结果组成一个新的数组，运算结果的位置跟操作数位置相同

# １　与标量之间的运算
# arr = np.arange(0,9).reshape(3,3)
# print(arr)
# print(arr+2)
# print(arr-2)
# print(arr*2)
# print(arr/2)

# ２　数组之间的运算
# arr1 = np.array([
    # [10,20,30],
    # [40,50,60]
    # ])
# arr1 = np.array([
#     [10,20],
#     [40,50]
#     ])     线性代数中不能相加，此处也是不能相加！
# arr2 = np.array([
#     [1,2,3],
#     [4,5,6]
#     ])
# print(arr1)
# print(arr2)
# print('arr1+arr2',arr1+arr2)    # 加减法是元素级的运算
# print('arr1*arr2',arr1*arr2)    # 这不是矩阵之间的乘法！这是和加法一样，采用的元素级运算
# a1 = np.array([
#     [10,20],
#     [40,50]
#     ])
# a2 = np.array([
#     [1,2,3],
#     [4,5,6]
#     ])
# a3 = np.dot(a1,a2)   #这才是矩阵之间的乘法！矩阵之间的乘法不是元素级运算！！！！
# print(a3)

# 3 花式索引
# 是指利用整数数组进行索引的方式
# arr =np.random.randint(1,9,size=(8,4))
# print(arr)
# 获取0,3,5行数据
# print(arr[[0,3,5]])
# 获取0,0 3,3 5,2数据,意义对应
# print(arr[[0,3,5],[0,3,2]])
# 索引器  表示-0行的0,3,2号数据，３行的０，３，２号数据,5行的０，３，２号数据
#           每行的０，３，２号元素
# print(arr[np.ix_([0,3,5],[0,3,2])])

# ４　布尔索引
# 利用布尔类型的数组进行数据索引，最终返回的结果是对应索引数组中数据为True位置的值
# arr = np.random.random((3,3))
# print(arr)
# arr2 = arr<0.5
# print(arr2)
# name = np.array(['joe','susan','Tom'])
# score = np.array([
#     [70,80,90],
#     [77,88,99],
#     [66,86,96]
#     ])
# classes = np.array(['语文','数学','英语'])
# print(name=='joe')   #name=='joe'返回的是一个数组，[ True False False]
# print('joes score:',score[name=='joe'])   #花式索引．score[[ True False False]],
#                             # 其实就是score[[0,1,2]]的变相，只是用布尔值代替了，返回True的位置一行的值
# # print('语文',score[classes=='语文'])   # 结果同上，因为和name=='joe'和classes=='语文'返回值一样
# print('joes math score',score[name=='joe',classes=='数学'])   #或者
# print('joes math score',score[name=='joe'].reshape(-1,)[classes=='数学'])   #用reshape函数改变维度
# a = score[(name=='joe')|(name =='susan')]    #逻辑或｜；逻辑与＆；逻辑非~  不能使用and or not
# print(a)
# b = score[(name!='joe')&(name !='susan')]
# print(b)
# c = score[~(name == 'joe')]
# print(c)


# ５　数组的转置和轴对换
# 数组转置是指将shape进行重置操作，并将其值重置为原始shape元组的倒置，如：shape值为(2,3,4)   
# 转置之后的新元组的shape值为(4,3,2)f
# 对于二维数组(矩阵)，数组的转置就是矩阵的转置
# 可以通过调用数组的transpose函数或者T属性进行数组的转置操作 重新赋值
# arr =np.arange(40).reshape(5,-1)
# print('原来的数组：',arr)
# arr1 = arr.transpose()
# print('通过transpose函数转置后的数组：',arr1)
# arr2 = arr.T
# print('通过属性T转置后的数组：',arr2)

# 四　常用函数
# １　常用一元函数
# arr = np.array([-1,-2,-3])
# arr1 = np.abs(arr)
# # 绝对值
# print('绝对值:',arr1)
# # 平方根
# print('平方根:',np.sqrt(arr1))
# # 计算各个元素的指数e的x次方
# print('指数e的x次方:',np.exp(arr1))
# # 分别计算自然对数，底数为10的log，底数为2的log,以及log(1+x)，要求arr中的每个元素必须是正数
# print('自然对数:',np.log(arr1))
# print('底数为10的log:',np.log10(arr1))
# print('底数为2的log:',np.log2(arr1))
# print('log(1+x):',np.log1p(arr1))
# # 计算各个元素的正负号：1 0 -1分别为正数　零　负数
# print('各个元素的正负号:',np.sign(arr1))
# # ceil和floor分别是天花板和地板，代表向上取整和向下取整
# print('向上取整:',np.ceil(arr1))
# print('向下取整:',np.floor(arr1))
# # 四舍五入到最接近的整数
# print('四舍五入取整:',np.rint(arr1))
# # 判断元素不是数字　　isnan(is not a number)
# print('判断元素不是数字:',np.isnan(arr1))
# # 判断元素是不是有穷　　isfinite,isinf　有穷，无穷
# print('判断元素是有穷:',np.isfinite(arr1))
# print('判断元素是无穷:',np.isinf(arr1))
# # 普通以及双曲型三角函数 sin cos tan,sinh cosh tanh
# print('转成sin:',np.sin(arr1))
# print('转成cos:',np.cos(arr1))
# print('转成tan:',np.tan(arr1))
# print('转成sinh:',np.sinh(arr1))
# print('转成cosh:',np.cosh(arr1))
# print('转成tanh:',np.tanh(arr1))
# # 反三角函数
# # print('转成arcsin:',np.arcsin(arr1))
# # print('转成arccos:',np.arccos(arr1))
# print('转成arctan:',np.arctan(arr1))
# print('转成arcsinh:',np.arcsinh(arr1))
# print('转成arccosh:',np.arccosh(arr1))
# # print('转成arctanh:',np.arctanh(arr1))

# ２　二元函数
# arr1 = np.array([[1,0,-1,2],[-1,1,3,0],[0,5,-1,4]])
# arr2 = np.array([[0,3,4],[1,2,1],[3,1,-1],[-1,2,1]])
# 求两个数组的点积
# print('点积:',np.dot(arr1,arr2))

# arr1 = np.random.randint(1,9,size=(3,3))
# arr2 = np.random.randint(1,9,size=(3,3))
# print(arr1)
# print(arr2)
# # 元素级的求模计算（对应元素arr1%arr2,除法取余),形状相同
# # print('求模:',np.mod(arr1,arr2))
# # 执行元素级别的比较运算，最终返回一个布尔型数组
# # greater大于,greater_equal大于等于,less,less_equal,equal,not_equal
# print('大于：',np.greater(arr1,arr2))
# # 执行元素级别的布尔逻辑运算符，相当于中缀运算符&,|,^
# # logical_and,logical_or,logical_xor(异或)
# print('逻辑运算：',np.logical_xor(arr1,arr2))
# # 求解对数组中的每个元素进行给定次数n的指数值  np.power(arr1,n)
# print('指数值：',np.power(arr1,3))
# # 等同于   arr1**3
# print(arr1**3)

# ３　聚合函数
# 聚合函数是对一组值进行操作，返回一个单一值作为结果的函数,加了axis返回一个数组．
# 当然聚合函数也可以指定对某个具体的轴进行数据聚合操作，常用的聚合操作有：
# 平均值mean，最大值max，最小值min，求和sum,标准差std等
# 二维数组的情况下，axis=0表示同列的数据进行聚合操作；axis=１表示同行的数据进行聚合操作
# arr1 = np.random.randint(1,9,size=(3,3))
# arr2 = np.random.randint(1,9,size=(3,3))
# print(arr1)
# print(arr2)
# print(arr1.min(axis=0))   #每列的最小值
# print(arr1.max())         #数组的最大值
# print(arr1.sum())          #数组的和
# print(arr1.mean(axis=1))   #每行的平均值
# print(arr1.std(axis=1))    #每行的标准差

# ４　where函数　
# np.where(condition,x,y)函数是三元表达式　　x if condition else y的矢量化版本
# condition是条件，符合条件返回x,不符合条件返回y
# where函数其实就是封装的一个列表推导式:[xv if c else yv for (c,xv,yv) in zip(condition,x,y)]
# arr= np.where([[True,False],[True,True]],[[1,2],[3,4]],[[9,8],[7,6]])
# print(arr)
# arr1 = np.random.randint(1,9,size=(3,3))
# arr2 = np.random.randint(1,9,size=(3,3))
# print(arr1)
# print(arr2)
# condition = arr1<arr2
# # print(condition)
# # arr3=[xv if c else yv for (c,xv,yv) in zip(condition,arr1,arr2)]   只能一维
# # print(arr3)
# arr4 = np.where(condition,arr1,arr2)
# print('where:',arr4)
# 案例：
# arr = np.array([[1,2,3,np.NaN],[1,2,3,np.pi],[1,2,3,np.e]])
# print(arr)
# 将数组中的nan和无穷数用0代替
# condition = np.isnan(arr)|np.isinf(arr)
# arr1 = np.where(condition,0,arr)
# print(arr1)
# ５　unique函数
# np.unique函数的主要作用是将数组中的元素进行去重操作(即只保留不重复的数据)
arr1 = np.array(['a','b','c','d','a','c'])
print(arr1)
arr2 = np.unique(arr1)
print('去重:',arr2)




















  







