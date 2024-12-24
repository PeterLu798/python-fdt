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

# 全局变量和局部变量
cup = 100  # 全局变量


def fune():
    global cup
    cup = 200  # 全局变量
    print(f"fune print {cup}")  # fune print 200


def funf():
    print(f"funf print {cup}")  # funf print 200


fune()
funf()

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

# 匿名函数
funadd = lambda x, y: x + y
print(funadd(4, 5))  # 9

funk = lambda x, y: x if x > y else y
print(funk(4, 5))  # 5

# zip
a = [1, 2, 3, 4]
b = ["a", "b", "c", "d"]
z = zip(a, b)
# 然后就可以将z转成各种数据类型
print(dict(z))  # 转map {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# print(list(z))#转list [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# print(set(z))  # 转集合 {(4, 'd'), (2, 'b'), (3, 'c'), (1, 'a')}

# map
funm = lambda x: x * x
li = [1, 2, 4, 8]
print(list(map(funm, li)))  # [1, 4, 16, 64]

# reduce
from functools import reduce

li = [1, 2, 3, 4]
print(reduce(funadd, li))  # 10

# enumerate
for i, num in enumerate(li):
    print(i, num)

print("*" * 50)


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


# 抛出异常
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
