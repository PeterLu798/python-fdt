# __new__()实现单例模式

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


# 通过类方法实现单例模式
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


# 通过装饰器实现单例模式
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

print("*" * 50)
# 通过导入模块时实现
from tools.time_tools import DateUtil
from tools.time_tools import DateUtil

ddd = DateUtil()
print(ddd.__module__)
print(ddd.__class__)


# 通过元类实现
class A(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "ins"):
            cls.ins = super().__new__(cls)
        return cls.ins


a1 = A()
a2 = A()
print(id(a1))
print(id(a2))


# __call__使用
class B(object):
    def __call__(self, *args, **kwargs):
        print("这是call方法")


B()()  # 这是call方法
