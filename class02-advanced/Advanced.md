# 语法进阶
## 面向对象
### [code01_object.py](code01_object.py)
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
## [code02.py](code02.py)
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
### [code03_singleton.py](code03_singleton.py)
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
### [code04_file.py](code04_file.py)
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