import time
from collections.abc import Iterable, Iterator

print(isinstance([1, 2], Iterable))  # True

list = [1, 4, 5, 2]
it = iter(list)
print(it.__next__())
print(next(it))  # next()方法内部调用了__next__方法


# 自定义迭代器
class Person:
    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        self.n += 1
        return self.n


print(isinstance(Person(), Iterator))  # True


# 生成器
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

# 生成器表达式
# 列表推导式
list1 = [i * 2 for i in range(3)]
print(list1)  # [0, 2, 4]

# 创建生成器表达式
list2 = (i * 2 for i in range(3))
print(next(list2))
print(next(list2))
print(next(list2))


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
