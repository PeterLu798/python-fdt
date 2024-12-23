# 类型转换
int = 5
# 整数转为字符串
s = str(5)
# 字符串转为list
l = list(s)
# 字符串转为元组
tu = tuple(s)
# 字符串转为集合
set1 = set(s)
# list转为字符串
se = str(l)
# list转元组
tu1 = tuple(l)
# list转集合
se1 = set(tu1)

# 转字典（特殊）
x = ["a1", "b1", "c1", "d1"]
y = ["a2", "b2", "b3"]
z = zip(x, y)
print(dict(z))

# 深浅拷贝
a = 10
b = 10
print(id(a))  # 140705617148632
print(id(b))  # 140705617148632
s = "hello"
t = "hello"
print(id(s))  # 2905618815600
print(id(t))  # 2905618815600

l = [1, 2, 3]
m = l
print(id(l))  # 2221094530688
print(id(m))  # 2221094530688

import copy

u = [1, 2, 3]
v = copy.copy(u)
print(id(u))  # 2444626097664
print(id(v))  # 2444626493056

# 不可变对象
i = 72
print(id(i))
i += 3  # 这时i的内存地址已经变了
print(id(i))
