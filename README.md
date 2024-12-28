



# 语法基础
## [code01.py](class01-syntax%2Fcode01.py)
### 注释
```python
# 单行注释

'''
多行注释（不推荐）
'''

"""
另一种多行注释（推荐）
"""
```
### 输出
```python
# 打印多个字符
print('hello world', '你好')
# 默认\n为结尾，可以修改
print('可以修改end', end=',')
```
### 变量
1. 标识符的规范：见名知其意  
2. 标识符命名规范    
2.1 只能由数字、字母、下划线组成   
2.2 不能以数字开头   
2.3 不能是关键字   
2.4 区分大小写   
3. 变量名的命名规范   
3.1 驼峰命名：userName   
3.2 下划线  
### 数值类型
1. 整型：int
2. 浮点型：float
3. 布尔型：bool  
### 字符串
1. 字符串连接：+  
2. 重复输出字符串：*   
3. in、not in操作符
4. r转译字符
### 格式化输出
按照我们想要输出的格式，先定义一个模板，照着模板输出  
1. 注意%f保留小数位的写法  
```python
age = 18
name = "Wil"
# 保留1位小数就是%.1f，其他同理
height = 170.3
print("我的名字是%s，我的年龄是%d，我的身高是%.1fcm" % (name, age, height))
```   
2. format()   
2.1 不带数字编号{}  
```python
age = 18
name = "Wil"
print("My name is {}, my age is {}".format(name, age))
```  
   2.2 带数字编号{0} {1} 
```python
age = 18
name = "Wil"
print("My name is {0}, my age is {1}, my brother's name is {0} too".format(name, age))
```  
   2.3 设置参数  
```python
print("用户名{userName} 密码是{pwd}".format(userName="root", pwd="123"))
```  
3. f{'表达式'}
```python
age = 18
name = "Wil"
print(f'My name is {name}, my age is {age}')
```

## [code02.py](class01-syntax%2Fcode02.py)
### 转义字符
### 运算符
1. // 取整除，返回除法的整数部分（商）。例如9//2=4  
2. ** 幂，又称次方、乘方。例如2**3=8  
3. += 例如a+=b等价于 a = a+b  
4. -= 例如a-=b等价于 a = a-b  
5. /=、*=、//=、**=、%= 同理
### 类型转换
1. 数值转str：str(num)
2. str转整数：int(str)，其他同理
### 输入
input函数
### if语句
```python
score = 50
if score>=80:
    print("优秀")
elif 60 <= score < 80:
    print("及格")
else:
    print("不及格")
```
### 逻辑运算符
and or not
### random类
1. random.random()：随机生成一个[0,1)之间的浮点数。
2. random.randint(a,b)：随机生成[a,b]范围内一个整数。
3. random.randrange(a,b,step)  
3.1 不指定step，随机生成[a,b)范围内一个整数。  
3.2 指定step，step作为步长会进一步限制[a,b)的范围，比如randrange(0,11,2)意即生成[0,11)范围内的随机偶数。  
3.3 不指定a，则默认从0开始。  
4. random.uniform(a,b)：产生[a,b]范围内一个随机浮点数。  
5. random.choice(seq)：从非空序列中随机选取一个数据并带回，该序列可以是list、tuple、str、set。  
```python
import random
# 随机输出”石头“、”剪刀“、”布“
myList = ["石头","剪刀", "布"]
print(random.choice(myList))
```    
### while循环
```python
i = 0
while i < 10:
    print(f"i= {i}")
    if i % 2 == 0:
        print(f"这是偶数：{i}")
    i += 1
```
### range函数
range(a, b, step)  
1. 表示[a, b)范围的整数  
2. a不填默认为0  
3. step: 每次跳跃的间距，不填默认为1  
```python
for i in range(5):
    print(i)
# 0 1 2 3 4
```
### for循环
```python
# 求1——100累加和
sum = 0
for i in range(1, 101):
    sum += i
print(sum)
```  
1. break关键字：和Java同理
2. continue关键字：和Java同理  

## 字符串
### [code03_str.py](class01-syntax%2Fcode03_str.py)
### 字符编码
字符编码的本质是二进制数据与语言文字的一一对应关系  
### 几种字符编码
1. unicode：兼容万国语言
2. utf-8：unicode的实现方式之一，优势是对不同的字符用不同的长度来表示
3. gbk：专门解决中文编码，每个字符占2字节
4. utf-8中一个英文/数字占用一个字节，一个汉字占3~4个字节
### encode编码
通过encode编码可以将字符转换为二进制字节流   
```python
str1 = "hello world"
stream = str1.encode("utf-8") # 默认utf-8
print(type(stream)) # <class 'bytes'>
```  
直接将字符串用二进制流表示
```python
s1 = b"hello"
print(type(s1)) # <class 'bytes'>
```
### decode解码
通过decode将二进制字节流转换为字符串
````python
# decode解码
s2 = b"hha"
print(s2.decode("utf-8"))
````
### 索引
字符串中的索引即下标，从0开始
```python
s3 = "abcd"
print(s3[0]) # a
print(s3[3]) # d
```  
在python中不仅支持顺序索引，同时还支持倒序索引，倒序从-1开始
```python
s3 = "abcd"
print(s3[-1]) # d
print(s3[-2]) # c
```
### 切片
字符串切片语法：[起始索引:结束索引:步长]，范围左闭右开，步长默认为1  
````python
name = "class_name_peter"
print(name[6:10:1]) # name
print(name[6:10:2]) # nm
print(name[:]) # class_name_peter
print(name[-1:3:-1]) # retep_eman_s
````
1. 切片区间为左闭右开
2. 步长可以控制查找方向，步长为正时表示从左向右定位，步长为负数表示从右往左定位
3. 切片时索引超出范围不会报错，查找范围截止至最后一位
4. 索引取值方向和步长方向要保持一致，否则不会取到值
### 字符串的常用操作
1. find(子串, startIndex, endIndex)  
子串是否在字符串中，如果在返回第一次找到时的索引值，否则返回-1   
可以通过startIndex、endIndex指定查找范围
```python
mytest = "this is my test"
print(mytest.find("this")) # 0
print(mytest.find("hello")) #-1
```
2. index(子串, startIndex, endIndex)     
跟find非常相似，不同点是，当查找不存在时，该方法会报错
```python
mytest = "this is my test"
print(mytest.index("this")) # 0
print(mytest.index("hello")) # ValueError: substring not found
```
3. count(子串, startIndex, endIndex)       
查找子串出现在字符串中的次数  
```python
mytest = "this is my test"
print(mytest.count("t")) #3
print(mytest.count("hello")) #0
```
4. replace(旧字串, 新字串, 替换次数)
````python
test1 = "this is test1"
print(test1.replace("t", "T")) # This is TesT1
print(test1.replace("t", "T", 1)) # This is test1
````
5. split(子串, 切的次数)
````python
test2 = "what a fuck this world"
print(test2.split(" ")) # ['what', 'a', 'fuck', 'this', 'world']
print(test2.split(" ", 1))  # ['what', 'a fuck this world']
````
6. capitalize()   
只将首字母大写  
```python
test1 = "this is test1"
print(test1.capitalize())  # This is test1
```
7. lower()  
将所有大写变为小写   
```python
test3 = "HELLO WORLD"
print(test3.lower())  # hello world
```  
8. upper()  
将所有小写变为大写  
```python
test4 = "how are you"
print(test4.upper())  # HOW ARE YOU
```
9. title()  
将每个单词首字母变大写  
````python
test4 = "how are you"
print(test4.title())  # How Are You
````
10. islower()  
````python
test4 = "how are you"
print(test4.islower())  # True
test5 = "How are you"
print(test5.islower())  # False
````
11. isupper()

````python
test3 = "HELLO WORLD"
test5 = "How are you"
print(test3.isupper())  # True
print(test5.isupper())  # False
````
12. isdigit()  
判断字符串是否是数字
```python
numStr = "124"
print(numStr.isdigit())  # True
strNum = "3.1E5"
print(strNum.isdigit())  # False
```
13. startswith(子串)  
````python
test5 = "How are you"
print(test5.startswith("how"))  # False
print(test5.startswith("How"))  # True
````
14. endswith(子串)
````python
test5 = "How are you"
print(test5.endswith("you"))  # True
````
15. join
```python
code = "python"
print("*".join(code))  # p*y*t*h*o*n
```
16. strip()  
只能删除字符串<font color=red>首尾</font>的空格
17. lstrip()  
删除字符串开头的空格
18. rstrip()  
删除字符串末尾的空格 

## 列表
### [code04_list.py](class01-syntax%2Fcode04_list.py)
### 列表基本性质
1. 列表的定义：中括号包围所有元素，每个元素间用逗号分割
2. 列表的性质：有序、存储多个元素，元素可以是不同类型
3. 列表的下标从左往右是从0开始，也可以倒着来，即从右往左从-1开始
4. 索引超出列表长度会报错
```python
li = ["a", "b", 121, "hello"]
print(li[1])  # b
print(li[-2])  # 121
print(li[10])  # IndexError: list index out of range
```
### 列表的遍历
1. for循环遍历
````python
li = ["a", "b", 121, "hello"]
for i in li:
    print(i)
````
2. while循环遍历
````python
li = ["a", "b", 121, "hello"]
i = 0
while i < len(li):
    print(li[i])
    i += 1
````
### 列表添加元素
1. 直接相加：+
````python
language = ["Python", "Java", "C++"]
numList = [1990, 1222, 5554]
language = language + numList
print(language)  # ['Python', 'Java', 'C++', 1990, 1222, 5554]
````
2. insert(index, obj): 在index前面插入obj元素    
2.1 当index是正数时，会在index下标处插入元素    
2.2 当index是负数时，会在index前面插入元素  
2.3 当index大于列表长度时，会在首/尾插入元素  
2.4 元组会作为一个整体插入   
````python
language = ["Python", "Java", "C++"]
language.insert(1, "Go")
language.insert(10, "C#")
language.insert(-1, "JS")
language.insert(-10, "html")
print(language)  # ['html', 'Python', 'Go', 'Java', 'C++', 'JS', 'C#']
t = ("Shell", "C")
language.insert(0, t)
print(language)  # [('Shell', 'C'), 'html', 'Python', 'Go', 'Java', 'C++', 'JS', 'C#']
````
3. append(obj): 直接在列表末尾添加元素
4. extend(obj): 也是在末尾添加元素，但是会识别obj中的元素拆分成单个的
````python
li1 = ["aaa", "bbb"]
li2 = ["ddd", "tttt"]
li1.append(li2)
print(li1)  # ['aaa', 'bbb', ['ddd', 'tttt']]
li1.extend(li2)
print(li1)  # ['aaa', 'bbb', ['ddd', 'tttt'], 'ddd', 'tttt']
````
### 列表修改元素
修改元素的本质就是赋值   
1. 修改单个元素  
````python
breakfast = ["豆浆", "油条"]
breakfast[0] = "豆腐脑"
print(breakfast)  # ['豆腐脑', '油条']
````
2. 修改一组元素：<font color = red>注意左闭右开</font>

````python
breakfast = ["豆浆", "油条", "包子", "馒头"]
breakfast[1:4] = ["鸡蛋"]  # 左闭右开
print(breakfast)  # ['豆浆', '鸡蛋']
````
3. 对空切片赋值操作

````python
breakfast = ["豆浆", "油条", "包子", "馒头"]
breakfast[2:2] = ["鸡蛋"]  # 左闭右开
print(breakfast)  # ['豆浆', '油条', '鸡蛋', '包子', '馒头']
````
### 列表删除元素
1. del
````python
r = list("hello")
print(r)  # ['h', 'e', 'l', 'l', 'o']
del r[0]
print(r)  # ['e', 'l', 'l', 'o']
del r[0:2]  # 左闭右开
print(r)  # ['l', 'o']
del r
print(r)  # NameError: name 'r' is not defined
````
2. pop(index)：下标删除，如果不填下标则默认删除列表中最后一个元素
````python
nums = [1, 2, 3, 4, 5]
p = nums.pop()
print(p)  # 5
print(nums)  # [1, 2, 3, 4]
````
3. remove(obj)
````python
mm = ["Hello", "world", "you"]
mm.remove("you")
print(mm)  # ['Hello', 'world']
````
4. clear：删除所有元素
````python
mm = ["Hello", "world", "you"]
mm.clear()
print(mm)  # []
````
### 列表查找元素
1. in/not in
````python
find = ["Hello", "world", "you"]
print("he" in find)  # False
print("you" in find)  # True
print("lla" not in find)  # True
````
2. count(obj)：统计obj元素出现在列表中的次数   
可用此方法来判断某个元素是否在列表中  
3. index(obj, start, end)：查找obj元素在列表中的索引位置，如果元素不存在则报错
````python
find = ["Hello", "world", "you"]
print(find.index("he"))  # ValueError: 'he' is not in list
````
### 列表排序
1. reverse
````python
kk = [1, 2, 3, 4]
kk.reverse()
print(kk)  # [4, 3, 2, 1]
````
2. sort()  
2.1 只能用于列表排序   
2.2 会直接改变原列表的顺序
````python
hh = [5, 2, 65, 4, 8, 1]
hh.sort()  # 默认从小到大
print(hh)  # [1, 2, 4, 5, 8, 65]
hh.sort(reverse=True)  # 从大到小
print(hh)  # [65, 8, 5, 4, 2, 1]
````
3. sorted()     
3.1 python内置的   
3.2 不会修改原数组的值
````python
ff = [1, 4, 2, 9, 3]
ff1 = sorted(ff)
print(ff)  # [1, 4, 2, 9, 3]
print(ff1)  # [1, 2, 3, 4, 9]
````
### 列表推导式
````python
# 给列表中的每个元素都乘以2
dd = [1, 2, 3, 4]
print([i * 2 for i in dd])  # [2, 4, 6, 8]
````
## 元组
### [code05_tuple.py](class01-syntax%2Fcode05_tuple.py)
元组是不可变的list类型，不可以增删改。   
意义：因为元组不支持增删改，所以提高了代码编写的安全性，如果有只读场景，可以考虑使用元组。    
### 元组的定义   
定义单个元素的元组时要加逗号
````python
# 元组的定义
tup = (1, 3, 4)
# 定义单个元素的元组时要加逗号
tup1 = (1)
print(type(tup1))  # <class 'int'>
tup1 = (1,)
print(type(tup1))  # <class 'tuple'>
````
### 元组的操作
1. count
2. index
3. len
```python
tup1 = (1,)
print(len(tup1))  # 1
```
4. 元组”可变“的情况
````python
tt = (3, 5, [99, 88, 77], 6)
tt[2][0] = 66
print(tt)  # (3, 5, [66, 88, 77], 6)
````
## 字典
### [code06_dictionary.py](class01-syntax%2Fcode06_dictionary.py)
就是HashMap
````python
# 定义字典
dic1 = {}
dic2 = {"name": "ll", "age": 18}
dic3 = dict()
````
### 字典增删改查
````python
dic3 = dict()

# 添加元素
dic3["id"] = 1
dic3["name"] = "Lucy"
print(dic3)  # {'id': 1, 'name': 'Lucy'}

# 修改元素
dic3["name"] = "Peter"
print(dic3)  # {'id': 1, 'name': 'Peter'}

# 查找
print(dic3["name"])  # Peter

# 删除元素
del dic3["name"]
print(dic3)  # {'id': 1}

# 清空字典
dic3.clear()
print(dic3)  # {}
````
### 字典常用操作
1. len
````python
map = {"id": 2}
print(len(map))  # 1
````
2. keys()、values()
````python
map = {"id": 2, "age": 20, "name": "MyName"}
keys = map.keys()
for k in keys:
    print(k)

values = map.values()
for v in values:
    print(v)
````
3. items()   
一对一对的遍历
```python
map = {"id": 2, "age": 20, "name": "MyName"}
items = map.items()
for key, value in items:
    print(key, value)

# 输出如下
# id 2
# age 20
# name MyName
```
## 集合
### [code07_set.py](class01-syntax%2Fcode07_set.py)
相当于Java中的Set集合，元素无序且不重复
### 集合的定义
````python
# 定义集合
s1 = {10, 20, 30}
print(type(s1))  # <class 'set'>
# 字符串转集合
s2 = set("hello")
print(s2)  # {'h', 'l', 'o', 'e'}
# 定义一个空集合
s3 = set()
````
### 集合添加元素
1. add()
````python
s3 = set()
s3.add("zoo")
s3.add(1)
s3.add(1)  # 自动去重
print(s3)  # {'zoo', 1}
````
2. update(obj)：obj必须是可迭代对象（列表、集合、字典、元组等）   
当update的元素是字典时，只添加key
````python
s4 = set()
s4.update([10, 11])
s4.update((12, 56))
print(s4)  # {56, 10, 11, 12}
s4.update({"name": "Pe"})
print(s4)  # {56, 10, 11, 12, 'name'}
````
### 集合删除元素
1. remove(obj): 删除指定元素，如果不存在则报错
2. discard(obj): 删除指定元素，如果不存在不会报错
3. pop(): 随机删除一个元素，返回删除的元素
### 交集、并集
````python
l = {1, 2, 3, 4}
m = {3, 4, 5, 6}
# 求交集
print(l & m)  # {3, 4}
# 求并集
print(l | m)  # {1, 2, 3, 4, 5, 6}
````
## 阶段总结
### 运算符
|运算符|描述|支持的容器类型|
|:----|:----|:----|
|+|合并|字符串、列表、元组|
|*|复制|字符串、列表、元组|
|in|元素是否存在|字符串、列表、元组、字典|
|not in|元素是否不存在|字符串、列表、元组、字典|
### 公共方法
|公共方法|描述|支持的容器类型|
|:----|:----|:----|
|len|求长度，即元素个数|字符串、列表、元组、字典、集合|
|max|求最大元素|列表、元组、集合|
|min|求最小值|列表、元组、集合|
|enumerate|将下标和数据一一列出来|列表、元组|

## [code08.py](class01-syntax%2Fcode08.py)
### 类型转换
1. 转字符串：str(o)
2. 转列表：list(o)
3. 转元组：tuple(o)
4. 转集合：set(o)
5. 转字典：dict(o)
```python
int = 5
# 整数转为字符串
s = str(5)
# 字符串转为list
l = list(s)
# 字符串转为元组
tu = tuple(s)
# 字符串转为集合
set1 = set(s)
# list转为字符串
se = str(l)
# list转元组
tu1 = tuple(l)
# list转集合
se1 = set(tu1)

# 转字典（特殊）
x = ["a1", "b1", "c1", "d1"]
y = ["a2", "b2", "b3"]
z = zip(x, y)
print(dict(z))
```
### 深浅拷贝
1. 深拷贝   
1.1 数值类型、字符串类型当值相等时，两个变量公用一个内存地址
1.2 列表、集合等类型变量赋值操作会使内存地址一致
````python
a = 10
b = 10
print(id(a))  # 140705617148632
print(id(b))  # 140705617148632
s = "hello"
t = "hello"
print(id(s))  # 2905618815600
print(id(t))  # 2905618815600

l = [1, 2, 3]
m = l
print(id(l))  # 2221094530688
print(id(m))  # 2221094530688
````
2. 浅拷贝   
使用copy模块   
````python
import copy

u = [1, 2, 3]
v = copy.copy(u)
print(id(u))  # 2444626097664
print(id(v))  # 2444626493056
````
### 不可变对象
简单说就是当修改了变量的值之后，变量的内存地址也会发生改变，这样的数据类型就是不可变的。  
python中数值类型、string类型、元组都是不可变对象。   
### 可变对象
那就是当修改了变量的值之后，变量的内存地址不会发生改变。  
python中列表、集合、字典都是可变对象

## 函数
### [code09_function.py](class01-syntax%2Fcode09_function.py)
### 函数的定义
1. 函数与方法的区别：函数是直接调用的，方法是对象调用的，是类里面的
2. 如果函数有多个返回值，那么将作为一个元组类型被返回
````python
# 定义函数
def sayHello():
    print("Hello world")


# 函数的调用
sayHello()


# 函数的返回值
def funa():
    return 10


print(funa())


# 多返回值
def funb():
    return 10, {"name": "Pe"}, [1, 2, 3]


f = funb()
print(type(f))  # <class 'tuple'>
````
### 函数的参数
1. 必填参数
2. 默认参数
3. 可选参数
4. 关键字参数
5. 命名关键字参数：*,后面的都是命名关键字参数，调用的时候要加key
````python
# 必填参数
def add(x, y):
    return x + y


# 默认参数
def encodefun(string, character="utf-8"):
    return string.encode(character)


# 不定长参数
def func(*args):
    print(type(args))  # <class 'tuple'>


func(1, 22, 4, 2)


# 关键字参数
def fund(**kwargs):
    print(kwargs)
    print(type(kwargs))


fund(name="Peter", age=18)


# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


person("Peter", 19, city="beijing", job="coder")
````
### 作用域
1. 名称空间   
1.1 内置名称空间：随着python解释器启动而产生，停止而回收。第一个被加载  
1.2 全局的名称空间：随着所在执行文件启动而产生，执行结束而回收，第二个被加载  
1.3 局部名称空间：随着函数的调用而产生，结束而回收。如函数的参数、函数内定义的变量   
2. 全局作用域：包含内置命名空间和全局命名空间   
3. 局部作用域：包含局部命名空间，在函数内可以使用的  
4. Python查找变量的顺序：局部命名空间-> 全局命名空间-> 内置命名空间   
### 全局变量和局部变量
````python
cup = 100  # 全局变量


def fune():
    cup = 200  # 局部变量
    print(f"fune print {cup}")  # fune print 200


def funf():
    print(f"funf print {cup}")  # funf print 100


fune()
funf()
````
global 关键字
````python
cup = 100  # 全局变量


def fune():
    global cup
    cup = 200  # 全局变量
    print(f"fune print {cup}")  # fune print 200


def funf():
    print(f"funf print {cup}")  # funf print 200


fune()
funf()
````
nonlocal 关键字
````python
water = 500


def fung():
    water = 700

    def funh():
        nonlocal water  # 申明water为外层的局部变量 即water=700
        print(f"funh print {water}")  # funh print 700
        water = 900

    funh()
    print(f"fung print {water}")  # fung print 900


fung()
print(f"water={water}")  # water=500
````
### 匿名函数
````python
funadd = lambda x, y: x + y
print(funadd(4, 5))  # 9
````
ifelse的lambda用法  
````python
funk = lambda x, y: x if x > y else y
print(funk(4, 5))  # 5
````
### 内置函数
1. abs(num) 求绝对值
2. sum(a,b,c...) 求和
3. zip 拉链函数
````python
a = [1, 2, 3, 4]
b = ["a", "b", "c", "d"]
z = zip(a, b)
# 然后就可以将z转成各种数据类型
print(dict(z))  # 转map {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# print(list(z))#转list [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# print(set(z))  # 转集合 {(4, 'd'), (2, 'b'), (3, 'c'), (1, 'a')}
````
4. map(fun, 可迭代对象)：映射函数，对可迭代对象中的每个元素进行映射，分别去执行函数fun
````python
funm = lambda x: x * x
li = [1, 2, 4, 8]
print(list(map(funm, li)))  # [1, 4, 16, 64]
````
5. reduce(fun, 可迭代对象)：对可迭代对象中的元素进行累计计算，执行函数fun
````python
from functools import reduce

li = [1, 2, 3, 4]
funadd = lambda x, y: x + y
print(reduce(funadd, li))  # 10
````
6. enumerate(可迭代对象)：用于将一个可迭代的对象组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中
````python
li = [1, 2, 3, 4]
for i, num in enumerate(li):
    print(i, num)
````
### 拆包
````python
# 拆包
def funl():
    return 1, 2, 3


a, b, c = funl()  # funl() 返回的是一个元组类型，这里将元组进行拆包
print(a, b, c)

# 元组拆包升级版
tu = (1, 2, 3, 4)
a, *b, c = tu  # 多变量赋值
print(f"a={a}")  # a=1
print(f"b={b}")  # b=[2, 3]
print(f"c={c}")  # c=4

# 列表拆包
li = [1, 2, 3, 4]
a, *b, c = li
print(f"a={a}")  # a=1
print(f"b={b}")  # b=[2, 3]
print(f"c={c}")  # c=4

# 字典拆包
map = {"name": "Peter", "age": 18}
a, b = map  # 对字典拆包只有键，没有值
print(a, b)  # name age
````
### 异常捕获
````python
# 异常捕获
def funm():
    print(hsfgss)


try:
    funm()
except Exception as e:
    print(f"发生异常：{e}")
else:
    print("没有发生异常，就会执行else模块")
finally:
    print("不管是否发生异常，都会执行的模块")
````
### 抛出异常
raise抛出异常
````python
def inputpwd():
    pwd = input("请输入长度超过6位的密码：")
    if (len(pwd) < 6):
        raise Exception("密码长度不足6位")
    return pwd


try:
    pwd = inputpwd()
    print(f"用户输入的密码为：{pwd}")
except Exception as e:
    print("发生异常：", e)
````
## 模块
### [code10_module.py](class01-syntax%2Fcode10_module.py)
### 内置模块
````python
# 查看内置模块
import builtins

print(dir(builtins))
````
### 第三方库
使用命令行导入：pip install 模块名   
使用PyCharm开发时，安装第三方库步骤如下：   
File -> Settings -> File -> Interpreter
![pipinstall.png](class01-syntax%2Fpipinstall.png)
### 自定义模块
```python
# 自定义模块
import tools.Timetools as timetools

print(timetools.now())
print(timetools.my_time_zone)
```
### __name__和__main__

### 包
没啥可讲的

## [code11.py](class01-syntax%2Fcode11.py)
### 递归函数
```python
# 0——x累加
def funa(x):
    if x == 0:
        return 0
    return funa(x - 1) + x

print(funa(3))
```
### 函数的引用
````python
def funa(x):
    if x == 0:
        return 0
    return funa(x - 1) + x

print(funa(3))
res = funa  # 函数引用，就相当于给funa起了个别名
print(res(3))
````
### 闭包
### 装饰器   
为什么使用装饰器？    
可以对不同的函数进行装饰，而避免直接修改业务代码。
````python
def logger(func):
    def wrapper(*args):
        print(f"开始执行函数 {func.__name__}")
        return func(*args)

    print(f"函数 {func.__name__} 执行完毕")
    return wrapper  # 装饰器必须返回内部方法名

def add(x, y):
    return x + y

fn = logger(add)
print(fn(10, 20))
````
装饰器的语法糖使用方式：
````python
def logger(func):
    def wrapper(*args):
        print(f"开始执行函数 {func.__name__}")
        return func(*args)

    print(f"函数 {func.__name__} 执行完毕")
    return wrapper  # 装饰器必须返回内部方法名

@logger
def add(x, y):
    return x + y
@logger
def printm(x, y, z):
    print(x, y, z)

print(add(10, 20))
printm(1, 2, 3)
````
### 回调函数
```python
call = lambda: print("call")

def funx(fun, *args):
    print(f"处理逻辑 {args}")
    # 处理完毕调用回调函数
    fun()

funx(call)
```

# 语法进阶
## 面向对象
### [code01_object.py](class02-advanced%2Fcode01_object.py)
### 类的定义
1. 关键字class
2. 类名：一般使用驼峰法，首字母大写，私有类可用一个下划线开头
3. object是最顶极父类
4. 属性、方法
````python
class Hero(object):
    name = "Hero"  # 属性

    def info(self):  # self表示实例本身（相当于Java的this？）
        print("I am the class Hero")
````
### 创建对象
````python
hero = Hero()
print(hero.name)  # Hero
hero.info()  # I am the class Hero
````
### 类的属性
1. 查看类的属性
2. 类的属性的增删改查
````python
class Student():
    name = "Peter"

    def info(self):
        print("xxx")


print(Student.__dict__)  # 查看类的属性
print(Student.__dict__["name"])  # 查看单个属性
print(Student.name)  # 查看属性
Student.age = 18  # 新增属性
Student.name = "Lucy"  # 修改属性
del Student.age  # 删除属性
````
### 构造函数
实例化一个对象。

```python
class Order:
    def __init__(self, id, costprice, sellprice):  # 构造函数
        self.id = id
        self.costprice = costprice
        self.sellprice = sellprice

    def getprofit(self):
        return self.sellprice - self.costprice


order = Order(1, 32.1, 68.2)
print(f"订单 {order.id} 的利润是{order.getprofit()}")
```
### 析构函数
销毁一个对象。  
1. 自动调用：析构函数会在程序退出之前系统自动调用。
```python
class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):  # 析构函数
        print(f"{self.name}被销毁了")


person = Person("kk")
```
2. 手动调用
```python
class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name}被销毁了")


person = Person("kk")

del person
```
### \_\_str__()
相当于Java的toString()方法
### 封装
面向对象的思想就是封装
### 私有属性和方法
#### 下划线在Python中的作用
1. _xx 表示私有属性或方法，但是实际上类和对象也可以访问
2. __xx 真正的私有属性或方法，类、子类及对象不能直接访问，只能在类的内部访问
3. \_\_xx__ 用户名字空间的魔法对象或属性
4. xx__ 用于避免与Python关键词的冲突
#### 私有属性和方法
私有属性和方法只能在该类内部调用，其外部或子类都不能直接调用
```python
class A:
    _name = "LL"
    __age = 18  # 私有属性

    def get_age(self):
        return self.__age

    def set_sex(self, sex):
        self.__sex = sex

    def get_sex(self):
        return self.__sex

    def __printfoo(self):  # 私有方法
        print("foo")

    def printsth(self):
        self.__printfoo()  # 调用私有方法
        print("sth.")


a = A()
print(A._name)  # LL
# print(A.__age)  # AttributeError: type object 'A' has no attribute '__age'. Did you mean: '_A__age'?
print(a._name)  # LL
# print(a.__age)  # AttributeError: 'A' object has no attribute '__age'. Did you mean: '_A__age'?
print(a.get_age())  # 正确访问私有属性的方式
a.printsth()
a.set_sex("男")
print(a.get_sex())
```
### 继承
#### 单继承    
单继承书写方式：class 子类名(父类名):
```python
class B(A):
    pass  # 什么都不写


b = B()
b.printsth()
```
#### 多继承
python还可以继承多个类（好像一般不推荐?）
````python
class A1:
    def printa1(self):
        print("a1")


class B(A, A1):
    pass  # 什么都不写


b = B()
b.printsth()
b.printa1()
````
#### 继承传递
```python
class C:
    def printc(self):
        print("c")
class C1(C):

    def printc1(self):
        print("c1")
class C2(C1):
    pass

c2 = C2()
c2.printc()
c2.printc1()
```
#### 继承重写
1. 直接重写，如Dog子类重写say方法
2. 子类重写方法中使用到了父类的能力，通过super()调用
````python
class Animal:
    def say(self):
        print("")

    def eat(self):
        print("Eat meat")


class Dog(Animal):
    def say(self):
        print("Wangwang")

    def eat(self):
        super().eat() #通过super()调用父类方法
        print("Eat noodle")
````
## [code02.py](class02-advanced%2Fcode02.py)
### 多继承
Python中子类可以继承多个父类，并且具有所有父类的非私有属性和方法。   
这个在上面[多继承](#多继承)中已经写了示例。   
下面看看多继承执行的顺序问题：
````python
class A:
    def foo(self):
        print("A foo")
class B:
    def foo(self):
        print("B foo")
class C(A, B):
    pass
c = C()
c.foo()  # A foo
# 查看类的执行顺序
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
````
### 多态
多态：一种事物的多种形态。   
在Python中多态实际指的就是继承一个抽象类，然后子类对父类的方法实现不同的版本。   
举一些多态的例子：
````python
# 1. +的多态性
print(1 + 2)  # 此处表示数学相加
print("hello" + "world")  # 此处表示字符串拼接
# 2. len函数的多态性
print(len("world"))
print(len([1, 2, 3]))
````
自己实现一个多态：   
多态的实现关键在于process(e, x, y)函数的实现。
````python
class E:
    def process(self):
        pass


class E1(E):
    def process(self):
        print("process E1")


class E2(E):
    def process(self):
        print("process E2")


def process(e, x, y):
    print(f"process {x}")
    e.process()
    print(f"process {y}")


e1 = E1()
process(e1, 1, 2)

e2 = E2()
process(e2, 3, 4)
````
### 类方法
总结一句话就是Python中的类方法就相当于Java中的静态方法，不用实例化对象而直接使用 类名.方法名 调用。
1. 类方法的使用场景    
1.1 当方法中需要使用类对象时（如访问私有属性），定义类方法    
1.2 类方法一般和类属性配合使用
2. 类方法定义方式
````python
class F:
    foo = "foo"

    @classmethod  # 类方法必须使用该注解申明
    def run(cls):  # 类方法的第一个参数必须时cls
        print(f"run {cls.foo}")

# 调用方式
F.run()  # run foo
f = F()
f.run()  # run foo
````
3. 用类方法对类属性进行读写
````python
class F:
    foo = "foo"

    @classmethod
    def get_foo(cls):
        return cls.foo

    @classmethod
    def set_foo(cls, foo):
        cls.foo = foo
````
### 静态方法
````python
class M:
    @staticmethod  # 静态方法申明方式
    def foo(x, y):
        print(f"process {x} and {y}")
````
### \_\_new__()方法
创建对象时第一个被调用的方法。
````python
class N(object):
    def __new__(cls, *args, **kwargs):
        print("创建对象前执行")
        return object.__new__(cls)  # 如果不返回，则实例不会初始化，即不能执行__init__方法

    def __init__(self):
        print("初始化对象前执行")


n = N()
"""
运行结果：
创建对象前执行
初始化对象前执行
"""
````
## 单例模式
### [code03_singleton.py](class02-advanced%2Fcode03_singleton.py)
### 实现单例的5种方法
1. \_\_new__()实现单例模式
````python
class DateUtil(object):
    ins = None

    def __new__(cls, *args, **kwargs):
        if cls.ins is None:
            cls.ins = super().__new__(cls)
        return cls.ins

d1 = DateUtil()
d2 = DateUtil()
print(id(d1))
print(id(d2))
````
2. 通过类方法实现单例模式
````python
class JsonUtil(object):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


j1 = JsonUtil.get_instance()
j2 = JsonUtil.get_instance()
print(id(j1))
print(id(j2))
````
3. 通过装饰器实现单例模式
````python
def outer(fn):
    _ins = {}

    def inner():
        if fn not in _ins:
            _ins[fn] = fn()
        return _ins[fn]

    return inner


@outer
class XxxUtil(object):
    pass


xx1 = XxxUtil()
xx2 = XxxUtil()
print(id(xx1))
print(id(xx2))
````
4. 通过导入模块时实现    
Python中的模块是天然的单例模式，import一次即可。
5. 通过元类实现   
hasattr(__object, __name):判断对象object中是否有属性名或方法名叫name的。
通过元类实现单例，就是在__new()__方法中吧判断None的条件换成使用hasattr
````python
class A(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "ins"):
            cls.ins = super().__new__(cls)
        return cls.ins


a1 = A()
a2 = A()
print(id(a1))
print(id(a2))
````
### 魔术方法
1. \_\_方法名__ 这类方法叫做魔术方法。
2. 常见的魔术方法，通过print(dir(A))来查看，其中A是一个类
3. 一些常见的魔术方法  
3.1 \_\_doc__: 表示类的描述信息   
3.2 \_\_module__: 所在模块名   
3.3 \_\_class__: 所在类   
3.4 \_\_call__: 能直接用实例()调用
````python
class B(object):
    def __call__(self, *args, **kwargs):
        print("这是call方法")


B()()  # 这是call方法
````
3.5__dict__ 查看类或对象中的所有属性。__dict__是dir()的子集，许多内建类如list没有__dict__属性。

## 文件
### [code04_file.py](class02-advanced%2Fcode04_file.py)
### 文件的基本操作
#### 读取文件
1. 相对路径
````python
# 相对路径
f1 = open("Test.txt", "rb")
try:
    txt = f1.read()
    print(txt.decode("utf-8"))
finally:
    f1.close()
````
2. 绝对路径
```python
# 绝对路径
f2 = open(r"D:\Foo.txt", "rb")  # windows下用r转义
try:
    content = f2.read()
    print(content.decode("utf-8"))
finally:
    f2.close()
```
3. readline和readlines
```python
with open("Foo2.txt", encoding="utf-8") as f:
    while True:
        txt = f.readline()
        if not txt:
            break
        print(txt, end="")

with open("Foo2.txt", encoding="utf-8") as f:
    print(f.readlines())  # ['追加一段文字\n', '追加一段文字\n', '追加一段文字\n', '追加一段文字\n', '追加一段文字\n']
```
#### 写文件
1. 以二进制覆盖写
````python
# 以二进制覆盖写
f3 = open("Foo.txt", "wb")
try:
    content = """
    这是中文，
    This is English
    """
    f3.write(content.encode(encoding="utf-8"))
finally:
    f3.close()

print("*" * 50)
# 以二进制读出来
f4 = open("Foo.txt", "rb")
try:
    print(f4.read().decode(encoding="utf-8"))
finally:
    f4.close()
````
2. 以二进制追加写
````python
f3 = open("Foo.txt", "ab")
try:
    content = "追加一段文字\n"
    f3.write(content.encode(encoding="utf-8"))
finally:
    f3.close()
````
#### with关键字
with的作用：相当于try...finally，只不过将finally中的close自动执行了
````python
with open("Foo.txt", "rb") as f5:
    print(f5.read().decode(encoding="utf-8"))

# 查看f5的关闭状态
print(f5.closed)  # True
````
#### tell方法和seek方法
````python
with open("Foo.txt", "rb") as f:
    print(f.read(12).decode(encoding="utf-8"))  # 注意这里一个汉字4字节
    print(f.tell())  # tell方法返回当前指针所在位置 12

    f.seek(0, 0)  # 第一个0是偏移量，第二个0是指针指向的开始位置
    print(f.tell())  # 0
````
### 文件备份
````python
class CopyFile:
    @staticmethod
    def copy(filepath):
        index = filepath.rfind(".")
        new_file_path = None
        if index == -1:
            new_file_path = filepath + "(备份)"
        else:
            new_file_path = filepath[:index] + "(备份)" + filepath[index:]
        print(new_file_path)
        f1 = open(filepath, "rb")
        f2 = open(new_file_path, "wb")
        try:
            while True:
                content = f1.read(1024)
                if len(content) == 0:
                    break
                f2.write(content)
        finally:
            f1.close()
            f2.close()
````
### 目录操作
````python
import os

# 文件（夹）重命名
os.rename("Foo2.txt", "Foo2.txt")
# 创建文件夹
os.mkdir("D:/wilia")  # 只能创建一层
# 删除文件
os.remove("D:/wilia")
# 获取当前目录
print(os.getcwd())
# 改变默认路径
os.chdir("../")
# 获取目录列表
print(os.listdir())
````
## 迭代器
### [code05_iterator.py](class02-advanced%2Fcode05_iterator.py)
### 可迭代对象Iterable
可迭代对象的本质就是都是collections模块里的Iterable类创造出来的实例。
1. 查看是否为可迭代对象
````python
from collections.abc import Iterable

print(isinstance([1, 2], Iterable))  # True
````
### 迭代器Iterator
1. 使用iter()方法将可迭代对象创建迭代器
2. 使用__next()__方法进行遍历
```python
list = [1, 4, 5, 2]
it = iter(list)
print(it.__next__())
print(next(it))  # next()方法内部调用了__next__方法
```
### 迭代器协议
1. 迭代器对象是实现了迭代器协议的对象
2. 迭代器对象必须实现\_\_iter__()方法和\_\_next__()方法
3. 自定义迭代器
```python
from collections.abc import Iterable, Iterator

class Person:
    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        self.n += 1
        return self.n


print(isinstance(Person(), Iterator))  # True
```
### 生成器Generator
生成器是特定的迭代器。  
迭代器用于从数据集中取出元素，而生成器用于“凭空”生成元素，它不会一次性将所有元素都生成，而是按需一个一个的生成，所以从头到尾只需要占用一个元素空间。   
1. 如何生成生成器：使用yield关键字
````python
"""
D:/Foo.txt中的内容如下：
Hello world
Hello Python
你好中国
你好
Hello u
hello mimi
"""
def search(filepath, word):
    with open(filepath, encoding="utf-8") as f:
        for item in f:
            if word in item:
                yield item


t = search("D:/Foo.txt", "Hello")
print(next(t), end="")
print(next(t), end="")
print(next(t), end="")
# print(next(t), end="")  # 读结束时，报异常StopIteration
````
2. 生成器表达式   
生成器表达式的创建很简单，只需要吧列表生成式中的[]改成()即可
````python
# 列表推导式
list1 = [i * 2 for i in range(3)]
print(list1)  # [0, 2, 4]

# 创建生成器表达式
list2 = (i * 2 for i in range(3))
print(next(list2))
print(next(list2))
print(next(list2))
````
3. 使用生成器执行速度更快
````python
import time
def sum1():
    s1 = time.time()
    print(sum([i for i in range(10000000)]))
    print(f"sum1执行时间: {time.time() - s1}")  # sum1执行时间: 0.40175843238830566


def sum2():
    s1 = time.time()
    print(sum((i for i in range(10000000))))
    print(f"sum2执行时间: {time.time() - s1}")  # sum2执行时间: 0.3052406311035156


sum1()
sum2()
````
## 多线程
### 创建多线程
### [code06_thread.py](class02-advanced%2Fcode06_thread.py)
使用threading模块中的Thread类创建出实例对象，然后通过start()方法真正的去产生一个新的线程。    
Thread的参数：
1. group: 线程组
2. target: 执行的目标任务名（可以是方法、继承了Thread的子类）
3. args: 以元组的方式给执行任务传递参数
4. *args: 传任意多个参数
5. kwargs: 以字典方式给执行任务传递参数
6. name: 线程名      

创建多线程步骤：   
1. 导入模块 threading
2. 创建子线程 Thread()类
3. 设置守护线程 setDaemon(Ture) 设置守护线程时，主线程执行完了，子线程也会跟着结束
4. 启动子线程 start()
5. 阻塞主线程 join()：调用方式t1.join()，t1为子线程，阻塞主线程，主线程会等待子线程t1执行完再执行下面的代码
     
### 互斥锁
### [code07_lock.py](class02-advanced%2Fcode07_lock.py)
1. 创建一把锁：local = Lock()
2. 上锁：local.acquire()；解锁：local.release()
3. 上锁和解锁必须成对出现，上完锁解锁之后才能继续上锁，否则会死锁

## 多进程
### [code08_process.py](class02-advanced%2Fcode08_process.py)
### 创建多进程
使用multiprocessing模块中的Process创建多进程实例，其参数如下：   
1. target: 调用对象，即子进程执行的任务
2. args: 给target指定的函数传递的参数，以元组形式传递
3. kwargs: 表示调用字典对象
4. name: 子进程名字
5. group: 指定进程组   

常见属性  
1. name: 当前进程别名，默认Process-N
2. pid: 进程号
3. ppid: 父进程号     

windows查看进程号  
```shell
tasklist
# 然后ctl+shift+F搜索
```
### 进程常用方法
1. start() 启动进程实例
2. is_alive() 判断是否活着
3. join([timeout]) 等待子进程执行结束（在当前位置阻塞主进程）
4. terminate() 不管任务是否完成，立马终止子进程

### 进程之间不共享全局变量
```python
from multiprocessing import Process
list1 = []
def listadd():
    for i in range(10):
        list1.append(i)
    print(list1)
def listprint():
    print(list1)
if __name__ == "__main__":
    p1 = Process(target=listadd)
    p2 = Process(target=listprint)
    p1.start()
    p1.join()
    p2.start()
"""
运行结果：
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[]
"""
```
### 进程间的通信
#### 队列 Queue
````python
from queue import Queue

q = Queue(3)  # 队列：先进先出
q.put("消息1")  # put用来往队列放数据
q.put("消息2")
print(q.full())  # full判断队列是否满了
q.put("消息3")
print(q.full())

print(q.get())  # get用来取出队列中的数据
print(q.get())
print(q.get())
print(q.empty())  # empty判断队列是否为空
print(q.qsize())  # qsize 返回队列当前大小
````
#### 使用队列进行进程间通信
```python
from multiprocessing import Process, Queue
def write(queue, list):
    for i in list:
        if not queue.full():
            queue.put(i)
        else:
            raise Exception("队列已满")


def read(queue):
    while not queue.empty():
        print(queue.get())


if __name__ == "__main__":
    queue = Queue(100)
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    p1 = Process(target=write, args=(queue, li))
    p2 = Process(target=read, args=(queue,))
    p1.start()
    p1.join()  # 如果这里不等待p1执行完毕，有时候p2先执行会读不到数据
    p2.start()
```
## 进程池
### [code09_pool.py](class02-advanced%2Fcode09_pool.py)
### 进程池的基本操作
1. 创建进程池：p = Pool(N)，N表示最大进程N个
2. 异步给进程池提交任务：p.apply_async(target, args),注意args也是以元组形式提交
3. 从异步方法apply_async获取业务结果，必须使用get()方法
4. 同步给进程池提交任务：p.apply(target, args)
5. 从同步方法apply获取业务结果，apply返回值就是业务结果
6. p.close() 关闭进程池，关闭之后p不再接受新的请求
7. p.join() 阻塞主进程等待所有子进程执行完毕
### 进程池间的通信
进程池间的通信也是使用队列，但是注意使用不同模块下的队列，进程池间的通信使用的是Manager().Queue()
````python
from multiprocessing import Manager

queue = Manager().Queue()
````
## 协程
### [code10_coroutine.py](class02-advanced%2Fcode10_coroutine.py)
1. 协程：单线程下的并发
2. 协程存在的意义：    
多线程是分时切片的，线程切换需要耗时，如保存状态等   
协程只使用一个线程，在一个线程中规定代码块执行顺序   
其次协程能被程序员方便的控制执行顺序
3. 使用协程的场景：   
前面说过，**多线程适用的场景是IO密集型作业；多进程适用场景是计算密集型作业**。     
而协程是线程中的线程，其特点就是切换方便，比多线程更敏捷、高效。所以**面对IO密集型需要频繁切换线程的作业，协程更适合**。

### 创建协程
#### greenlet 创建协程
```shell
# 下载greenlet包
pip install greenlet
```
````python
from greenlet import greenlet
def process():
    print(f"save user")
    # 切换到g2协程中执行process2
    g2.switch("pdf", "word")
    print(f"save order")
def process2(a, b):
    print(f"read {a}")
    print(f"read {b}")
    # 执行完process2后继续切回g1执行process
    g1.switch()
g1 = greenlet(process)
g2 = greenlet(process2)
# 先执行g1
g1.switch()
````
#### gevent 创建协程
```shell
# 下载gevent包
pip3 install gevent
```
````python
import gevent
def funa(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # sleep用来模拟一个耗时操作，注意要用gevent的sleep
        gevent.sleep(1)


g3 = gevent.spawn(funa, 2)
g4 = gevent.spawn(funa, 2)
g5 = gevent.spawn(funa, 2)
# 启动协程
g3.join()
````
monkey.patch方法原理：  
1. monkey patch指的是在执行时动态替换,通常是在startup的时候。
2. 用过gevent就会知道,会在最开头的地方gevent.monkey.patch_all();把标准库中的thread/socket等给替换掉.这样我们在后面使用socket的时候能够跟寻常一样使用,无需改动不论什么代码,可是它变成非堵塞的了。
3. 就是把里面的函数转变成gevent协程里面的相同的函数，这样就可以说都变成导入的gevent的函数，gevent是类似一个协程空间，当你用生成协程时，就会在gevent容器空间中生成一个标记好的协程，当多个协程同时存储在容器空间时，gevent就会统一调配CPU的使用，当那个协程出现堵塞时，gevent就会马上切换执行到下一个协程标记中去，实现一个非堵塞的运行gevent容器空间！
4. gevent到底能实现哪些阻塞方法的平替呢，请直接查看patch_all方法所有参数，True的都是支持的，False的都是不支持的。
```python
def patch_all(socket=True, dns=True, time=True, select=True, thread=True, os=True, ssl=True,
              subprocess=True, sys=False, aggressive=True, Event=True,
              builtins=True, signal=True,
              queue=True, contextvars=True,
              **kwargs):
    pass
```
````python
import gevent, time
from gevent import monkey
monkey.patch_all()

def funa(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # 因为前面申明了monkey.patch_all()，所以这里的time.sleep方法被自动替换成了gevent下非阻塞的同名实现函数
        time.sleep(1)

g3 = gevent.spawn(funa, 2)
g4 = gevent.spawn(funa, 2)
g5 = gevent.spawn(funa, 2)

g3.join()
````
gevent.joinall方法：待所有协程任务，直到所有协程任务完成后才继续向后执行。

## 正则表达式
### [code11_regularexp.py](class02-advanced%2Fcode11_regularexp.py)

# 语法核心
## os模块
### [code01_os.py](class03-core%2Fcode01_os.py)
## sys模块
### [code02_sys.py](class03-core%2Fcode02_sys.py)
## time模块
### [code03_time.py](class03-core%2Fcode03_time.py)
## logging模块
### [code04_logging.py](class03-core%2Fcode04_logging.py)
1. 定义全局logger：[code04_logging.py](class03-core%2Fcode04_logging.py)
2. 在别的文件中引用该模块并使用logger
````python
import code04_logging

logger = code04_logging.logger
logger.info("这里能不能打日志")
````
