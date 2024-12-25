# 多继承
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

# 多态
# 1. +的多态性
print(1 + 2)  # 此处表示数学相加
print("hello" + "world")  # 此处表示字符串拼接
# 2. len函数的多态性
print(len("world"))
print(len([1, 2, 3]))


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


# 类方法
class F:
    foo = "foo"

    @classmethod  # 类方法必须使用该注解申明
    def run(cls):  # 类方法的第一个参数必须时cls
        print(f"run {cls.foo}")

    @classmethod
    def get_foo(cls):
        return cls.foo

    @classmethod
    def set_foo(cls, foo):
        cls.foo = foo


# 调用方式
F.run()  # run foo
f = F()
f.run()  # run foo


class M:
    @staticmethod  # 静态方法申明方式
    def foo(x, y):
        print(f"process {x} and {y}")


# __new__()方法
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
