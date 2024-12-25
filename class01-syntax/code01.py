import keyword

"""
bug、注释与输出
"""
print('hello world', '你好')
print('可以修改end', end=',')
print('')

"""
变量
"""
a = 10
# 查看关键字
print(keyword.kwlist)

"""
数值类型
"""
# int
num = 10
print(type(num))  # <class 'int'>

# float: 所有带小数点的
numf = 1.2
# 3.1E5 == 3.1 * 10^5
numf2 = 3.1E5
print(type(numf2))  # <class 'float'>

# bool
print(True)
print(False)

"""
字符串
"""
str = """
hello
  python  
    I'm here
""";
print(str)
print("a" + "b")
print("*" * 50)
print("a" in "hello")
print("h" in "hello")
print("o" not in "hello")
print(r"\n")

"""
格式化输出
"""
age = 18
name = "Wil"
height = 170.3
print("我的名字是%s，我的年龄是%d，我的身高是%.1fcm" % (name, age, height))

print("My name is {}, my age is {}".format(name, age))
print("My name is {0}, my age is {1}, my brother's name is {0} too".format(name, age))
print("用户名{userName} 密码是{pwd}".format(userName="root", pwd="123"))

print(f'My name is {name}, my age is {age}')
