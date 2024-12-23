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
