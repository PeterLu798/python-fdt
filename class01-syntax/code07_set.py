# 定义集合
s1 = {10, 20, 30}
print(type(s1))  # <class 'set'>
# 字符串转集合
s2 = set("hello")
print(s2)  # {'h', 'l', 'o', 'e'}
# 定义一个空集合
s3 = set()

# 增
s3.add("zoo")
s3.add(1)
s3.add(1)  # 自动去重
print(s3)  # {'zoo', 1}

# update
s4 = set()
s4.update([10, 11])
s4.update((12, 56))
print(s4)  # {56, 10, 11, 12}
s4.update({"name": "Pe"})
print(s4)  # {56, 10, 11, 12, 'name'}

# 将x、y集合合并并去重
x = {"apple", "banana", "cherry"}
y = {"google", "apple"}
x.update(y)
print(x)

x.remove("apple")
x.discard("apple")

# 交集、并集
l = {1, 2, 3, 4}
m = {3, 4, 5, 6}
# 求交集
print(l & m)  # {3, 4}
# 求并集
print(l | m)  # {1, 2, 3, 4, 5, 6}

print("*" * 50)
"""
阶段总结
"""
str = "hello world"
print(len(str))
for i in enumerate(str):
    print(i)

print("-" * 30)

list = [1, 4, 6, 2]
print(max(list))
print(min(list))
print(len(list))
for i in enumerate(list):
    print(i)

print("-" * 30)

set = {4, 5, 2, 8, 1}
print(max(set))
print(min(set))
print(len(set))
for i in enumerate(set):
    print(i)

print("-" * 30)

tup = (1, 4, 6, 3, 9)
print(max(tup))
print(min(tup))
print(len(tup))
for i in enumerate(tup):
    print(i)

print("-" * 30)

map = {"name": "ddd"}
print(len(map))
for i in enumerate(map):
    print(i)
