# 语法基础
## [Code01.py](Code01.py)
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

## [Code02.py](Code02.py)
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

## [Code03_Str.py](Code03_Str.py)
### 字符串
#### 字符编码
字符编码的本质是二进制数据与语言文字的一一对应关系  
#### 几种字符编码
1. unicode：兼容万国语言
2. utf-8：unicode的实现方式之一，优势是对不同的字符用不同的长度来表示
3. gbk：专门解决中文编码，每个字符占2字节
4. utf-8中一个英文/数字占用一个字节，一个汉字占3~4个字节
#### encode编码
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
#### decode解码
通过decode将二进制字节流转换为字符串
````python
# decode解码
s2 = b"hha"
print(s2.decode("utf-8"))
````
#### 索引
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
#### 切片
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
#### 字符串的常用操作
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

## [Code04_List.py](Code04_List.py)
### 列表
#### 列表基本性质
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
#### 列表的遍历
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
#### 列表添加元素
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
#### 列表修改元素
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
#### 列表删除元素
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
#### 列表查找元素
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
#### 列表排序
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
#### 列表推导式
````python
# 给列表中的每个元素都乘以2
dd = [1, 2, 3, 4]
print([i * 2 for i in dd])  # [2, 4, 6, 8]
````
## [Code05_Tuple.py](Code05_Tuple.py)
### 元组
元组是不可变的list类型，不可以增删改。   
意义：因为元组不支持增删改，所以提高了代码编写的安全性，如果有只读场景，可以考虑使用元组。    
#### 元组的定义   
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
#### 元组的操作
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