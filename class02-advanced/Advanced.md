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
## 迭代器
### [code05_iterator.py](code05_iterator.py)
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
### [code06_thread.py](code06_thread.py)
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
### [code07_lock.py](code07_lock.py)
1. 创建一把锁：local = Lock()
2. 上锁：local.acquire()；解锁：local.release()
3. 上锁和解锁必须成对出现，上完锁解锁之后才能继续上锁，否则会死锁

## 多进程
### [code08_process.py](code08_process.py)
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
### [code09_pool.py](code09_pool.py)
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
### [code10_coroutine.py](code10_coroutine.py)
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