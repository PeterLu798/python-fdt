# 语法基础
## Code01.py
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

## Code02.py
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

## Code03.py
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
